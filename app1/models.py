from django.db import models
from django.contrib.auth.models import AbstractUser

class Rsetting (models.Model):
  cur_year = models.IntegerField(default=1400,verbose_name='سال جاری')
  start_time = models.IntegerField(default=7,verbose_name='ساعت شروع فعالیت سازمان')
  end_time = models.IntegerField(default=14,verbose_name='ساعت پایان فعالیت سازمان')
  lim_my = models.IntegerField(default=31,verbose_name='محدودیت مرخصی در سال(به روز)')
  lim_mm = models.IntegerField(default=15,verbose_name='محدودیت مرخصی در ماه(به روز)')
  lim_md = models.IntegerField(default=2,verbose_name='محدودیت مرخصی در روز(به ساعت)')
  work_time = models.IntegerField(default=7,verbose_name='ساعت کاری در روز')
  rel_work = models.FloatField(default=6.5,verbose_name='نسبت روز کاری به مرخصی ساعتی')
  signer = models.IntegerField(default=10001,verbose_name='امضاء کننده')
  baygan = models.IntegerField(default=10001,verbose_name='شماره پرسنلی مسئول بایگانی')
  mali = models.IntegerField(default=10001,verbose_name='شماره پرسنلی مدیر امور مالی')
  hozoor = models.IntegerField(default=10001,verbose_name='شماره پرسنلی مسئول حضور و غیاب')
  amoozesh = models.IntegerField(default=10001,verbose_name='شماره پرسنلی مسئول آموزش')
  ranande = models.IntegerField(default=10001,verbose_name='شماره پرسنلی راننده')
  negah1 = models.IntegerField(default=10001,verbose_name='شماره پرسنلی نگهبان 1')
  negah2 = models.IntegerField(default=10001,verbose_name='شماره پرسنلی نگهبان 1')
  negah3 = models.IntegerField(default=10001,verbose_name='شماره پرسنلی نگهبان 1')
  nagah_ezaf = models.IntegerField(default=2,verbose_name='تعداد روزهای اضافه کار ثابت نگهبانان')
  mamooriat =  models.IntegerField(default=10000000,verbose_name='مبلغ هر روز ماموریت به ریال')
  mablagh1 =  models.IntegerField(default=10000000,verbose_name='مبلغ هر روز ماموریت راننده به ریال')
  mablagh2 =  models.IntegerField(default=10000000,verbose_name='مبلغ ثابت براي راننده اول و دوم به ریال')
  dastzarb = models.FloatField(default=1.4,verbose_name=' دستمزد ماهيانه ضربدر')
  dasttaghsim = models.FloatField(default=7.33,verbose_name='تقسيم بر ')
  kharidm = models.IntegerField(default=2,verbose_name='تعداد روز مرخصي قابل خريد')


class Ruser(AbstractUser):
    personeli = models.IntegerField(null=True,unique=True)
    password = models.CharField(max_length=100)
    dastmozd = models.IntegerField(default=7000000)
    mobile = models.CharField(max_length=11,default='')
    def __str__(self):
        return self.username

class StateType(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class PassType(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Pass(models.Model):
    user = models.ForeignKey(Ruser , on_delete=models.CASCADE ,verbose_name='نام کاربری')
    req_date = models.CharField(max_length=10 ,verbose_name='تاریخ  ثبت درخواست')
    pass_type = models.ForeignKey(PassType , on_delete=models.CASCADE ,verbose_name='نوع مرخصی ' )
    start_date = models.CharField(max_length=10 ,verbose_name='تاریخ شروع')
    end_date = models.CharField(max_length=10 ,verbose_name='تاریخ پایان')
    start_time = models.CharField(max_length=10 ,verbose_name='ساعت شروع')
    end_time = models.CharField(max_length=10 ,verbose_name='ساعت پایان')
    reason = models.CharField(max_length=10 ,verbose_name='علت درخواست')
    sick_paper = models.ImageField(upload_to='images', blank=True, null=True ,verbose_name='گواهی درخواست')
    state = models.ForeignKey(StateType , default=3 , on_delete=models.CASCADE ,verbose_name='وضعیت درخواست')
    signer = models.CharField(max_length=10 , default='10001' ,verbose_name='تایید کننده' )
    def __str__(self):
        return self.req_date




