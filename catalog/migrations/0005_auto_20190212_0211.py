# Generated by Django 2.1.5 on 2019-02-12 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
