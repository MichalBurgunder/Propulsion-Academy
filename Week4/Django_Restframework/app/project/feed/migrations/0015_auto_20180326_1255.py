# Generated by Django 2.0.3 on 2018-03-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0014_auto_20180326_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='share_relation',
            field=models.TextField(verbose_name='share_relation'),
        ),
    ]
