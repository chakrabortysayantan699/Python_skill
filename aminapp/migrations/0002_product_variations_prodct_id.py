# Generated by Django 4.1.1 on 2022-12-29 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_variations',
            name='prodct_id',
            field=models.IntegerField(default=999),
        ),
    ]