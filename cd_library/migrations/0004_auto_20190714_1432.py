# Generated by Django 2.2.3 on 2019-07-14 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cd_library', '0003_auto_20190710_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cd',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.RemoveField(
            model_name='cd',
            name='type',
        ),
        migrations.AddField(
            model_name='cd',
            name='type',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='cd_library.Types'),
            preserve_default=False,
        ),
    ]
