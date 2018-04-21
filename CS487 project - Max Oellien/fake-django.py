import random
from pprint import pprint

from bs4 import BeautifulSoup as bs
from yattag import Doc

weekdays = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
]
days = [str(i) for i in range(30)]
month = 'April'

output_name = 'calendar_output.html'


def generate_html(month, days, weekdays):
    doc, tag, text = Doc().tagtext()

    with tag('html'):
        with tag('head'):
            doc.stag('link', rel="stylesheet", href="style.css")

        with tag('body'):
            with tag('h1'):
                text('Hawk Calendar')

            with tag('div', klass='month'):
                with tag('ul'):
                    with tag('li', klass='prev'):
                        text('<')

                    with tag('li', klass='next'):
                        text('>')

                    with tag('li'):
                        text(month)

            with tag('ul', klass='weekdays'):
                for day in weekdays:
                    with tag('li'):
                        text(day)

            random_pos = random.randrange(0, len(days))

            with tag('ul', klass="days"):

                for i in range(len(days)):
                    day = days[i]
                    with tag('li'):
                        if i is not random_pos:
                            text(day)
                        else:
                            with tag('span', klass="active"):
                                text(day)



    return doc.getvalue()


if __name__ == '__main__':
    weekdays = [weekday[0:2] for weekday in weekdays]  # le snip snip ;)

    outstr = generate_html(month, days, weekdays)

    outstr = bs(outstr, 'html.parser').prettify()  # prettify it

    with open(output_name, 'w') as f:  # output HTML
        f.write(outstr)
