# Generated by Django 3.0.5 on 2020-06-23 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=200)),
                ('end_time', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='Member',
            new_name='User',
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.AddField(
            model_name='activityperiod',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
