# Generated by Django 3.0.7 on 2020-07-14 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pno', models.IntegerField()),
                ('pname', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('pimage', models.ImageField(upload_to='suresh/')),
            ],
        ),
    ]
