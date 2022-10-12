# Generated by Django 4.1.1 on 2022-10-10 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='post_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='upload_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
