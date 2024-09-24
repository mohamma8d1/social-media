# Generated by Django 4.2 on 2024-09-13 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('request_from', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='friend_request_from', to=settings.AUTH_USER_MODEL)),
                ('request_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='friend_request_to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Friendship',
                'verbose_name_plural': 'Friendship',
                'unique_together': {('request_from', 'request_to')},
            },
        ),
    ]
