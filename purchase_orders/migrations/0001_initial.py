# Generated by Django 4.2.5 on 2024-05-06 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0002_alter_vendor_average_response_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(max_length=100)),
                ('order_date', models.DateField()),
                ('delivery_date', models.DateField()),
                ('items', models.TextField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('SHIPPED', 'Shipped'), ('DELIVERED', 'Delivered')], default='PENDING', max_length=20)),
                ('quality_rating', models.FloatField(default=0.0)),
                ('issue_date', models.DateField(auto_now_add=True)),
                ('acknowledgement_date', models.DateField(blank=True, null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor')),
            ],
        ),
    ]
