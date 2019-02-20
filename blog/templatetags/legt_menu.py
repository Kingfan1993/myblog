

from django import template


register = template.Library()
from blog.models import *

@register.inclusion_tag('left_html.html')
def left_tage():
    user_obj = UserInfo.objects.filter(id=1)[0]
    category_list = user_obj.blog.category_set.all()
    article_list = Article.objects.all().order_by('-create_time')
    tag_list = user_obj.blog.tag_set.all()
    article_recent = article_list[0:5]
    return locals()
