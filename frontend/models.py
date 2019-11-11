from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.shortcuts import reverse

import enum


class GameVersion(models.Model):
    name = models.CharField(max_length=16)
    release_date = models.DateTimeField()


class ProjectMembershipTypes(enum.IntEnum):
    OWNER = enum.auto()
    MEMBER = enum.auto()


class ReleaseChannels:
    ALPHA = 1
    BETA = 2
    RELEASE = 3


RELEASE_CHANNEL_NAMES = (
    (ReleaseChannels.ALPHA, "Alpha"),
    (ReleaseChannels.BETA, "Beta"),
    (ReleaseChannels.RELEASE, "Release"),
)


class ProjectMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    type = models.IntegerField()


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField()
    last_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    members = models.ManyToManyField(User, through=ProjectMembership)

    def __str__(self):
        return f"<Project: {self.name}>"

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})


class Release(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    game_version = models.ForeignKey(GameVersion, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    channel = models.SmallIntegerField(choices=RELEASE_CHANNEL_NAMES)
    release_date = models.DateTimeField(default=now)


class Download(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE)
    human_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    downloads = models.BigIntegerField()
    file = models.FileField()
