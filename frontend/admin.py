from django.contrib import admin

from .models import Project, ProjectMembership, Download, Release, GameVersion

class ProjectMembershipInline(admin.TabularInline):
    model = ProjectMembership

class DownloadInline(admin.TabularInline):
    model = Download

class ReleaseInline(admin.TabularInline):
    model = Release

class ReleaseAdmin(admin.ModelAdmin):
    inlines = [
        DownloadInline,
    ]

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        ProjectMembershipInline,
        ReleaseInline,
    ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Release, ReleaseAdmin)
admin.site.register(GameVersion)
