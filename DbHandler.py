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

    @staticmethod
    def getQuestionValues( dbname, tablename ):
        
        conn = sqlite3.connect( dbname )
        c = conn.cursor()
        c.execute("select * from {0}".format( tablename ))

        questionValues = c.fetchall()
        conn.close()

        return questionValues
    

    @staticmethod
    def getXValues( dbname, tablename ):

        conn = sqlite3.connect( dbname )
        c = conn.cursor()
        c.execute("select def1 from {0}".format( tablename ))

        xValues = [x[0] for x in c.fetchall()]

        print xValues

        return xValues


    @staticmethod
    def getYValues( dbname, tablename ):

        conn = sqlite3.connect( dbname )
        c = conn.cursor()
        c.execute("select def2 from {0}".format( tablename ))

        yValues = [y[0] for y in c.fetchall()]
        print yValues

        return yValues
