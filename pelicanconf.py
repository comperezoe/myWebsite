from pelican.settings import DEFAULT_CONFIG
from pelican.readers import RstReader
from pelican.readers import HTMLParser

AUTHOR = 'Zoé Compère'
SITENAME = 'Zoé Compère'
SITESUBTITLE = "Flutist"
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Brussels'

DEFAULT_LANG = 'en'

THEME = "."
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = [
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
]

# Social widget
SOCIAL = [
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
]

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Themes
HEADER_COLOR = '#7B5A48'

# Favicon
FAVICON = 'favicon.png'

STATIC_PATHS = ['../static/images']
EXTRA_PATH_METADATA = {
    '../static/images/icons/favicon.png': {'path': 'favicon.png'}
}

ARTICLE_EXCLUDES = ["articles_excluded"]

config = DEFAULT_CONFIG.copy()

INTRO_CONTENT = "This is my website. Sorry for the mess"