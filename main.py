import Question

def main():

    question = Question.Question('What do you think of this project?')

    print question.getQuestion()

    newOpinion = input('What\'s your opinion of this from 1 to 5? ')
    newLeRiDefinition = input('Do you consider this to be on the Left or on the Right? ')
    newConLibDefinition = input('Do you consider this to be a conservative or a liberal value? ')

    question.setOpinion( newOpinion )
    question.setLeRiDefinition( newLeRiDefinition )
    question.setConLibDefinition( newConLibDefinition )

    question.showData()

    return 0

main()