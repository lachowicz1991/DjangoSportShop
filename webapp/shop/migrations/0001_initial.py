# Generated by Django 3.2.9 on 2021-11-15 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OutdoorIndoor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SportCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('rental_price', models.FloatField(null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('date_created', models.CharField(max_length=200, null=True)),
                ('category', models.ManyToManyField(null=True, to='shop.SportCategory')),
                ('gender', models.ManyToManyField(null=True, to='shop.Gender')),
                ('item_type', models.ManyToManyField(null=True, to='shop.OutdoorIndoor')),
                ('rental', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.rental')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.status')),
            ],
        ),
    ]
