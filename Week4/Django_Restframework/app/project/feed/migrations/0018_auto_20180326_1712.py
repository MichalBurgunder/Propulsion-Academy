# Generated by Django 2.0.3 on 2018-03-26 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0017_userprofile_sprichwort'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created'], 'verbose_name': ('Post',), 'verbose_name_plural': ('Posts',)},
        ),
    ]
