# Generated by Django 2.2.5 on 2019-09-14 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studentinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std', models.IntegerField()),
                ('fees', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.FloatField()),
                ('dateTxn', models.DateField()),
                ('receipt', models.FileField(blank=True, null=True, upload_to='receipts/')),
                ('rollNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentinfo.Student')),
            ],
        ),
    ]
