# Generated by Django 4.1.1 on 2022-09-25 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainblog', '0002_post_pv_post_uv'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_md',
            field=models.BooleanField(default=False, verbose_name='Markdown语法'),
        ),
    ]
