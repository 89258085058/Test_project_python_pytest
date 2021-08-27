from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys

try:
    opt, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"


for o, a in opt:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", homephone="", mobilephone="",
                    workphone="", secondaryphone="", Address="", email="", email2="", email3="")] +[
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), homephone=random_string("homephone", 10), mobilephone=random_string("mobilephone", 10),
                workphone=random_string("workphone", 10), secondaryphone=random_string("secondaryphone", 10), Address=random_string("Address", 10),
                email=random_string("email", 10), email2=random_string("email2", 10), email3=random_string("email3", 10))
    for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as cont:
    cont.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))