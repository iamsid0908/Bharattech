# Generated by Django 4.0.3 on 2023-11-30 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_challanges'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenges',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('problemstatement', models.TextField()),
                ('sample_input_1', models.TextField()),
                ('sample_input_2', models.TextField()),
                ('sample_output_1', models.TextField()),
                ('sample_output_2', models.TextField()),
                ('explanations', models.TextField()),
                ('language', models.CharField(choices=[('1', 'Python'), ('2', 'Java'), ('3', 'CPP')], default='1', max_length=10)),
                ('stack', models.CharField(choices=[('1', 'frontend'), ('2', 'backtend')], max_length=20)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users.user',),
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.DeleteModel(
            name='Challanges',
        ),
    ]
