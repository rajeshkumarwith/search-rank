from django.contrib.sitemaps import Sitemap
from .models import *
from django.urls import reverse

class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Profile.objects.all()

    def lastmod(self, obj):
        return obj.article_published
        
    def location(self,obj):
        return '/blog/%s' % (obj.article_slug)



class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['main:homepage_view', 'main:contact_view']

    def location(self, item):
        return reverse(item)