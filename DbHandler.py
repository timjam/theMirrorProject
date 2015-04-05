import sqlite3

class DbHandler:

    @staticmethod
    def execDB(dbname, cmd):

        conn = sqlite3.connect(dbname)

        c = conn.cursor()
        c.execute(cmd)
        conn.commit()
        conn.close()

    @staticmethod
    def showTables(dbname):

        conn = sqlite3.connect(dbname)
        c = conn.cursor()

        c.execute("SELECT name FROM sqlite_master WHERE type='table';")

        print
        print(c.fetchall())

        conn.close()

    @staticmethod
    def showTableValues( dbname, tablename ):
    	conn = sqlite3.connect(dbname)

    	c = conn.cursor()
    	c.execute("select * from {0}".format( tablename ))

    	print
    	print(c.fetchall())

    	conn.close()