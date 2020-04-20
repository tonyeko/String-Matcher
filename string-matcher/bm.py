def buildLast(pattern):
    last = [-1 for i in range(128)]
    for i in range(len(pattern)):
        last[ord(pattern[i].lower())] = i
    return last

def search(text, pattern):
    '''String matching Boyer Moore Algorithm modified, can search multiple pattern occurence in a text'''
    last = buildLast(pattern)
    idxText = idxPattern = len(pattern)-1
    idxFound = []
    while idxText < len(text):
        if pattern[idxPattern].lower() == text[idxText].lower():
            if idxPattern == 0: 
                idxFound.append(idxText)
                idxText = idxText+2*len(pattern)-1 #geser text ke posisi string setelah matched
                idxPattern = len(pattern)-1 #reset idxPattern
            else:
                idxText-=1
                idxPattern-=1
        else:
            lastOcc = last[ord(text[idxText].lower())]
            idxText += len(pattern)-min(idxPattern, 1+lastOcc)
            idxPattern = len(pattern)-1
    return idxFound