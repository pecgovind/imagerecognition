# Generated by Django 3.2 on 2021-04-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScannedDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'scanned_document',
            },
        ),
    ]
