import pymysql.cursors
import sys

coursenum = sys.argv[1]
dept = sys.argv[2]


connection = pymysql.connect(host='uvaclasses.martyhumphrey.info',
                                 user='UVAClasses',
                                 password='WR6V2vxjBbqNqbts',
                                 db='uvaclasses',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql1 = "SELECT `EnrollmentLimit` FROM `CompSci1178Data` WHERE `ClassNumber`=%s and `Mnemonic`=%s"
        sql2 = "SELECT `Enrollment` FROM `CompSci1178Data` WHERE `ClassNumber`=%s and `Mnemonic`=%s"
        cursor.execute(sql1,(coursenum, dept))
        result1 = cursor.fetchone()
        cursor.execute(sql2,(coursenum, dept))
        result2 = cursor.fetchone()

        if dept == "CS" or dept == "cs":
            if result1 != None:
                print "The course " + coursenum + " in " + dept + " has " + str(int(result1['EnrollmentLimit']) - int(result2['Enrollment'])) + " seats left"
            else: print "I am not aware of that course at the University of Virginia"
        else: print "I am not aware of that department at the University of Virginia"

finally:
    connection.close()