# Generated by Django 3.1.7 on 2021-07-16 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='t_address',
            new_name='destination',
        ),
        migrations.RemoveField(
            model_name='student',
            name='parents_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='std_address',
        ),
        migrations.RemoveField(
            model_name='student',
            name='std_email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='std_gender',
        ),
        migrations.RemoveField(
            model_name='student',
            name='std_phone',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='t_email',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='t_phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False, verbose_name='student status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_teacher',
            field=models.BooleanField(default=False, verbose_name='teacher status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]