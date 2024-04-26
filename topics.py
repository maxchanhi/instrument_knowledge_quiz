from question import reed,transposing,clef,voice_types,piano_knowledge,orniments,instrumental_technique
def pick_topic(pick = str):
    topic = {'Reed':reed(),'Transposing':transposing(),
             "Clef":clef(),"Voice types":voice_types(),
             "Piano":piano_knowledge(),"Orniments":orniments(),
             "Inst. technique":instrumental_technique()
             }
    return topic[pick]
