# Generated by Django 5.2.3 on 2025-06-20 15:40

import core.models
import django.core.validators
import django.db.models.deletion
import django.db.models.functions.text
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[core.models.validate_restaurant_name_begins_with_a])),
                ('website', models.URLField(default='')),
                ('date_opened', models.DateField()),
                ('latitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
                ('longitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('restaurant_type', models.CharField(choices=[('IN', 'Indian'), ('CH', 'Chinese'), ('IT', 'Italian'), ('GR', 'Greek'), ('MX', 'Mexican'), ('FF', 'Fast Food'), ('OT', 'Other')], max_length=2)),
            ],
            options={
                'ordering': [django.db.models.functions.text.Lower('name')],
                'get_latest_by': 'date_opened',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='core.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.DecimalField(decimal_places=2, max_digits=8)),
                ('datetime', models.DateTimeField()),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sales', to='core.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='StaffRestaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.FloatField(null=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.restaurant')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.staff')),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='restaurants',
            field=models.ManyToManyField(through='core.StaffRestaurant', to='core.restaurant'),
        ),
    ]
