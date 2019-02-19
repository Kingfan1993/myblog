from django.shortcuts import render,HttpResponse
from django import views
from blog.models import *
# Create your views here.
from utils.mypage import MyPage
class Index(views.View):
    def get(self,request):
        user_obj = UserInfo.objects.filter(id=1)[0]
        category_list = user_obj.blog.category_set.all()
        article_list = Article.objects.all().order_by('-create_time')
        tag_list = user_obj.blog.tag_set.all()
        article_recent = article_list[0:5]

        data_amount = article_list.count()
        page_num = request.GET.get("page", 1)
        page_obj = MyPage(page_num, data_amount, per_page_data=4, url_prefix='index')
        # 按照分页的设置对总数据进行切片
        article_list = article_list[page_obj.start:page_obj.end]
        page_html = page_obj.ret_html()
        return render(request,'index.html',locals())

class QueryView(views.View):
    def get(self,request,condition,query):

        condition_list = ['category', 'tag']
        if condition not in ['category','tag']:
            return HttpResponse(404)
        article_list = []
        if condition == condition_list[0]:
            article_list = Article.objects.filter(category__title=query)
        elif condition == condition_list[1]:
            article_list = Article.objects.filter(tags__title=query)
        elif not article_list:
            article_list =Article.objects.all()
        else:
            article_list = Article.objects.all()

        url = request.path.strip('/')
        data_amount = article_list.count()
        page_num = request.GET.get("page", 1)
        page_obj = MyPage(page_num, data_amount, per_page_data=4, url_prefix=url)
        # 按照分页的设置对总数据进行切片
        article_list = article_list[page_obj.start:page_obj.end]
        page_html = page_obj.ret_html()

        user_obj = UserInfo.objects.filter(id=1)[0]
        category_list = user_obj.blog.category_set.all()
        tag_list = user_obj.blog.tag_set.all()
        article_recent = article_list[0:5]
        return render(request,'query.html',locals())


class ArticleContent(views.View):
    def get(self,request,id):
        article_list = Article.objects.all()
        user_obj = UserInfo.objects.filter(id=1)[0]
        category_list = user_obj.blog.category_set.all()
        tag_list = user_obj.blog.tag_set.all()
        article_recent = article_list[0:5]

        article = Article.objects.filter(id=id).first()




        return render(request,'ariticlecontent.html',locals())