# Generated by Django 4.2.2 on 2023-07-03 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_beer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCartlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('beers', models.ManyToManyField(to='main_app.beer')),
            ],
        ),
    ]