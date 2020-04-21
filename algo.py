from stringmatcher import decomposer, kmp, bm, rgx

def search(listFile, keyword, method, currentFolder):
    fileResult = []
    for file in listFile:
        searchResult = []
        text = decomposer.decomposition(currentFolder+"/"+file)
        if method == "kmp":
            for sentence in text:
                idxFound = kmp.search(sentence, keyword);
                if idxFound: 
                    searchResult.append((rgx.searchDate(sentence), rgx.searchDigit(sentence), sentence))
        elif method == "bm":
            for sentence in text:
                idxFound = bm.search(sentence, keyword);
                if idxFound: searchResult.append(sentence)
        else:
            for sentence in text:
                idxFound = rgx.search(sentence, keyword);
                if idxFound: searchResult.append(sentence)
        fileResult.append((file, searchResult))
    print(fileResult)
    return fileResult
    

# search(['tes.txt'], "terkonfirmasi positif", "kmp", "test")