# Generated by Django 2.2.3 on 2019-07-14 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cd_library', '0004_auto_20190714_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cd',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cd_library.Types'),
        ),
    ]
