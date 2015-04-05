class Question:

    def __init__(self, question):
        self.question = question
        self.opinion = 0
        self.leRiDefinition = 0
        self.conLibDefinition = 0

    # Methods
    def showData(self):
        print 'Question: {0}'.format(self.question)
        print 'Your opinion: {0}'.format(self.opinion)
        print 'Your LeRi-definition: {0}'.format(self.leRiDefinition)
        print 'Your ConLib-definition: {0}'.format(self.conLibDefinition)



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