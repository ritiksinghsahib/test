from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

 
class ViewSitemap(Sitemap):

    def items(self):
        return['Home','Event','services','Regularupdate']

    def location(self,item):
        return reverse(item)

    