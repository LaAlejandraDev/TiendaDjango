# Generated by Django 5.1.6 on 2025-03-06 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto_nombre', models.TextField(max_length=100)),
                ('producto_precio', models.FloatField(max_length=100)),
                ('producto_imagen', models.ImageField(blank=True, null=True, upload_to='productos/')),
            ],
            options={
                'ordering': ['id'],
                'permissions': [('poder_agregar_productos', 'Puede usar crud productos')],
            },
        ),
    ]
