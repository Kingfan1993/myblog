from django.db import models

# Create your models here.


from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(models.Model):
    # 用户名
    name = models.CharField(max_length=32)
    # 密码
    pwd = models.CharField(max_length=32)
    # 头像
    avatar = models.FileField(upload_to="avatars/", default="avatars/default.png")  # 头像
    # 手机号
    phone = models.CharField(max_length=11,null=True,blank=True)
    # 邮箱号
    email = models.EmailField(null=True,blank=True)
    # 自我描述
    desc = models.CharField(max_length=32,blank=True,null=True)
    # QQ号
    qq = models.CharField(max_length=32,blank=True,null=True)
    class Meta:
        verbose_name='用户'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

class Article(models.Model):
    # 标题
    title = models.CharField(max_length=32)
    # 描叙
    desc = models.CharField(max_length=255,null=True,blank=True)
    # 头像
    avatar = models.FileField(upload_to="articleimg/", default="articleimg/default.png")  # 头像
    # 内容
    content = models.TextField(null=True,blank=True)
    # 创建时间
    create_time = models.DateField(null=True,blank=True)
    # 标签
    tags = models.ManyToManyField(to='Tag',blank=True,null=True)
    # 分类
    categorys = models.ManyToManyField(to='Category',blank=True,null=True)
    class Meta:
        verbose_name='文章'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=32)
    class Meta:
        verbose_name='标签'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title


class Category(models.Model):
    title =models.CharField(max_length=32)
    class Meta:
        verbose_name='分类'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title









