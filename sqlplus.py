#!/usr/bin/python
# !!! Code For python2

from subprocess import Popen, PIPE
 
#function that takes the sqlCommand and connectString and returns the queryReslut and errorMessage (if any)
def runSqlQuery(sqlCommand, connectString):
    session = Popen(['sqlplus', '-S', connectString], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    session.stdin.write(sqlCommand)
    return session.communicate()

#example 1: run a query that returns a numeric value
connectString = 'system/passwd_db'
sqlCommand = 'select * from dual;'
queryResult, errorMessage = runSqlQuery(sqlCommand, connectString)
print queryResult
