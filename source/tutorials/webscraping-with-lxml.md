~~~py
from lxml import html
import requests
url = 'http://en.wikipedia.org/wiki/List_of_NCAA_Division_I_institutions'
tree  = html.fromstring(requests.get(url).text)
school_cells = tree.cssselect('table.wikitable')[0].cssselect('tr th:nth-of-type(1) a')
school_names = [t.text_content() for t in school_cells]
~~~
