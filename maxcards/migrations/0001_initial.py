# Generated by Django 4.2.4 on 2023-08-31 19:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.UUIDField(default=uuid.uuid4)),
                ('account_holder', models.CharField(max_length=30)),
                ('card_number', models.CharField(max_length=12)),
                ('cvv', models.IntegerField()),
                ('price', models.FloatField()),
                ('card_type', models.CharField(choices=[('Visa', 'Visa Card'), ('Master', 'Master Card')], max_length=8)),
            ],
            options={
                'verbose_name_plural': 'Card',
            },
        ),
        migrations.CreateModel(
            name='Payment_screenshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('transaction_type', models.CharField(max_length=100)),
                ('sent_on', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(null=True, upload_to='Screenshots')),
            ],
            options={
                'verbose_name_plural': 'Payment_screenshots',
            },
        ),
        migrations.CreateModel(
            name='User_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('order_status', models.CharField(choices=[('Pending', 'Pending'), ('Declined', 'Declined'), ('Approved', 'Approved')], default='Pending', max_length=8, null=True)),
                ('transaction_type', models.CharField(max_length=100, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maxcards.cards')),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
