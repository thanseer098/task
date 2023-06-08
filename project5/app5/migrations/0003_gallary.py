# Generated by Django 4.1.2 on 2023-05-20 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app5', '0002_alter_register_password_alter_register_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('price', models.CharField(max_length=250)),
            ],
        ),
    ]