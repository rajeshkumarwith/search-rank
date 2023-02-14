from django.contrib.sitemaps.views import sitemap
from .sitemaps import ArticleSitemap,StaticSitemap
from django.urls import path
from app import views
from .views import *
from app import search
from .search import *
app_name = "app"

sitemaps = {
    'blog':ArticleSitemap,
    'static':StaticSitemap 
}

urlpatterns = [
    # path("", views.homepage, name="homepage"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('searchdata',searchapi,name='search'),
    path('search',search_api, name='search'),
    path('add',add,name='add'),
    path('index',datasearch,name='data'),
    path('show',datashow,name='show'),
    path('connect',query,name='connect'),
    path('dataquery',dataquery,name='dataquery')

]



