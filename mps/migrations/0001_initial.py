# Generated by Django 5.0.6 on 2024-06-22 13:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberOfParliament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.URLField(default='https://img.freepik.com/free-vector/illustration-businessman_53876-5856.jpg?w=740&t=st=1719052890~exp=1719053490~hmac=4e6f9ee8ae73ee004e482dc13a877e58d9dc91abcc31b2f6cfe9d878199eaba6')),
                ('county', models.CharField(max_length=100)),
                ('constituency', models.CharField(max_length=100)),
                ('party', models.CharField(max_length=100)),
                ('tokenized_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
