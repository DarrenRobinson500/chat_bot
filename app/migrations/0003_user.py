# Generated by Django 4.1.5 on 2023-01-21 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_label_past_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.label')),
            ],
        ),
    ]
