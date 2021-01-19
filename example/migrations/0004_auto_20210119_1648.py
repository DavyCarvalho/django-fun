# Generated by Django 3.1.5 on 2021-01-19 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0003_album_musician'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='shirt_size',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default=False, max_length=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(blank=True, default=False),
        ),
    ]
