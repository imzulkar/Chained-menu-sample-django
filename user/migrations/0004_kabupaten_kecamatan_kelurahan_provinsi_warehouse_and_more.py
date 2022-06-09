# Generated by Django 4.0.4 on 2022-06-03 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_phase_project_alter_user_profile_pic_projectphase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kabupaten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.IntegerField(blank=True, null=True)),
                ('provinsi_code', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'kabupaten',
                'db_table': 'kabupaten',
            },
        ),
        migrations.CreateModel(
            name='Kecamatan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.IntegerField(blank=True, null=True)),
                ('kabupaten_code', models.IntegerField(blank=True, null=True)),
                ('kabupaten', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.kabupaten')),
            ],
            options={
                'verbose_name_plural': 'kecamatan',
                'db_table': 'kecamatan',
            },
        ),
        migrations.CreateModel(
            name='Kelurahan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.BigIntegerField(blank=True, null=True)),
                ('kecamatan_code', models.IntegerField(blank=True, null=True)),
                ('kecamatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.kecamatan')),
            ],
            options={
                'verbose_name_plural': 'kelurahan',
                'db_table': 'kelurahan',
            },
        ),
        migrations.CreateModel(
            name='Provinsi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('code', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'provinsi',
                'db_table': 'provinsi',
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kabupaten', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_kabupaten', to='user.kabupaten')),
                ('kecamatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_kecamatan', to='user.kecamatan')),
                ('kelurahan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_kelurahan', to='user.kelurahan')),
                ('provinsi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_provinsi', to='user.provinsi')),
            ],
        ),
        migrations.AddField(
            model_name='kabupaten',
            name='provinsi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.provinsi'),
        ),
    ]