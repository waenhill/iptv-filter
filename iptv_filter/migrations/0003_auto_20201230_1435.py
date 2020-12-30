# Generated by Django 3.1.4 on 2020-12-30 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iptv_filter', '0002_auto_20201230_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='epgchannel',
            name='output_representation',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='epgprogramme',
            name='output_representation',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playlistchannel',
            name='output_representation',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]