# Generated by Django 4.2 on 2023-04-29 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0004_alter_profile_avatar_alter_profile_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ended_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
