# coding: utf-8

import urllib.request
import icalendar


ics_url = "http://eiga.com/movie/coming.ics"
ics = urllib.request.urlopen(ics_url).read()


cal = icalendar.cal.Component.from_ical(ics)
for e in cal.walk():
    if (isinstance(e, icalendar.cal.Event)):
        print("%s %s" % (e["DTSTART"].dt, e["SUMMARY"]))
