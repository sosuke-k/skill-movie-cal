# coding: utf-8

import urllib.request
import icalendar
import pendulum


def lambda_handler(event, context):

    # if (event.session.application.applicationId !== "amzn1.echo-sdk-ams.app.[unique-value-here]") {
    #     context.fail("Invalid Application ID")
    # }

    ics_url = "http://eiga.com/movie/coming.ics"
    ics = urllib.request.urlopen(ics_url).read()

    movies = []
    cal = icalendar.cal.Component.from_ical(ics)
    for e in cal.walk():
        if (isinstance(e, icalendar.cal.Event)):

            movies.append((e["DTSTART"].dt, e["SUMMARY"]))

    now = pendulum.now()
    one_week_ago = now.subtract(days=7)
    text = "最近公開した映画は、"
    released_movies = [m for m in movies if m[0] <= now and m[0] >= one_week_ago]

    if len(released_movies) > 0:
        released_movies = sorted(released_movies, key=lambda x: x[0], reverse=True)[:5]
        text = text + "、".join([m[1] for m in released_movies]) + "です。"
    else:
        text = text + "ありません。"

    response = {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": text,
            }
        }
    }
    return response
