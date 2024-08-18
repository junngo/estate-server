# Generated by Django 5.1 on 2024-08-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AptTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sgg_cd', models.CharField(max_length=5)),
                ('umd_cd', models.CharField(max_length=5)),
                ('land_cd', models.CharField(blank=True, max_length=1, null=True)),
                ('bonbun', models.CharField(blank=True, max_length=4, null=True)),
                ('bubun', models.CharField(blank=True, max_length=4, null=True)),
                ('road_nm', models.CharField(blank=True, max_length=100, null=True)),
                ('road_nm_sgg_cd', models.CharField(blank=True, max_length=5, null=True)),
                ('road_nm_cd', models.CharField(blank=True, max_length=7, null=True)),
                ('road_nm_seq', models.CharField(blank=True, max_length=2, null=True)),
                ('road_nmb_cd', models.CharField(blank=True, max_length=1, null=True)),
                ('road_nm_bonbun', models.CharField(blank=True, max_length=5, null=True)),
                ('road_nm_bubun', models.CharField(blank=True, max_length=5, null=True)),
                ('umd_nm', models.CharField(max_length=60)),
                ('apt_nm', models.CharField(max_length=100)),
                ('jibun', models.CharField(blank=True, max_length=20, null=True)),
                ('exclu_use_ar', models.DecimalField(blank=True, decimal_places=4, max_digits=22, null=True)),
                ('deal_year', models.IntegerField()),
                ('deal_month', models.IntegerField()),
                ('deal_day', models.IntegerField()),
                ('deal_amount', models.CharField(max_length=40)),
                ('floor', models.IntegerField(blank=True, null=True)),
                ('build_year', models.IntegerField(blank=True, null=True)),
                ('apt_seq', models.CharField(max_length=20)),
                ('cdeal_type', models.CharField(blank=True, max_length=1, null=True)),
                ('cdeal_day', models.CharField(blank=True, max_length=8, null=True)),
                ('dealing_gbn', models.CharField(blank=True, max_length=10, null=True)),
                ('estate_agent_sgg_nm', models.CharField(blank=True, max_length=3000, null=True)),
                ('rgst_date', models.CharField(blank=True, max_length=8, null=True)),
                ('apt_dong', models.CharField(blank=True, max_length=400, null=True)),
                ('sler_gbn', models.CharField(blank=True, max_length=100, null=True)),
                ('buyer_gbn', models.CharField(blank=True, max_length=100, null=True)),
                ('land_leasehold_gbn', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
    ]