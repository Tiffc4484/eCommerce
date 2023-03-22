# Generated by Django 4.1.7 on 2023-03-21 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("store", "0007_rename_orderitem_orderhasproduct"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="digital",
            new_name="is_on_sale",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="name",
            new_name="product_name",
        ),
        migrations.AddField(
            model_name="customer",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="available_stock",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="cost",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.FloatField(null=True),
        ),
    ]