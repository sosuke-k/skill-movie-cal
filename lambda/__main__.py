# coding: utf-8

import urllib.request
import icalendar


def lambda_handler(event, context):

    if (event.session.application.applicationId != = "amzn1.echo-sdk-ams.app.[unique-value-here]") {
        context.fail("Invalid Application ID")
    }

    ics_url = "http://eiga.com/movie/coming.ics"
    ics = urllib.request.urlopen(ics_url).read()

    cal = icalendar.cal.Component.from_ical(ics)
    for e in cal.walk():
        if (isinstance(e, icalendar.cal.Event)):
            print("%s %s" % (e["DTSTART"].dt, e["SUMMARY"]))
