# Generated by Django 4.1.6 on 2023-02-15 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0003_remove_sample_rack_sample_rack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='rack',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='scanner.rack'),
        ),
    ]
