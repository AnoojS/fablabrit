# Generated by Django 4.0.5 on 2022-07-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery')),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
    ]
