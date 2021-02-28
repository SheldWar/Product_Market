# Generated by Django 3.1.7 on 2021-02-28 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0, verbose_name='Скидка в %'),
        ),
    ]