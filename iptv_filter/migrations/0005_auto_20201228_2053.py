# Generated by Django 3.1.4 on 2020-12-28 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iptv_filter', '0004_auto_20201228_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlistchannel',
            name='included',
            field=models.BooleanField(default=None),
        ),
    ]