"""
Downloads and unzips each data file from the NYPD Stop and Frisk page
"""
import os.path
import re
import shutil
import requests
from urllib.parse import urljoin
from lxml import html
MAINURL = 'http://www.nyc.gov/html/nypd/html/analysis_and_planning/stop_question_and_frisk_report.shtml'
NYPD_RAW_PATH = 'data-hold/raw'
page = requests.get(MAINURL)
doc = html.fromstring(page.text)
hrefs = [a.attrib['href'] for a in doc.cssselect('a') if 'csv.zip' in a.attrib['href']]
for href in hrefs:
    year = re.search('\d{4}', href).group()
    url = urljoin(MAINURL, href)
    # zn is the zip file to save to
    zn = os.path.join(NYPD_RAW_PATH, "%s.zip" % year)
    with open(zn, 'wb') as zf:
        print("Downloading", url)
        zf.write(requests.get(url).content)
        zf.seek(0)
        print("Unzipping", zn)
        shutil.unpack_archive(zn, './data-hold')




