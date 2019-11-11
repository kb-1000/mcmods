# Generated by Django 2.2.7 on 2019-11-12 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('release_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('channel', models.SmallIntegerField(choices=[(1, 'Alpha'), (2, 'Beta'), (3, 'Release')])),
                ('release_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('game_version', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='frontend.GameVersion')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(through='frontend.ProjectMembership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('human_name', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('downloads', models.BigIntegerField()),
                ('file', models.FileField(upload_to='')),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Release')),
            ],
        ),
    ]