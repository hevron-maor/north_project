# Generated by Django 2.2.4 on 2019-09-03 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190830_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardpage',
            name='theme',
            field=models.CharField(choices=[('white', 'White'), ('black', 'Black')], default='white', max_length=250),
        ),
    ]
