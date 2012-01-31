import sys
import os
try:
    import json
except ImportError:
    import simplejson as json 

def printlist(sfolder):
    for filename in os.listdir(sfolder):
        teamname = filename.split('.')[0]
        print "%s,%s\\%s,%s" % (teamname,sfolder,filename,sfolder)


printlist('NHL')
printlist('MLB')
printlist('NBA')
printlist('NFL')


soccerdata = json.load(open('top100.json'))

keys = soccerdata.keys()
keys.sort()

for imagename in keys:
    print "SOC%s,Soccer\\%s.gif,Soccer,%s" % (imagename, imagename, soccerdata[imagename])
