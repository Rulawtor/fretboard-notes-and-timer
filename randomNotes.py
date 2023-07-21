import random
import time

notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#",]
again = True

while again:
    time_end = time.time()
    noteIndex = random.choice(notes)
    notes.remove(noteIndex)
    
    if notes == []:
        notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#",]
        
    print(noteIndex)
    
    repeat = input()
    lap = round((time.time() - time_end), 2)

    print(str(lap) +"\n")
    if repeat != "":
        again = False