# Generated by Django 5.2 on 2025-04-13 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_autor_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='telefone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
