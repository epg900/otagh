from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,Http404
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import format_html
from .forms import SignupForm,Rsettingform,Tpass
from .models import Rsetting,Ruser,Pass,PassType,StateType
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import pandas as pd
#import os,shutil,threading,random,string,requests
#import os,shutil,pyotp,threading,cryptocompare,random,string,pyqrcode
#from pytube import YouTube
#from datetime import datetime
#from django.contrib.auth.models import User,Permission
####################################################################
def index(request):
	try:
	    return render (request,'ou.html')
	except:
		raise Http404("Not Found")
####################################################################
def admin(request):
	try:
	    return render (request,'bt.html')
	except:
		raise Http404("Not Found")
####################################################################
def login_form(request):
	return render (request,'login.html')
####################################################################
def logout_form(request):
	logout(request)
	return redirect ('/')
####################################################################
def changePass(request):
	if not request.user.is_authenticated:
		return render (request,'login.html' )
	pass1=request.POST['pass1']
	request.user.set_password(pass1)
	request.user.save()
	#logout(request)
	#return render (request,'login.html')
	return HttpResponse("True", content_type='text/plain')
####################################################################
def logauth(request):
    try:
        if request.method == 'POST':
            #otp_chk=pyotp.TOTP('H4ZT2CIHQM5XO2VUSZPHWTBHMNQBDY3B')
            username=request.POST['username']
            password=request.POST['password']
            #if username=='admin':
            #    if otpcode!=otp_chk.now():
            #        return redirect ('/')
            user = authenticate(request, username=username, password=password)
            if user is not None :
                if username == 'admin' :
                   login(request , user)
                   return redirect ('/admin')
                else:
                   login(request , user)
                   lst=[[1,'a','aa','ac',0],[2,'b','aa','ac',0],[3,'c','aa','ac',1],[4,'d','aa','ac',3],[5,'e','aa','ac',1]]
                   df = pd.DataFrame(lst, columns =['id', 'title', 'link','clas','parent'])
                   return render (request,'ou.html',{'temp' : df})
            else:
                return redirect ('/')
    except:
        return redirect ('/')
    return redirect ('/')

####################################################################
def changepass(request):
    if request.user.username == "admin":
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('/admin')
            else:
                messages.error(request, '')
        else:
            form = PasswordChangeForm(request.user)
    return render(request, 'bt.html', {'form': form , 'var1' : 7 })
####################################################################
def emailme(request):
    send_mail(subject='', message=str(''),  from_email=settings.EMAIL_HOST_USER,   recipient_list=['epg900@gmail.com'])
    return HttpResponse("Email Sent")
####################################################################
def signup(request):
    if not request.user.is_authenticated:
        return redirect ('/')
    try:
        if request.user.username == "admin":
            if request.method == 'POST':
                    form = SignupForm(request.POST)
                    if form.is_valid():
                        form.save()
                        return render(request, 'bt.html', {'bodytitle':'کاربر ساخته شد','bodytext':'برای ساخت یک کاربر دیگر روی گزینه افزودن کلیک کنید', 'var1' : 5 })
            else:
                    form = SignupForm()
        return render(request, 'bt.html', {'form': form , 'var1' : 6 })
    except:
        return redirect ('/')

####################################################################
def setconf(request):
    if not request.user.is_authenticated:
        return redirect ('/')
    try:
        if request.user.username == "admin":
            ins1=Rsetting.objects.all().first()
            signer = Ruser.objects.get(personeli=ins1.signer)
            mali = Ruser.objects.get(personeli=ins1.mali)
            if request.method == 'POST':
                form = Rsettingform(request.POST, instance = ins1)
                if form.is_valid():
                    form.save()
                    return render(request, 'bt.html', {'var1' : 2 , 'bodytitle':'تنظیمات ذخیره شد'})
            else:
                form = Rsettingform(instance = ins1)
        return render(request, 'bt.html', {'form': form , 'var1' : 1 , 'signer' : signer.last_name , 'mali' : mali.last_name })
    except:
        return redirect ('/')

####################################################################
def listuser(request):
    if not request.user.is_authenticated:
        return redirect ('/')
    try:
        if request.user.username == "admin":
            userlist=Ruser.objects.exclude(username = "admin")
        return render(request, 'bt.html', {'userlist': userlist , 'var1' : 3 })
    except:
        return redirect ('/')
####################################################################
def useredit(request):
    if not request.user.is_authenticated:
        return redirect ('/')
    try:
        if request.user.username == "admin":
            if request.method == 'POST':
                idx = request.POST['idnum']
                ins1=Ruser.objects.get(id = idx)
                form =SignupForm(request.POST , instance = ins1)
                if form.is_valid():
                    form.save()
                    ins1.set_password(request.POST['password1'])
                    ins1.save()
                    #update_session_auth_hash(request, user)  # Important!
                    #messages.success(request, 'Your password was successfully updated!')
                    return redirect('/admin')
            else:
                idx = request.GET['id']
                ins1=Ruser.objects.get(id = idx)
                form =SignupForm(instance = ins1)
                return render(request, 'bt.html', {'form': form , 'var1' : 4 ,'idx' : idx })
        return redirect('/')
    except:
        return redirect ('/')
####################################################################
def addpass(request):
    if not request.user.is_authenticated:
        return redirect ('/')
    try:
        if request.method == 'POST':
                form = Tpass(request.POST,initial={'pass_type':1,})
                #form.fields['pass_type'].widget.attrs['readonly'] = True
                if form.is_valid():
                    instance=form.save(commit=False)
                    instance.user=request.user
                    instance.pass_type=PassType.objects.get(id = 1)
                    instance.save()
                    #form.save(commit=False)
                    #form.user=request.user
                    #form.save()
                    return render(request, 'ou.html', {'bodytitle':'افزوده شد','bodytext':'', 'var1' : 2 })
        else:
                form = Tpass(initial={'pass_type':1,})
        return render(request, 'ou.html', {'form': form , 'var1' : 1 })
    except:
        return redirect ('/')
####################################################################
def listpass(request):
    if not request.user.is_authenticated:
        return redirect ('/')
    try:
        passlist=Pass.objects.all()
        return render(request, 'ou.html', {'passlist': passlist , 'var1' : 3 })
    except:
        return redirect ('/')
####################################################################
def passtest(request):
    if not request.user.is_authenticated:
        return redirect ('/')
    if request.user.username == "h.tizhoosh":
        if request.method == 'GET' and request.GET.get("id") is not None and request.GET.get("ok") is not None:
                idx = request.GET['id']
                okn = request.GET['ok']
                #return HttpResponse(idx + " " + okn)
                if okn == '1' :
                    ins1=Pass.objects.get(id = idx)
                    ins1.state=StateType.objects.get(id = 1)
                    ins1.save()
                if okn == '2' :
                    ins1=Pass.objects.get(id = idx)
                    ins1.state=StateType.objects.get(id = 2)
                    ins1.save()
        passlist = Pass.objects.all()
        return render(request, 'ou.html',{'passlist' : passlist , 'var1' : 8 })
    return redirect ('/')


####################################################################
def test(request):

    html_text=format_html("<H1>{}</H1>","<i>test<i>")
    return HttpResponse(html_text)

'''

if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'index.html', {'form': form})
        else:
            form = ImageForm()
        context = {'bodytitle':'خوش آمدید','bodytext':'Benvenuto','form': form}
        return render(request, 'index.html', context)

disp=Image.objects.all()
    if request.method == 'POST':
        post1=request.POST['imgid']
        pic=Image.objects.filter(pk=int(post1))
        pic1=os.path.join(settings.BASE_DIR,'app1')
        pic11=pic[0].image.url
        pic2=pic1 + '/' + pic11
        if os.path.isfile('/home/epg900/site1/app1/static/tmp2.jpg'):
                os.remove('/home/epg900/site1/app1/static/tmp2.jpg')
        if os.path.isfile(pic2):
            pic3=os.path.join(settings.BASE_DIR, 'app1/static')
            pic4=os.path.join(pic3,'tmp2.jpg')
            shutil.copy(pic2, pic4)
        return render(request,'disp.html', {'disp':disp ,'pic':post1})


        url = request.GET['url']
        response = requests.get(url, stream=True, headers={'user-agent': request.headers.get('user-agent')})
        return StreamingHttpResponse(response.raw,content_type=response.headers.get('content-type'),status=response.status_code,reason=response.reason)

python3.8 -m pip install cryptocompare     <<    Its Only  Work on Pythonanywhere
epgccp@gmail.com    cc#@1234
user1_code='H4ZT2CIHQM5XO2VUSZPHWTBHMNQBDY3B'
user1=pyotp.random_base32()
totp=pyotp.TOTP(user1)
url1=totp.provisioning_uri(name='user1',issuer_name='Django_test')
qr=pyqrcode.create(url1)
qr.svg('qrcode.svg',quiet_zone=1)
print(qr.terminal(quiet_zone=1))

u = User.objects.get(username = 'user1')
    u.delete()
    u=user1.has_perm('app1.Admin1')

    from django.contrib.auth.models import Permission,User
    permission = Permission.objects.get(codename='Admin1')
    user = User.objects.get(username='admin')
    user.user_permissions.add(permission)

    user.save()
'''
####################################################################