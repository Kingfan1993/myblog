from django.contrib import admin

# Register your models here.
from blog.models import *


admin.site.register(UserInfo)
admin.site.register(Article)
admin.site.register(Article2Tag)  # 文章-标签
admin.site.register(Category)  # 文章分类
admin.site.register(Tag)  # 文章标签
admin.site.register(Comment)  # 文章评论
admin.site.register(Blog)  # 博客站点
admin.site.register(ArticleUpDown)  # 点赞
admin.site.register(ArticleDetail)  # 文章详情