# Generated by Django 4.2.4 on 2023-08-29 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_time_uploaded_documents_upload_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]