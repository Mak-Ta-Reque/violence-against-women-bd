# Generated by Django 3.0.7 on 2020-06-17 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20200617_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='country',
        ),
        migrations.RemoveField(
            model_name='item',
            name='todolist',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='ToDoList',
        ),
    ]