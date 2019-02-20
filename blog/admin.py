from django.contrib import admin

# Register your models here.
from blog.models import *





admin.site.register(User)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title',)

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            '/static/kindeditor/kindeditor-all.js',
            '/static/kindeditor/lang/zh-CN.js',
            '/static/kindeditor/config.js',
        )

admin.site.register(Category)  # 文章分类
admin.site.register(Tag)  # 文章标签
