import sqlite3

class DbHandler:

    @staticmethod
    def execDB(dbname, cmd):

        print dbname
        print cmd

        conn = sqlite3.connect(dbname)

        c = conn.cursor()
        c.execute(cmd)
        conn.commit()
        conn.close()