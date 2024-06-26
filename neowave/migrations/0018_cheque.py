# Generated by Django 4.0 on 2024-04-05 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('neowave', '0017_transaction_receiver_balance_after_transaction_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cheque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cheque_number', models.CharField(max_length=20, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('issuer', models.CharField(max_length=100)),
                ('recipient', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('cleared', 'Cleared'), ('stopped', 'Stopped')], default='pending', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cheques_created', to='auth.user')),
                ('stopped_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cheques_stopped', to='auth.user')),
                ('user_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neowave.account')),
            ],
        ),
    ]
