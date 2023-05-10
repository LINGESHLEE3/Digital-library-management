# Generated by Django 4.1.4 on 2023-01-20 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=50)),
                ('a_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=50)),
                ('s_password', models.CharField(max_length=50)),
                ('s_phone', models.BigIntegerField()),
                ('s_semester', models.IntegerField()),
                ('s_course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Issue_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_date', models.DateField()),
                ('e_date', models.DateField()),
                ('bk_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.book')),
                ('std_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.student')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.course'),
        ),
    ]