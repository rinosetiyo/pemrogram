# Generated by Django 5.1.5 on 2025-02-11 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='featured_blog',
            new_name='is_featured',
        ),
    ]
