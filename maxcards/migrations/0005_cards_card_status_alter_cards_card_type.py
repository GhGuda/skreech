# Generated by Django 4.2.3 on 2023-07-07 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maxcards', '0004_cards_card_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='card_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Declined', 'Declined'), ('Approved', 'Approved')], default='Pending', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='cards',
            name='card_type',
            field=models.CharField(choices=[('Visa', 'Visa'), ('Master', 'Master')], max_length=8),
        ),
    ]