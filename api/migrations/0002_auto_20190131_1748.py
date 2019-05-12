# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-01-31 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailaddressinfo',
            name='parent',
        ),
        migrations.AddField(
            model_name='addressinfo',
            name='code',
            field=models.IntegerField(blank=True, null=True, verbose_name='城乡分类代码'),
        ),
        migrations.AddField(
            model_name='addressinfo',
            name='ddd',
            field=models.IntegerField(blank=True, null=True, verbose_name='长途区号'),
        ),
        migrations.AddField(
            model_name='addressinfo',
            name='post_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='邮政编码'),
        ),
        migrations.AlterField(
            model_name='addressinfo',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, verbose_name='统计用区划代码'),
        ),
        migrations.AlterField(
            model_name='chineseuniversity',
            name='cid',
            field=models.IntegerField(verbose_name='city_id'),
        ),
        migrations.AlterField(
            model_name='chineseuniversity',
            name='sid',
            field=models.IntegerField(verbose_name='school_id'),
        ),
        migrations.AlterField(
            model_name='universitydepartment',
            name='did',
            field=models.IntegerField(verbose_name='department_id'),
        ),
        migrations.AlterField(
            model_name='universitydepartment',
            name='sid',
            field=models.IntegerField(verbose_name='school_id'),
        ),
        migrations.DeleteModel(
            name='DetailAddressInfo',
        ),
    ]