from django.db import models


# Create your models here.

class Memu(models.Model):
    '''
    菜单表
    '''
    title = models.CharField(verbose_name='标题', max_length=12)
    icon = models.CharField(verbose_name='图标', max_length=12)


class Permissions(models.Model):
    '''
    权限表
    '''
    url = models.CharField(verbose_name='URL', max_length=32)
    title = models.CharField(verbose_name='名称', max_length=12)
    name = models.CharField(verbose_name='别名', max_length=12, unique=True)

    memu = models.ForeignKey(verbose_name='管理菜单', to='Memu', to_field='id', null=True, blank=True)
    parent = models.ForeignKey(verbose_name='父菜单', to='Permissions', null=True, blank=True)


class Role(models.Model):
    name = models.CharField(verbose_name='名称', max_length=12)
    permissions = models.ManyToManyField(verbose_name='关联权限', to='Permissions')


class User(models.Model):
    name = models.CharField(verbose_name='用户名', max_length=12)
    password = models.CharField(verbose_name='密码', max_length=64)

    roles = models.ManyToManyField(verbose_name='关联角色', to='Role')



