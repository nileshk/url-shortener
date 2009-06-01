import datetime

from django.db import models
from django.conf import settings
#from django.contrib.auth.models import User
from django import forms

from urlweb.shortener.baseconv import base62

class Link(models.Model):
    """
    Model that represents a shortened URL

    # Initialize by deleting all Link objects
    >>> Link.objects.all().delete()
    
    # Create some Link objects
    >>> link1 = Link.objects.create(url="http://www.google.com/")
    >>> link2 = Link.objects.create(url="http://www.nileshk.com/")

    # Get base 62 representation of id
    >>> link1.to_base62()
    'B'
    >>> link2.to_base62()
    'C'
    
    # Set SITE_BASE_URL to something specific
    >>> settings.SITE_BASE_URL = 'http://uu4.us/'

    # Get short URL's
    >>> link1.short_url()
    'http://uu4.us/B'
    >>> link2.short_url()
    'http://uu4.us/C'

    # Test usage_count
    >>> link1.usage_count
    0
    >>> link1.usage_count += 1
    >>> link1.usage_count
    1

    """
    url = models.URLField(verify_exists=True, unique=True)
    date_submitted = models.DateTimeField(default=datetime.datetime.now())
    usage_count = models.IntegerField(default=0)

    def to_base62(self):
        return base62.from_decimal(self.id)

    def short_url(self):
        return settings.SITE_BASE_URL + self.to_base62()
    
    def __unicode__(self):
        return self.to_base62() + ' : ' + self.url

class LinkSubmitForm(forms.Form):
    u = forms.URLField(verify_exists=True,
                       label='URL to be shortened:',
                       )
