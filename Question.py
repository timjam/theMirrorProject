from DbHandler import DbHandler

class Question:

    questionCount = 0

    def __init__(self, question):

        Question.questionCount += 1

        self.questionID = Question.questionCount
        self.question = question
        self.opinion = 0
        self.leRiDefinition = 0
        self.conLibDefinition = 0
        self.dbname = 'theMirrorProject-questions.db'
        self.tablename = 'q{0}'.format(self.questionID)
        
        cmd = "create table if not exists {0} (def1 integer, def2 integer)".format(self.tablename) #Can't have spaces in the table name. Create a table with the question ID somehow
        DbHandler.execDB( self.dbname, cmd)


    # Methods
    def showData(self):
        print 'Question: {0}'.format(self.question)
        print 'Your opinion: {0}'.format(self.opinion)
        print 'Your LeRi-definition: {0}'.format(self.leRiDefinition)
        print 'Your ConLib-definition: {0}'.format(self.conLibDefinition)

    def storeData(self, leRiDefinition, conLibDefinition):

        storecmd = "insert into {0} values ({1},{2})".format(self.tablename, leRiDefinition, conLibDefinition)
        DbHandler.execDB( self.dbname, storecmd )
        
        DbHandler.showTables( self.dbname )
        DbHandler.showTableValues( self.dbname, self.tablename )



    # Getters
    def getQuestion(self):
        return self.question

    def getOpinion(self):
        return self.opinion

    def getLeRiDefinition(self):
        return self.leRiDefinition

    def getConLibDefinition(self):
        return self.conLibDefinition



    # Setters
    def setOpinion(self, newOpinionValue):
    	self.opinion = newOpinionValue

    def setLeRiDefinition(self, newLeRiDefinitionValue):
        self.leRiDefinition = newLeRiDefinitionValue

    def setConLibDefinition(self, newConLibDefinition):
        self.conLibDefinition = newConLibDefinition