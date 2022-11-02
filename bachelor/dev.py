# from app.sql.parser.parser import parser
#
# parser("SELECT * FROM datatable_1; SELECT one FROM datatable_2")

from typing import Any

# from pyparsing import Word, alphas
#
#
# greet = Word(alphas) + "," + Word(alphas) + "!"
# hello = "Hello, World!"
# a = greet.parseString(hello)
#
# print(hello, "->", greet.parseString(hello))

# from typing import Any
#
import sqlparse  # type: ignore

#
# from app.consts import SQL_MACROS
#
#
# query = """
# SELECT *
# FROM datatable
# where years>'1993'
# """
#
# query = sqlparse.format(  # type: ignore
#     query,
#     reindent=True,
#     keyword_case="upper",
#     use_space_around_operators=True,
# )
#
# a = """
# --begin-sql
# SELECT dataset_1_select
# FROM dataset_1
# SYMDIFF
# SELECT dataset_2_select
# FROM dataset_2
#
# /**/
#
# SELECT *
# FROM (
#     SELECT {dataset_1_select}
#     FROM dataset_1
#     UNION
#     SELECT {dataset_2_select}
#     FROM dataset_2
# ) AS symdiff_{random}
# EXCEPT
# SELECT *
# FROM (
#     SELECT {dataset_1_select}
#     FROM dataset_1
#     INTERSECT
#     SELECT {dataset_2_select}
#     FROM dataset_2
# ) AS symdiff_{random}
# --end-sql
# """
#
response = sqlparse.parse(
    """
SELECT dataset_1_select
FROM dataset_1
SYMDIFF
SELECT dataset_2_select
FROM dataset_2
"""
)

parsed = response[0]

for _token in response[0].tokens:  # type: ignore
    token: Any = _token

    if str(token) in ("SYMDIFF",):
        print(token)

#
#
# Makro pro relační dělení

from pyparsing import (
    Optional,
    oneOf,
    Literal,
    Word,
    printables,
    Group,
    OneOrMore,
    ZeroOrMore,
)

"""
A simple parser for calendar (*.ics) files,
as exported by the Mozilla calendar.

Any suggestions and comments welcome.

Version:   0.1
Copyright: Petri Savolainen <firstname.lastname@iki.fi>
License:   Free for any use
"""


# TERMINALS

BEGIN = Literal("BEGIN:").suppress()
END = Literal("END:").suppress()
valstr = printables + "\xe4\xf6\xe5\xd6\xc4\xc5 "

EQ = Literal("=").suppress()
SEMI = Literal(";").suppress()
COLON = Literal(":").suppress()

EVENT = Literal("VEVENT").suppress()
CALENDAR = Literal("VCALENDAR").suppress()
ALARM = Literal("VALARM").suppress()

# TOKENS

CALPROP = oneOf("VERSION PRODID METHOD", asKeyword=True)
ALMPROP = oneOf("TRIGGER", asKeyword=True)
EVTPROP = oneOf(
    """X-MOZILLA-RECUR-DEFAULT-INTERVAL
       X-MOZILLA-RECUR-DEFAULT-UNITS
       UID DTSTAMP LAST-MODIFIED X RRULE EXDATE""",
    asKeyword=True,
)

valuestr = Word(valstr).setName("valuestr")
propval = valuestr
typeval = valuestr
typename = oneOf("VALUE MEMBER FREQ UNTIL INTERVAL", asKeyword=True)

proptype = Group(SEMI + typename + EQ + typeval).setName("proptype").suppress()

calprop = Group(CALPROP + ZeroOrMore(proptype) + COLON + propval)
almprop = Group(ALMPROP + ZeroOrMore(proptype) + COLON + propval)
evtprop = (
    Group(EVTPROP + ZeroOrMore(proptype) + COLON + propval).suppress()
    | "CATEGORIES" + COLON + propval.setResultsName("categories")
    | "CLASS" + COLON + propval.setResultsName("class")
    | "DESCRIPTION" + COLON + propval.setResultsName("description")
    | "DTSTART" + proptype + COLON + propval.setResultsName("begin")
    | "DTEND" + proptype + COLON + propval.setResultsName("end")
    | "LOCATION" + COLON + propval.setResultsName("location")
    | "PRIORITY" + COLON + propval.setResultsName("priority")
    | "STATUS" + COLON + propval.setResultsName("status")
    | "SUMMARY" + COLON + propval.setResultsName("summary")
    | "URL" + COLON + propval.setResultsName("url")
).setName("evtprop")
calprops = Group(OneOrMore(calprop)).setName("calprops").suppress()
evtprops = Group(OneOrMore(evtprop))
almprops = Group(OneOrMore(almprop)).setName("almprops").suppress()

alarm = (BEGIN + ALARM + almprops + END + ALARM).setName("alarm")
event = (BEGIN + EVENT + evtprops + Optional(alarm) + END + EVENT).setName("event")
events = Group(OneOrMore(event))
calendar = (BEGIN + CALENDAR + calprops + ZeroOrMore(event) + END + CALENDAR).setName(
    "calendar"
)
calendars = OneOrMore(calendar)


# PARSE ACTIONS


def gotEvent(_, __, toks):
    print(toks)


event.setParseAction(gotEvent)


# MAIN PROGRAM

if __name__ == "__main__":

    calendars.parseFile("mozilla.ics")
