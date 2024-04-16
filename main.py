import mysql.connector as mysql # I don't understand why this is happening, "Defaulting to user installation because normal site-packages is not writeable...?"
# FIXED IT!! By creating a virtual environment I was able to identify that I has a $PATH conflict.

# Going to attempt & restore previous progress while handling with the bug later.

connection = mysql.connect(host = 'localHost', user  = 'root', password = 'mySqlPassword', database = 'bank')

'''
cursor = connection.cursor()
testQuery = ("SELECT * FROM banker")
cursor.execute(testQuery)
'''


