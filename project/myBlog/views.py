from django.shortcuts import render
from django.http import HttpResponse
from .models import Sender
from django.shortcuts import redirect
# Create your views here.
def blank(request):

    return redirect('/index/id=1/')
from django.core.paginator import Paginator
def index(request,num):
    reusername = request.session.get('name', '游客')

    articles = Sender.objects.all()
    for i in articles:
        if i.gender:
            i.gender = '男'
        else:
            i.gender = '女'
    paginator = Paginator(articles, 5)
    pageid = paginator.page(num)
    return render(request,'myBlog/index.html',{'people':pageid,'username':reusername})
def sendartical(request):
    title = request.session.get('title')
    name = request.session.get('name')
    return render(request, 'myBlog/sendartical.html',{'sname':name,'stitle':title})
def browseartical(request):
    artical =Sender.objects.all()
    return render(request,'myBlog/browseartical.html',{'articals':artical})
def login(requset):
    str = ''
    msg = requset.session.get('msg',True)
    if msg == False:
        str ="验证码输入错误,请重新输入"
    # requset.session['verificode'].clear()
    return render(requset,'myBlog/login.html',{'msg':str})


def codetext(request):
    code1 = request.POST.get('code').upper()
    code2 = request.session['verificode'].upper()
    if code1 == code2:
        name = request.POST.get('name')
        ps = request.POST.get('ps')
        title = request.POST.get('title')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        isDelete = request.POST.get('isDelete')
        request.session['title'] = title
        request.session['name'] = name
        request.session['ps'] = ps
        request.session['age'] = age
        request.session['gender'] = gender
        request.session['isDelete'] = isDelete
        # print(age)

        return redirect('/index/id=1/')
    else:
        request.session['msg'] = False
        return redirect('/login/')







def loginsuccess(request):
    name = request.POST.get('name')
    ps = request.POST.get('ps')
    title = request.POST.get('title')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    isDelete = request.POST.get('isDelete')
    request.session['title'] = title
    request.session['name'] = name
    request.session['ps'] = ps
    request.session['age'] = age
    request.session['gender'] = gender
    request.session['isDelete'] = isDelete
    # print(age)

    return redirect('/index/id=1/')
from django.contrib.auth import logout
def quitlogin(request):
    logout(request)
    return redirect('/index/id=1/')
from .models import Sender
from django.utils import timezone
from datetime import *
def complete(request):
    name = request.session.get('name')
    ps = request.session.get('ps')
    age = request.session.get('age')
    gender = request.session.get('gender')
    title = request.session.get('title')
    contents = request.POST.get('contents')
    isDelete = request.session.get('isDelete')
    temp = Sender()
    temp.name = name
    temp.ps = ps
    if age == '':
        age=20
    temp.age = int(age)
    temp.gender = bool(gender)
    temp.title = title
    temp.contents = contents
    temp.isDelete = bool(isDelete)
    temp.lasttime = datetime.now()
    temp.save()
    return redirect('/index/id=1/')


def verifycode(request):
    #引入绘图模块
    from PIL import Image , ImageDraw ,ImageFont
    #引入随机数模块
    import random
    #定义变量,用于画面的背景色，宽，高
    bgcolor = (random.randrange(20,100),random.randrange(20,100),random.randrange(20,100))
    width=100
    height=50
    #创建画面对象
    im = Image.new('RGB',(width,height),bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0,100):
        xy = (random.randrange(0,width),random.randrange(0,height))
        fill = (random.randrange(0,255),255,random.randrange(0,255))
        draw.point(xy,fill=fill)
    #定义验证码的备选值
    str ='1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    #随机选取4个值作为验证码
    rand_str=''
    for i in range(0,4):
        rand_str += str[random.randrange(0,len(str))]
    #构造字体对象
    font = ImageFont.truetype(r'C:\Windows\Fonts\9PX3BUS(1).TTF',20)
    #构造字体颜色
    fontcolor1 = (255,random.randrange(0,255),random.randrange(0,255))
    fontcolor2 = (255,random.randrange(0,255),random.randrange(0,255))
    fontcolor3 = (255,random.randrange(0,255),random.randrange(0,255))
    fontcolor4 = (255,random.randrange(0,255),random.randrange(0,255))
    #绘制4个字
    draw.text((5,2),rand_str[0],font=font,fill=fontcolor1)
    draw.text((25,10),rand_str[1],font=font,fill=fontcolor2)
    draw.text((50,20),rand_str[2],font=font,fill=fontcolor3)
    draw.text((75,15),rand_str[3],font=font,fill=fontcolor4)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verificode'] = rand_str
    #内存文件操作
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf,'png')
    #将内存中的图片数据返回给客户端，MIME类型为鱼片png
    return HttpResponse(buf.getvalue(),'image/png')



def upimg(request):
    return render(request,'myBlog/upimg.html')
import os
from django.conf import settings
def upimgsuccess(request):
    if request.method == 'POST':
        f = request.FILES['file']
        filedir = os.path.join(settings.MEDIA_ROOT,f.name)
        with open(filedir,'wb') as fd:
            for info in f.chunks():
                fd.write(info)

        return HttpResponse('上传成功')

    else:
        return HttpResponse('上传失败')
import json
import requests
def call(request):
    question = request.POST.get('question')
    #调用图灵
    def get_html(url, data, header):
        res = requests.get(url, params=data, headers=header)
        html = res.text
        return html

    key = 'a84759e77e76488682597943080f3f98'
    url = 'http://www.tuling123.com/openapi/api'
    # req_info = input('我说: ')
    header = {'Content-type': 'text/html', 'charset': 'utf-8'}
    data = {'key': key, 'info': question}
    target = get_html(url, data, header)
    target = json.loads(target)
    # print('景炀侯：' + target['text'])
    return render(request,'myBlog/index.html',{'con':target['text']})


