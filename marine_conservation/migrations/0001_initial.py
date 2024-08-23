# Generated by Django 5.1 on 2024-08-23 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConservationInitiative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('website', models.URLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='conservation_initiatives')),
            ],
        ),
        migrations.CreateModel(
            name='EndangeredSpecies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('species_type', models.CharField(max_length=50)),
                ('conservation_status', models.CharField(max_length=50)),
                ('habitat', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='endangered_species')),
            ],
        ),
        migrations.CreateModel(
            name='MarineProtectedArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('ecosystem_type', models.CharField(max_length=100)),
                ('conservation_status', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='protected_areas')),
            ],
        ),
    ]
