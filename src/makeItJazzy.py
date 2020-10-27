def csMakeItJazzy(chords):
    chordNum = '7'
    newChordsList = []
    testForSeven = ''.join(str(e) for e in chords)
    res = testForSeven.find('7')

    if res >= 0:
         return chords
    else:
        for chord in chords:
            newChords = chord + str(chordNum)
            newChordsList.append(newChords) 

        return newChordsList

print(csMakeItJazzy(["G", "F", "C"]))