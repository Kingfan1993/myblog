from django.shortcuts import render,HttpResponse
from django import views
from blog.models import *
# Create your views here.
from utils.mypage import MyPage
from django.http import JsonResponse
class Index(views.View):
    def get(self,request):
        article_list = Article.objects.all().order_by('-create_time')
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
        return render(request,'query.html',locals())


class ArticleContent(views.View):
    def get(self,request,id):
        article = Article.objects.filter(id=id).first()
        return render(request,'ariticlecontent.html',locals())


def test(request):
    if request.method=='POST':
        print(request.POST,request.GET)
    return render(request,'editor.html')

from myblog import settings
import os
def upload(request):

    img_obj = request.FILES.get('imgFile')
    base_path = os.path.join(settings.MEDIA_ROOT,'content_img')
    img_list = os.listdir(base_path)
    if img_obj.name in img_list:
        res = {'url':'media/content_img/{}'.format(img_obj.name),'error':1,'message':'请更改文件名'}
        return JsonResponse(res)
    path =os.path.join(base_path,img_obj.name)
    with open(path,'wb') as f:
        for line in img_obj:
            f.write(line)
    res = {'url': '/media/content_img/{}'.format(img_obj.name), 'error': 0}
    return JsonResponse(res)