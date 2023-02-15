# Generated by Django 4.1.6 on 2023-02-15 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0002_alter_rack_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='rack',
        ),
        migrations.AddField(
            model_name='sample',
            name='rack',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='scanner.rack'),
        ),
    ]
