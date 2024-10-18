# Generated by Django 5.1 on 2024-10-10 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0007_remove_userdetail_email_remove_userdetail_uname'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('info', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=50)),
            ],
        ),
    ]