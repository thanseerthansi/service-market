# Generated by Django 4.0.5 on 2022-06-20 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0003_rename_services_servicetypemodel_service'),
        ('userapp', '0003_usermodel_is_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_date', models.DateField()),
                ('locattion', models.CharField(max_length=100)),
                ('living_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='serviceapp.servicemodel')),
                ('userid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
