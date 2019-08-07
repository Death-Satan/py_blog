from django.shortcuts import render
from .models import website,Category,PV,Article,abodu as bodu
def Index(request):
    context = {}
    uid = request.GET.get('id', default='N')
    print(uid)
    context['title'] = website.objects.get(id=1).value
    context['description'] = website.objects.get(id=2).value
    context['signature'] = website.objects.get(id=4).value
    context['category'] = Category.objects.all()
    context['web_to'] = website.objects.get(id=5).value
    context['pv'] = PV.objects.get(id=1)
    if uid == 'N':
        context['article'] = Article.objects.all()
    else:
        context['article'] = Article.objects.filter(category_id=uid)
    print(context['article'])
    return  render(request,'index.html',context)

def article_data(request):
    context = {}
    context['signature'] = website.objects.get(id=4).value
    context['description'] = website.objects.get(id=2).value
    id = request.GET.get('id', default='N')
    if id == 'N':
        http = urlsplit(request.build_absolute_uri(None)).scheme
        host = request.META['HTTP_HOST']
        # 获取当前域名
        context['domain'] =  http + '://' + host + '/' + shorturl1 + '/'
        return render(request,'404.html',context)
    else:
        context['website'] = Article.objects.get(id=id)
    return render(request,'data.html',context)
def abodu(request):
    context = {}
    context['body'] = bodu.objects.get(id=1).body ##获取内容
    context['signature'] = website.objects.get(id=4).value #获取站点签名
    context['description'] = website.objects.get(id=2).value #获取内容摘要
    return render(request,'about.html',context) ##渲染模板