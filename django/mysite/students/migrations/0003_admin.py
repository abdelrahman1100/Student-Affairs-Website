# Generated by Django 4.1.4 on 2022-12-25 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('admin', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
