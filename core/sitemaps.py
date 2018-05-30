from django.contrib.sitemaps import Sitemap
from core.models import Event
from django.urls import reverse


class EventSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1

    def items(self):
        return Event.objects.all()

    def lastmod(self, obj):
         return obj.modified