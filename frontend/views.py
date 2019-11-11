import functools

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .forms import CreateProjectForm
from .models import Project, GameVersion


def index(request):
    projects = Project.objects.all()
    return render(request, "frontend/index.html", {"projects": projects})


class ProjectListView(ListView):
    queryset = Project.objects.order_by("-last_updated")
    paginate_by = 10
    template_name = "frontend/index.html"
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    queryset = Project.objects.all()
    context_object_name = "project"
    template_name = "frontend/project.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["game_versions"] = list(map(functools.partial(ProjectDetailView.annotate_project_releases, context["project"]),
                                            GameVersion.objects.filter(release__in=context[
                                                "project"].release_set.all()).distinct()))  # without distinct(), the QuerySet lists each GameVersion as often as releases reference it
        return context

    @staticmethod
    def annotate_project_releases(project: Project, game_version: GameVersion):
        releases = game_version.release_set.filter(project=project).order_by("-release_date")
        result_releases = []
        for channel in range(1, 4):
            result_releases.extend(releases.filter(channel=channel)[:1])
        game_version.project_releases = result_releases
        return game_version

class CreateProjectView(CreateView):
    form_class = CreateProjectForm
