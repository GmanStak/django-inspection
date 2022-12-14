# Generated by Django 4.0.8 on 2022-11-03 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostip', models.CharField(max_length=100, verbose_name='设备IP')),
                ('hostname', models.CharField(max_length=200, verbose_name='设备名称')),
                ('hostusername', models.CharField(max_length=100, verbose_name='登陆用户')),
                ('hostpassword', models.CharField(max_length=200, verbose_name='登陆密码')),
                ('hostport', models.CharField(default=22, max_length=100, verbose_name='设备连接端口')),
                ('hostdevice', models.CharField(max_length=200, verbose_name='设备类型')),
                ('hostinsGroup', models.CharField(max_length=100, verbose_name='巡检分组')),
            ],
            options={
                'verbose_name': '设备信息表',
                'verbose_name_plural': '设备信息表',
            },
        ),
        migrations.CreateModel(
            name='HostDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='HostInsGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InsGroupName', models.CharField(max_length=100)),
            ],
        ),
    ]
