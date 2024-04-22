from question import reed,transposing,clef,voice_types,piano_knowledge
def pick_topic(pick = str):
    topic = {'Reed':reed(),'Transposing':transposing(),
             "Clef":clef(),"Voice types":voice_types(),
             "Piano":piano_knowledge()
               }
    return topic[pick]
