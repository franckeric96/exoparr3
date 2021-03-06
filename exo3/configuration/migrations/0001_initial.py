# Generated by Django 2.2.10 on 2020-03-15 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/InfoSite')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'InfoSite',
                'verbose_name_plural': 'InfoSites',
            },
        ),
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('icon', models.CharField(choices=[('Facebook', 'fa-facebook'), ('twitter', 'fa-twitter'), ('Google-plus', 'fa-google-plus'), ('Linkedin', 'fa-linkedin')], max_length=20)),
                ('lien', models.URLField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Social Account',
                'verbose_name_plural': 'Social Accounts',
            },
        ),
    ]
