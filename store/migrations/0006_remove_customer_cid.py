# Generated by Django 4.1.7 on 2023-03-21 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_customer_cid_alter_customer_customer_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="cid",
        ),
    ]
