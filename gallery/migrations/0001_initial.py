# Generated by Django 3.0.3 on 2020-02-17 17:51

from django.db import migrations, models
import django.db.models.deletion
import gallery.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='album name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'photo album',
                'verbose_name_plural': 'photo albums',
                'db_table': 'photo_album',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=gallery.models.upload_path, verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='gallery.PhotoAlbum')),
            ],
            options={
                'verbose_name': 'photo',
                'verbose_name_plural': 'photos',
                'db_table': 'photo',
            },
        ),
    ]