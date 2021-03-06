# Generated by Django 3.2 on 2021-05-01 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookStore', '0002_auto_20210430_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdetails',
            name='timeAdded',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='bookdetails',
            name='Author_First',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bookdetails',
            name='Author_Last',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bookdetails',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
