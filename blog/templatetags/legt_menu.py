

from django import template


register = template.Library()
from blog.models import *

@register.inclusion_tag('left_html.html')
def left_tage():
    user = User.objects.get(id=1)
    category_list = Category.objects.all()
    article_list = Article.objects.all().order_by('-create_time')
    tag_list = Tag.objects.all()
    article_recent = article_list[0:5]
    return locals()
