# Generated by Django 4.1.3 on 2022-12-20 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_video', '0007_playlistitem_author_alter_playlistitem_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
    ]
