#!/usr/bin/python
#RMAN. Command from Rman. For Python2

from subprocess import Popen, PIPE

def runRmanQuery(rmanCommand, connectString):
    session = Popen(['rman', connectString], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    session.stdin.write(rmanCommand)
    return session.communicate()

connectString = 'target /'

rmanCommand = 'show all;'
queryResult, errorMessage = runRmanQuery(rmanCommand, connectString)
print queryResult