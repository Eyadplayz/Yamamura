#
# doc.py - a not-intended-to-be-imported documentation file
# 
# author: superwhiskers
# license: gplv3 
#

# these need to be imported for this file to be valid python
import random # for generating random numbers
import time   # for getting the time

"""
so, here is a file containing numerous breakdowns of how some things in
yamamura are constructed, reading this file gives you a fairly good idea
of how i, superwhiskers, constructed some of the more complicated or
frequently used things of yamamura.
"""

"""
1 - serverInfo dict

a dict containing info about a server yamamura is in

constructed from cfg.yaml inside of the servers/<serverid>_<servername> folder
generated by yamamura on first startup and the first time joining that server,
respectively
"""
serverInfo = dict(
    dbName = "db" ,           # string, the name of the database file, excluding extension
    dbPath = "path/to/db.db", # string, the full path to the database file, starting from the Yamamura root folder
    mods   = [ 1010, 1010 ]   # list, a list containing discord user ids for each of the mods in a server 
)

# this shows you the dict when this file is run
print("-- testing serverInfo")
print(serverInfo)

"""
2 - a whiskerflake

a string consisting of a hash of seconds since epoch in utc, and a
hash of a random number obtained from a list of random nummbers
generated in the range 1000 -> 9999
"""
def whiskerflake():
    # pick a random number from a list of 10
    # random ints ranging from 1000 -> 9999,
    # and then hash it after getting absoulute
    # value, then turn it into a string
    hopefullyRandInt = str(
        hash(
            abs(
                random.choice(
                     [ random.randint(1000, 9999) for _ in range(10) ]
                )
            )
        )
    )
    # then, generate a string from the hash
    # of seconds since epoch
    secondsSinceEpochHash = str(
        hash(
            time.time()
        )
    )

    # finally, add these two values and return them
    return ( secondsSinceEpochHash + hopefullyRandInt )

# test it for you
print("-- testing whiskerflake")
print(whiskerflake())

"""
3 - the mail dict:

a dict containing information about a modmail. generated by yamamura when a
modmail is sent
"""
mail = dict(
    id      = whiskerflake(),   # string, a whiskerflake. see #2
    sender  = 1010,             # int, a discord user id for the sender
    message = "hey there mods", # string, a string containing the message the user sent
    readBy  = [ 1010, 1010 ]    # list, a list containing discord user ids for each of the mods in a server 
)

# this shows you what could be a mail dict once it is generated
print("-- testing mail")
print(mail)
