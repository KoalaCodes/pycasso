# Generated by Django 3.1 on 2020-09-19 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('media_type', models.CharField(choices=[('C', 'Camera Photography'), ('D', 'Digital Artwork'), ('J', 'CSS codepen'), ('P', 'Painting'), ('S', 'Sketch Drawing')], max_length=1)),
                ('genre', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('colors_used', models.TextField(max_length=250)),
                ('karma', models.IntegerField(default=1)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('is_public', models.BooleanField(default=True)),
                ('url', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaintFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.TextField()),
                ('canvas_image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=500)),
                ('birthday', models.DateField(default='2020-09-17')),
                ('artist_type', models.CharField(choices=[('1', 'Photographer'), ('2', 'Painter'), ('3', 'Digital Illustrator')], default='C', max_length=25)),
                ('is_public', models.BooleanField(default=True)),
                ('location', models.CharField(max_length=100)),
                ('profile_img', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500)),
                ('rating', models.IntegerField()),
                ('date_created', models.DateField()),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.art')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
