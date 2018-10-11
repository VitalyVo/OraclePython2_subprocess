#!/usr/bin/python
#!!Code for python2
# Select from file test.sql

from subprocess import Popen, PIPE

def runSqlQuery(sqlCommand, connectString):
    session = Popen(['sqlplus', '-S', connectString], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    session.stdin.write(sqlCommand)
    return session.communicate()
connectString = ' / as sysdba'
sqlCommand = '@test.sql'
queryResult, errorMessage = runSqlQuery(sqlCommand, connectString)
print queryResult