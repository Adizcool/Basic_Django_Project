# Generated by Django 4.1.6 on 2023-02-09 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updatedby', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='centra_inventory.basemodel')),
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('purchase_id', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In-Transit', 'In-Transit'), ('Delivered', 'Delivered')], max_length=100)),
            ],
            bases=('centra_inventory.basemodel',),
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='centra_inventory.basemodel')),
                ('side_id', models.IntegerField(primary_key=True, serialize=False)),
                ('site_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
            ],
            bases=('centra_inventory.basemodel',),
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='centra_inventory.basemodel')),
                ('serial_number', models.IntegerField(primary_key=True, serialize=False)),
                ('ip_address', models.CharField(max_length=100)),
                ('mac_address', models.CharField(max_length=100)),
                ('switch_model', models.CharField(max_length=100)),
                ('switch_status', models.CharField(max_length=20)),
                ('switch_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='switchorder', to='centra_inventory.order')),
                ('switch_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='switchsite', to='centra_inventory.site')),
            ],
            bases=('centra_inventory.basemodel',),
        ),
        migrations.CreateModel(
            name='IAP',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='centra_inventory.basemodel')),
                ('serial_number', models.IntegerField(primary_key=True, serialize=False)),
                ('ip_address', models.CharField(max_length=100)),
                ('mac_address', models.CharField(max_length=100)),
                ('IAP_model', models.CharField(max_length=100)),
                ('IAP_status', models.CharField(max_length=100)),
                ('is_virtual', models.BooleanField(max_length=100)),
                ('IAP_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iaporder', to='centra_inventory.order')),
                ('IAP_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iapsite', to='centra_inventory.site')),
            ],
            bases=('centra_inventory.basemodel',),
        ),
    ]
