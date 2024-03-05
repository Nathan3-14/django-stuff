# Generated by Django 5.0.3 on 2024-03-04 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=30)),
                ('post_body', models.CharField(max_length=300)),
                ('post_pub_date', models.DateTimeField(verbose_name='Date Published')),
            ],
        ),
    ]