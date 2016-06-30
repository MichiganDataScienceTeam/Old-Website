# This script takes a spreadsheet that can be found on google drive
# and converts the data into markdown for easy posting to the about page.

from pandas import read_csv
import sys

df = read_csv(sys.argv[1])
# Convert the table to a list of lists. Each list is a row from the spreadsheet.
rows = list(map(list, df.values))

for person in rows:
    # first two cols in sheet.csv are timestamp and email
    comps = person[2]
    title = person[3]
    blurb = person[4]
    link = person[5]
    name = person[6]
    post = """
### %(name)s

* _%(title)s_
* Competitions Completed: _%(comps)s_
* _%(blurb)s_
* [Personal Page](%(link)s)

---""" % locals()
    print(post)

