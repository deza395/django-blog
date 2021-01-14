

from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('tecnologia/', tecnologia, name='tecnologia'),
    path('tips/', tips, name='tips'),
    path('python/', python, name='python'),
    path('ambiente/', ambiente, name='ambiente'),
    path('<slug:slug>/', detailsPost, name='detalle_post'),

]
