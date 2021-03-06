# Generated by Django 2.0.4 on 2018-05-31 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_remove_student_progress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='attendance',
        ),
        migrations.AddField(
            model_name='attendance',
            name='attendance_month',
            field=models.CharField(default='May', max_length=20),
        ),
        migrations.AddField(
            model_name='attendance',
            name='attendance_year',
            field=models.CharField(default='2018', max_length=20),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='student.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='guardian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='student.Guardian'),
        ),
    ]
