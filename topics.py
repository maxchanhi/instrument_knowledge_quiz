from question import *
def pick_topic(pick = str):
    topic = {'Reed':reed(),'Transposing':transposing(),
             "Clef":clef(),"Voice types":voice_types(),
               }
    return topic[pick]
