# ** Pelican Configuration File Defaults ** 

# ** Metadata **

AUTHOR = 'Rob Teszka'
SITENAME = 'Robmagus\' Nerd Shit'
# SITESUBTITLE = ''
# The following line is specific to the monospace theme
DESCRIPTION = 'You are in a maze of twisty little passages, all alike.'
SITEURL = ""
TIMEZONE = 'America/Vancouver'
DEFAULT_LANG = 'en'
# LOCALE = 'C'
# DEFAULT_DATE = 'fs'
# DISQUS_SITENAME = "blog-namehere"
# DEFAULT_METADATA = {"key": "value"}
# FILENAME_METADATA = r'(?P<date>\\d{4}-\\d{2}-\\d{2}).*'
# PATH_METADATA = ''
# EXTRA_PATH_METADATA = {}

# PLUGINS = None

# ANALYTICS

# ** Site Display & Nav Settings ** 

# DEFAULT_ORPHANS = 0
# REVERSE_CATEGORY_ORDER = False
# NEWEST_FIRST_ARCHIVES = True
# ARTICLE_ORDER_BY = 'reversed-date'
# PAGE_ORDER_BY = 'basename'
# DISPLAY_PAGES_ON_MENU = True
# DEFAULT_DATE_FORMAT = '%a %d %B %Y'
# DATE_FORMATS = {}
# SUMMARY_MAX_LENGTH = 50
# SUMMARY_MAX_PARAGRAPHS = None
# SUMMARY_END_SUFFIX = '…'
# WITH_FUTURE_DATES = True
# The following line is specific to the monospace theme
MD_EXTENSIONS = ['codehilite(css_class=codehilite code)']
# PYGMENTS_RST_OPTIONS = []
# DEFAULT_PAGINATION = False
# PAGINATED_TEMPLATES = {'index': None, 'tag': None, 'category': None, 'author': None}
# PAGINATION_PATTERNS = (
#(1, '{name}{extension}', '{name}{extension}'),
#(2, '{name}{number}{extension}', '{name}{number}{extension}'),
#)

# ** Themeing ** 

# CSS_FILE = 'main.css'  # 'wide.css' is available too
THEME = 'monospace'
# STYLESHEET_URL = 'https://url.com/stylesheets'
# TEMPLATE_EXTENSIONS = ['.html']
# DIRECT_TEMPLATES = ['index', 'authors', 'categories', 'tags', 'archives']
# THEME_TEMPLATES_OVERRIDES = []  # defaults to templates/
# TEMPLATE_PAGES = {"pages/jinja2_template.html": "jinja2_template.html"}

# ** Jinja Config ** 

# JINJA_ENVIRONMENT = {'trim_blocks': True, 'lstrip_blocks': True}
# JINJA_GLOBALS = {}
# JINJA_TESTS = {}

# ** Basic Settings ** 

# USE_FOLDER_AS_CATEGORY = True
# DEFAULT_CATEGORY = 'misc'
# DOCUTILS_SETTINGS = {}  # used only w reStructText
# MARKDOWN = {...}
# READERS = {"html": None}  # ie; avoid processing .html files
# INTRASITE_LINK_REGEX = '[{|](?P<what>.*?)[|}]'
# FORMATTED_FIELDS = ['summary']

# ** URLs and Web Things ** 

# PORT = 8000
# BIND = ''
# Uncomment following line if you want doc-relative URLs when developing
RELATIVE_URLS = True
# ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
# ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
# PAGE_URL = 'pages/{slug}/'
# PAGE_SAVE_AS = 'pages/{slug}/index.html'
# others

# ** Paths ** 

# IGNORE_FILES = ['**/.*']
# OUTPUT_PATH = 'output/'  # should corresp to webserver virthost root dir
PATH = "content"
# PAGE_PATHS = {'pages'}
# PAGE_EXCLUDES = []
# PLUGIN_PATHS = []
# ARTICLE_PATHS = ['']
# ARTICLE_EXCLUDES = []
# STATIC_PATHS = [
#    "images",
#    "extra/robots.txt",
#]
# STATIC_EXCLUDES = []
# THEME_STATIC_PATHS = ['static']

# ** Behaviour On Site Generation ** 

# DELETE_OUTPUT_DIRECTORY = False
# OUTPUT_RETENTION = []
# LOG_FILTER = []
# OUTPUT_SOURCES = False
# OUTPUT_SOURCES_EXTENSION = '.text'
# THEME_STATIC_DIR = 'theme'
# STATIC_CREATE_LINKS = False
# STATIC_CHECK_IF_MODIFIED = False

# ** Caching and Modification Checking ** 

# CACHE_CONTENT = False
# CONTENT_CACHING_LAYER = 'reader'
# CACHE_PATH = 'cache'
# GZIP_CACHE = True
# CHECK_MODIFIED_METHOD = 'mtime'
# LOAD_CONTENT_CACHE = False

# ** Typogrify Config ** 

# TYPOGRIFY = False
# TYPOGRIFY_IGNORE_TAGS = []
# TYPOGRIFY_OMIT_FILTERS = []
# TYPOGRIFY_DASHES = 'default'

# Main Menu
MENUITEMS = (
    ("Zombo", "http://zombo.com"),
)

GITHUB_URL = 'https://robmagus/robmagus.github.io'

# Blogroll
# LINKS_WIDGET_NAME = 'links'
LINKS = (
    ("Rob Teszka Magic", "https://robteszkamagic.com"),
    ("The Parlour Magic Show", "http://parlourmagic.show"),
    ("Penny Ventures", "https://pennyventures.blogspot.com"),
    ("Pelican", "https://getpelican.com/"),
)

# Social widget
# SOCIAL_WIDGET_NAME = 'social'
SOCIAL = (
    ("Instagram", "https://instagram.com/robmagus"),
    ("Bluesky", "https://robteszka.bsky.social"),
)

# Feed generation is usually not desired when developing
# ATOM/RSS

FEED_DOMAIN = None  # i.e. base URL is "/"
FEED_ALL_ATOM = None
FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"
