# Generated by Django 4.2.4 on 2023-10-08 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_waitinglist'),
    ]

    operations = [
        migrations.AddField(
            model_name='waitinglist',
            name='order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='waiting_list', to='orders.order'),
            preserve_default=False,
        ),
    ]
