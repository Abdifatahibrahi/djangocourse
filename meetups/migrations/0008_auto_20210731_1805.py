# Generated by Django 3.2.5 on 2021-07-31 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0007_auto_20210731_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='meetups',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, to='meetups.Participants'),
        ),
    ]