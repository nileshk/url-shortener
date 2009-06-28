url-shortener
=============

This is URL shortening application using the Django framework

The shortened URLs use the base 62 value of ids of the model they are
stored in.  A count of how many times the URLs are used is kept.  The
main page shows the 10 most recent and 10 most popular URLs.

Prerequisites
=============

Download Blueprint from: http://www.blueprintcss.org/
Copy the "blueprint" folder into static/css/ (which you may need to create)

Note that in a production installation, you'll want to have your web
server serve the "static" folder instead of letting Django serve it.

Settings
========

The following values need to be set in settings.py:

SITE_NAME
    The name of the site (e.g. 'urlshorteningsite.com')

SITE_BASE_URL
    The base URL of the site.  This can be based on the SITE_NAME:
    SITE_BASE_URL = 'http://' + SITE_NAME + '/'

REQUIRE_LOGIN
    Set REQUIRE_LOGIN to True if you want to require that a user be
    logged in to be able to submit a URL to be shortened.  Set it
    to False if you do not want to require login to submit a URL.
