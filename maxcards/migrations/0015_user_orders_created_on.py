# Generated by Django 4.2.3 on 2023-07-10 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maxcards', '0014_remove_cards_transaction_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_orders',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]