from pelican.settings import DEFAULT_CONFIG
from pelican.readers import RstReader
from pelican.readers import HTMLParser
from pelican.readers import BaseReader

class CustomReader(BaseReader):
    enabled = True
    file_extensions = ['htmlx']
    
    def read(self, source_path):
        # Custom parsing logic here
        with open(source_path,encoding="utf-8") as f:
            content = f.read()
        return content, None
 
# In settings
READERS = {'custom': CustomReader}

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
]

# Social widget
SOCIAL = (
    ('Facebook', 'https://forums.lanik.us/'),
    ('Youtube', 'https://forums.lanik.us/'),
    ('LinkedIn', 'https://forums.lanik.us/'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Themes
HEADER_COVER = "theme/images/gallery_image (16).jpg"
PAGE_HEADER_COLOR = "#7B5A48"

# Favicon
FAVICON = 'favicon.png'

STATIC_PATHS = ['../static/images','../static/js']
EXTRA_PATH_METADATA = {
    '../static/images/icons/favicon.png': {'path': 'favicon.png'},
}

PAGE_ORDER_BY = "page-order"

ARTICLE_EXCLUDES = ["articles_excluded"]

config = DEFAULT_CONFIG.copy()

customreader = CustomReader(config)
INTRO_CONTENT,_ = customreader.read("content/articles_excluded/intro.htmlx")