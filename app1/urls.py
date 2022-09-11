from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', views.index),
    path('login/', views.login_form),
	path('logout/', views.logout_form),
	path('changePass/', views.changePass ),
	path('changepass/', views.changepass ),
    path('logauth/', views.logauth),
    path('email/', views.emailme),
    path('signup/', views.signup),
    path('setconf/', views.setconf),
    path('edituser/', views.edituser),
    path('usereditform/', views.usereditform),
    path('useredit/', views.useredit),
    path('test/', views.test),
    path('addpass/', views.addpass),
    path('listpass/', views.listpass),
    path('passtest/', views.passtest),
]

