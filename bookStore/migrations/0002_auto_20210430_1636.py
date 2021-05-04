# Generated by Django 3.2 on 2021-04-30 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookStore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdetails',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='bookdetails',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookdetails',
            name='quanity_remaining',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]