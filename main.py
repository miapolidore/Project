import mysql.connector # I don't understand why this is happening, "Defaulting to user installation because normal site-packages is not writeable...?"

# Going to attempt & restore previous progress while handling with the bug later.

connection = mysql.connector.connect(host = 'localHost', user  = 'root', password = 'mySqlPassword', database = 'bank')

'''
cursor = connection.cursor()
testQuery = ("SELECT * FROM banker")
cursor.execute(testQuery)
'''


