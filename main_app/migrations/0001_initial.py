# Generated by Django 3.1 on 2020-09-14 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('media_type', models.CharField(choices=[('C', 'Camera Photography'), ('D', 'Digital Artwork'), ('J', 'CSS codepen'), ('P', 'Painting'), ('S', 'Sketch Drawing')], max_length=1)),
                ('genre', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('colors_used', models.TextField(max_length=250)),
                ('karma', models.IntegerField()),
                ('date_posted', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.user')),
            ],
        ),
    ]
