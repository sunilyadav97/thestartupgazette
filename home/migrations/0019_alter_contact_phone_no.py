# Generated by Django 4.1.3 on 2023-03-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_contact_created_at_alter_contact_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_no',
            field=models.IntegerField(blank=True, null=True, verbose_name='Phone No'),
        ),
    ]