# Generated by Django 2.2.1 on 2019-05-23 14:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=models.SET(-1), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
