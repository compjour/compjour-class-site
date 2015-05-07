"""
From the downloaded CSV files, fixes and unifies the headers across the different years.
Also produces a datetimestop column derived from the datestop and timestop columns

https://twitter.com/dancow/status/547157958476693504
Also produces lat/lng
http://pp19dd.com/2009/08/converting-state-plane-coordinates-to-lat-lon/
ong=-77.54227+0.000003599176×X
lat=40.16624+0.000002746597×Y


The end result is one large file.
"""

import re
DATEREGEXER = [
    # change 12/30/2014 to 2014-12-30
    (r'(?P<month>\d{2})(?P<day>\d{2})(?P<year>\d{4})', '\g<year>-\g<month>-\g<day>'),
    # fix 1142014 to 2014-01-14
    (r'(?P<month>\d)(?P<day>\d{2})(?P<year>\d{4})', '\g<year>-0\g<month>-\g<day>'),
]

TIMEREGEXER = [
    # change 1215 to 12:!5
    ('(?P<hour>\d{2})(?P<minute>\d{2})', '\g<hour>:\g<minute>'),
    # change 115 or 1:15 to 01:15
    ('^(?P<hour>\d):?(?P<minute>\d{2})$', '0\g<hour>:\g<minute>'),
    # change 54 to 00:54
    ('^(?P<minute>\d{2})$', '00:\g<minute>'),
    # change 4 to 00:04
    ('^(?P<minute>\d{1})$', '00:0\g<minute>')
]


def fix_date_str(s):
    for i, (regex, rtxt) in enumerate(DATEREGEXER):
        if re.search(regex, s):
            s = re.sub(regex, rtxt, s)
            break
    return s

def fix_time_str(s):
    for i, (regex, rtxt) in enumerate(TIMEREGEXER):
        if re.search(regex, s):
            s = re.sub(regex, rtxt, s)
            break
    return s

df = pd.read_csv(fname)
