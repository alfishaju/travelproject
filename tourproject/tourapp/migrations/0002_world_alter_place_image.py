# Generated by Django 4.2.3 on 2023-07-12 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='world',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='wats')),
                ('des', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
    ]
