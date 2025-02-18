# Generated by Django 5.1.5 on 2025-01-25 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, choices=[('BRAZIL', 'Brasil'), ('USA', 'Estados Unidos'), ('CHILE', 'Chile')], max_length=100, null=True)),
            ],
        ),
    ]
