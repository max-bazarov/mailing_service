# Generated by Django 4.1.4 on 2022-12-19 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0003_alter_mailing_start_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('not_sent', 'Not Sent'), ('sent', 'Sent'), ('failed', 'Failed')], default='not_sent', max_length=255),
        ),
    ]