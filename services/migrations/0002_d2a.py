# Generated by Django 3.2 on 2021-05-24 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OPAL', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='D2A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('D2A_completion_date', models.DateField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OPAL.patient')),
                ('therapist_completing_d2a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OPAL.therapist')),
            ],
        ),
    ]
