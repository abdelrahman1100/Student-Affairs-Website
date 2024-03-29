# Generated by Django 4.1.4 on 2022-12-26 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_student_dept'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraduatedStudent',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('dept', models.CharField(max_length=3)),
            ],
        ),
    ]
