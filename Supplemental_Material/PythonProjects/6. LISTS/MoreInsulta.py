# http://pythonicprose.blogspot.com/2010/03/python-insult-generator.html
# negative reinforcement through insults

#
#
# Sometimes negative reinforcement is the way to go.
# For the times when you need a kick in the pants
# rather than a pat on the back I whipped up this

# insult generator.
# It will churn out more insults then you can shake
# a stick at.

import random

class insultGenerator(object):
    def __init__(self):
        # setup the lists of insult fodder

        self.nounList = ['loser',
                         'jerk',
                         'nerd',
                         'doodie head',
                         'butthead',
                         'bonehead',
                         'dunce',
                         'moron',
                         'nerf herder']
        self.adjectiveList = ['smelly',
                              'ugly',
                              'gimpy',
                              'slimy',
                              'crabby',
                              'scabby',
                              'scratchy']
        self.connectorList = ['are one',
                              'are the biggest',
                              'are becoming a']
    def getInsult(self):
        insult = "you"

        # connector phrase
        connector = random.randint(1, len(self.connectorList))
        insult += " " + self.connectorList[connector-1]

        # adjectives
        adjCount = random.randint(2,4)
        random.shuffle(self.adjectiveList)
        for i in range(0,adjCount):
            if i != 0:
                insult += ", "

            else:
                insult += " "
            insult += self.adjectiveList[i]

        # ending noun
        noun = random.randint(1,len(self.nounList))
        insult += " " + self.nounList[noun-1]
        return insult


# a little example to get some insults flowing
if __name__ == '__main__':
    ig = insultGenerator()
    print(ig.getInsult())



# my output:
#   you are one ugly, slimy, scabby loser
#   you are the biggest scabby, slimy nerd
#   you are becoming a scabby, ugly, gimpy butthead

#   you are one slimy, smelly, crabby bonehead