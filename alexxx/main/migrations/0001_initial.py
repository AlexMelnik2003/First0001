# Generated by Django 5.0.3 on 2024-03-12 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_file', models.FileField(upload_to='files/')),
                ('my_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
