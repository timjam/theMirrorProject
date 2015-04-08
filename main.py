import Question
import matplotlib.pyplot as plt

def main():

    question = Question.Question('What do you think of this project?')

    print question.getQuestion()

    newOpinion = input('What\'s your opinion of this from 1 to 5? ')
    newLeRiDefinition = input('Do you consider this to be on the Left or on the Right? ')
    newConLibDefinition = input('Do you consider this to be a conservative or a liberal value? ')

    question.setOpinion( newOpinion )
    question.setLeRiDefinition( newLeRiDefinition )
    question.setConLibDefinition( newConLibDefinition )

    question.storeData(newLeRiDefinition, newConLibDefinition)

    plt.plot( [x-2 for x in question.loadLeRiDefinitions()], [y-2 for y in question.loadConLibDefinitions()], 'ro' )
    plt.axis( [-3, 3, -3, 3] )
    plt.show()



    return 0

main()