# Generated by Django 5.1.6 on 2025-02-26 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_alter_user_email_alter_user_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerApplication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Очікує розгляду'), ('in_progress', 'В обробці'), ('resolved', 'Вирішено')], default='pending', max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
