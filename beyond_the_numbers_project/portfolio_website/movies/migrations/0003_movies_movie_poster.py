# Generated by Django 4.1.7 on 2023-03-23 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_rename_moviesss_movies"),
    ]

    operations = [
        migrations.AddField(
            model_name="movies",
            name="movie_poster",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
    ]
