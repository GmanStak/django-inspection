from django.db import models

# Create your models here.
class HostDevice(models.Model):
    # id = models.AutoField(primary_key=True)
    device = models.CharField(max_length=32)

class HostInsGroup(models.Model):
    # id = models.AutoField(primary_key=True)
    InsGroupName = models.CharField(max_length=100)


class HostAdd(models.Model):
    hostip = models.CharField(max_length=100, verbose_name='设备IP')
    hostname = models.CharField(max_length=200, verbose_name='设备名称')
    hostusername = models.CharField(max_length=100, verbose_name='登陆用户')
    hostpassword = models.CharField(max_length=200, verbose_name='登陆密码')
    hostport = models.CharField(max_length=100, verbose_name='设备连接端口', default=22)
    hostdevice = models.CharField(max_length=200, verbose_name='设备类型')
    hostinsGroup = models.CharField(max_length=100, verbose_name='巡检分组')
    # hostdevice = models.ForeignKey("HostDevice", on_delete=models.CASCADE)
    # hostinsGroup = models.ForeignKey("HostInsGroup", on_delete=models.CASCADE)
    # hostaddstatus = models.BooleanField(default=True)
    class Meta():
        verbose_name = "设备信息表"
        verbose_name_plural = "设备信息表"
