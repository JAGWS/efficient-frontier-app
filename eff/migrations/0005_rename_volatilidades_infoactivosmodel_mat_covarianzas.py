# Generated by Django 3.2.6 on 2021-09-03 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eff', '0004_infoactivosmodel_num_activos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infoactivosmodel',
            old_name='volatilidades',
            new_name='mat_covarianzas',
        ),
    ]
