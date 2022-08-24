from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login_form),
	path('logout/', views.logout_form),
	path('changePass/', views.changePass , name='changePass'),
	path('changepass/', views.changepass ),
    path('logauth/', views.logauth),
    path('upload/', views.image_upload_view),
    path('display/', views.display),
    path('email/', views.emailme),
    path('bt/', views.bt),
    path('signup/', views.signup),
    path('setconf/', views.setconf),
    path('edituser/', views.edituser),
    path('usereditform/', views.usereditform),
    path('useredit/', views.useredit),
]

