from django.conf.urls import url,include
from . import views 

urlpatterns = [
    url('sample',views.sampleFun,name='sample'),
    url('index',views.indexFun,name='index'),
    url('home' ,views.homeFun,name = 'home'),
    url('test' ,views.testFun,name = 'test')

]