# Generated by Django 2.1.5 on 2019-01-31 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0016_remove_appuser_listens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='songs',
            field=models.ManyToManyField(related_name='album', to='recommend.Song'),
        ),
    ]
