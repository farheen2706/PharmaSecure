# Generated by Django 5.1.6 on 2025-02-16 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0022_alter_employee_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(blank=True, default='pbkdf2_sha256$870000$TkPK6zzUQ1vdBwtFx8kP9C$KZ2yroDwxSSlZa41sPQEIY/O5UzB1s/6mTRsK29mP1o=', max_length=128, null=True),
        ),
    ]
