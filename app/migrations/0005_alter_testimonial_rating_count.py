# Generated by Django 5.1.3 on 2024-12-07 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_testimonal_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='rating_count',
            field=models.IntegerField(choices=[(1, 'one'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')]),
        ),
    ]
