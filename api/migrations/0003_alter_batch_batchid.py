# Generated by Django 3.2.7 on 2022-12-11 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_batch_batchid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batchId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]