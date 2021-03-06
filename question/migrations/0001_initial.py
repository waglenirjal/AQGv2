# Generated by Django 3.1 on 2020-09-18 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllQues',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('subID', models.CharField(max_length=20)),
                ('Question', models.TextField()),
                ('mark', models.IntegerField()),
                ('level', models.IntegerField()),
                ('teacherID', models.CharField(max_length=20)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MathQues',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('Question', models.TextField()),
                ('optA', models.CharField(max_length=255)),
                ('optB', models.CharField(max_length=255)),
                ('optC', models.CharField(max_length=255)),
                ('optD', models.CharField(max_length=255)),
                ('ans', models.CharField(max_length=10)),
                ('mark', models.IntegerField()),
                ('level', models.IntegerField()),
                ('teacherName', models.CharField(max_length=20)),
                ('mathID', models.CharField(blank=True, max_length=20)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicsQues',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('Question', models.TextField()),
                ('optA', models.CharField(max_length=255)),
                ('optB', models.CharField(max_length=255)),
                ('optC', models.CharField(max_length=255)),
                ('optD', models.CharField(max_length=255)),
                ('ans', models.CharField(max_length=10)),
                ('mark', models.IntegerField()),
                ('level', models.IntegerField()),
                ('teacherID', models.CharField(max_length=20)),
                ('mathID', models.CharField(blank=True, max_length=20)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('subID', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
