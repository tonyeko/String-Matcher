def computeLPS(pattern):
    '''Compute LPS (longest proper prefix which is also suffix) for preprocessing in KMP Algorithm'''
    lps = [0 for i in range(len(pattern))]
    lastLps = 0 #variabel untuk mencatat lps 
    indexNow = 1 #pencarian lps dari index-1 (lps[0] pasti 0)
    while indexNow < len(pattern):
        if pattern[indexNow].lower() == pattern[lastLps].lower():
            lastLps+=1 #geser lastLps
            lps[indexNow] = lastLps
            indexNow+=1 #geser index saat ini
        elif lastLps > 0: #karakter pada pattern ke-i dan ke-lastLps tidak sama
            lastLps = lps[lastLps-1]
        else:
            lps[indexNow] = 0
            indexNow+=1

    return lps

def search(text, pattern):
    '''String matching KMP Algorithm modified, can search multiple pattern occurence in a text'''
    lps = computeLPS(pattern)
    idxText = idxPattern = 0
    idxFound = []
    while idxText < len(text):
        if (pattern[idxPattern].lower() == text[idxText].lower()):
            idxText+=1
            idxPattern+=1
            if idxPattern == len(pattern): 
                idxFound.append(idxText-idxPattern)
                idxPattern = 0
        elif idxPattern > 0:
            idxPattern = lps[idxPattern-1]
        else:
            idxText+=1
    return idxFound
