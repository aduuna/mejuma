# Generated by Django 2.0.7 on 2018-08-02 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=255, verbose_name='Short Statement'),
        ),
        migrations.AddField(
            model_name='user',
            name='call_number',
            field=models.IntegerField(blank=True, default=0, verbose_name='Default Call/SMS No.'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=255, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='user',
            name='whatsapp_number',
            field=models.CharField(blank=True, max_length=14, verbose_name='WhatsApp No.'),
        ),
    ]
