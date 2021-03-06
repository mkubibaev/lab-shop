# Generated by Django 3.0.6 on 2020-05-30 12:18

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
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(max_length=2000, verbose_name='Description')),
                ('category', models.CharField(choices=[('tech', 'Technology'), ('books', 'Books'), ('food', 'Food'), ('other', 'Other')], default='tech', max_length=40, verbose_name='Category')),
                ('count', models.IntegerField(verbose_name='Count')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price')),
            ],
        ),
    ]
