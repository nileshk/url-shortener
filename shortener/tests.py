"""
Tests for views
"""

__test__ = {"doctest": """

# Initialize by deleting all Link objects
>>> from models import Link
>>> Link.objects.all().delete()

>>> from django.test import Client
>>> client = Client()

# Index page
>>> r = client.get('/')
>>> r.status_code # /
200
>>> r.template[0].name
'shortener/index.html'

# Turn off logged-in requirement and set base URL
>>> from django.conf import settings
>>> settings.REQUIRE_LOGIN = False
>>> settings.SITE_BASE_URL = 'http://uu4.us/'

# Empty submission should forward to error page
>>> r = client.get('/submit/')
>>> r.status_code # /submit/
200
>>> r.template[0].name # /submit/
'shortener/submit_failed.html'

# Submit a URL
>>> url = 'http://www.google.com/'
>>> r = client.get('/submit/', {'u': url})
>>> r.status_code # /submit/u?=http%3A%2F%2Fwww.google.com%2F
200
>>> r.template[0].name
'shortener/submit_success.html'
>>> link = r.context[0]['link']
>>> link.to_base62()
'B'
>>> link.short_url()
'http://uu4.us/B'
>>> link_from_db = Link.objects.get(url = url)
>>> base62 = link_from_db.to_base62()
>>> base62
'B'
>>> link_from_db.usage_count
0

# Short URL for previously submitted URL
>>> r = client.get('/' + base62)
>>> r.status_code # '/' + base62
301
>>> r['Location']
'http://www.google.com/'

# Invalid URL should get a 404
>>> r = client.get('/INVALID')
>>> r.status_code # /INVALID
404

# Index now shows link in recent_links / most_popular_links
>>> r = client.get('/')
>>> r.status_code # /
200
>>> r.template[0].name
'shortener/index.html'
>>> context = r.context[0]
>>> len(context['recent_links'])
1
>>> len(context['most_popular_links'])
1

# Get info on Link
>>> r = client.get('/info/' + base62)
>>> r.status_code # info
200
>>> r.template[0].name
'shortener/link_info.html'
>>> link = r.context[0]['link']
>>> link.url
u'http://www.google.com/'
>>> link.usage_count # Usage count should be 1 now
1

"""}

