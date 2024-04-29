# Generated by Django 5.0.1 on 2024-04-16 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0006_remove_payment_tbl_buyer'),
    ]

    operations = [
        migrations.CreateModel(
            name='outpayment_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=300)),
                ('numb', models.IntegerField()),
                ('item', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='payment_tbl',
            new_name='inpayment_tbl',
        ),
    ]