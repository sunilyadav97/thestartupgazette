# Generated by Django 4.1.3 on 2022-12-25 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='../static/img/deafult.jpg', null=True, upload_to='post_images'),
        ),
    ]
