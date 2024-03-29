# Generated by Django 4.0.6 on 2022-08-22 20:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import short_url_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourse_url', models.URLField(max_length=1000, validators=[django.core.validators.URLValidator])),
                ('short_url', models.CharField(db_index=True, default=short_url_app.models.generate_short_url_string, max_length=6, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
