# Generated by Django 4.1.3 on 2022-12-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_video', '0002_playlistitem_status_alter_status_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlistitem',
            name='status',
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(blank=True, default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playlistitem',
            name='status',
            field=models.ManyToManyField(blank=True, null=True, to='course_video.status'),
        ),
    ]
