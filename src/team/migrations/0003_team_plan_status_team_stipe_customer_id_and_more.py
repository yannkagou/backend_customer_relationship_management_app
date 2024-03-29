# Generated by Django 5.0.1 on 2024-01-27 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_plan_team_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='plan_status',
            field=models.CharField(choices=[('active', 'Active'), ('cancelled', 'Cancelled')], default='active', max_length=255),
        ),
        migrations.AddField(
            model_name='team',
            name='stipe_customer_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='stipe_subscription_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
