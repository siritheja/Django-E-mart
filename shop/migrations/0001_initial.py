# Generated by Django 3.1.5 on 2021-01-16 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('disc_price', models.FloatField()),
                ('category', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='product/default.jpg', upload_to='product/')),
            ],
        ),
    ]
