# Generated by Django 5.1.1 on 2024-10-04 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_preschool_charges'),
    ]

    operations = [
        migrations.CreateModel(
            name='school_cca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=255)),
                ('school_section', models.CharField(max_length=255)),
                ('cca_grouping_desc', models.CharField(max_length=255)),
                ('cca_generic_name', models.CharField(max_length=255)),
                ('cca_customized_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='school_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=255)),
                ('url_address', models.URLField()),
                ('address', models.TextField()),
                ('postal_code', models.CharField(max_length=10)),
                ('telephone_no', models.CharField(max_length=20)),
                ('telephone_no_2', models.CharField(blank=True, max_length=20, null=True)),
                ('fax_no', models.CharField(blank=True, max_length=20, null=True)),
                ('fax_no_2', models.CharField(blank=True, max_length=20, null=True)),
                ('email_address', models.EmailField(max_length=254)),
                ('mrt_desc', models.TextField(blank=True, null=True)),
                ('bus_desc', models.TextField(blank=True, null=True)),
                ('principal_name', models.CharField(max_length=255)),
                ('first_vp_name', models.CharField(blank=True, max_length=255, null=True)),
                ('second_vp_name', models.CharField(blank=True, max_length=255, null=True)),
                ('third_vp_name', models.CharField(blank=True, max_length=255, null=True)),
                ('fourth_vp_name', models.CharField(blank=True, max_length=255, null=True)),
                ('fifth_vp_name', models.CharField(blank=True, max_length=255, null=True)),
                ('sixth_vp_name', models.CharField(blank=True, max_length=255, null=True)),
                ('dgp_code', models.CharField(max_length=255)),
                ('zone_code', models.CharField(max_length=255)),
                ('type_code', models.CharField(max_length=255)),
                ('nature_code', models.CharField(max_length=255)),
                ('session_code', models.CharField(max_length=255)),
                ('mainlevel_code', models.CharField(max_length=255)),
                ('sap_ind', models.CharField(max_length=255)),
                ('autonomous_ind', models.CharField(max_length=255)),
                ('gifted_ind', models.CharField(max_length=255)),
                ('ip_ind', models.CharField(max_length=255)),
                ('mothertongue1_code', models.CharField(max_length=255)),
                ('mothertongue2_code', models.CharField(blank=True, max_length=255, null=True)),
                ('mothertongue3_code', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
