import decomposer
import kmp
import bm
import rgx
import time

def main(path, keyword, method):
    result = []
    start = time.time()
    text = decomposer.decomposition(path)
    if method == "kmp":
        for sentence in text:
            idxFound = kmp.search(sentence, keyword);
            if idxFound: result.append((sentence, idxFound)); print(sentence); print("=================")
    elif method == "bm":
        for sentence in text:
            idxFound = bm.search(sentence, keyword);
            if idxFound: result.append((sentence, idxFound)); print(sentence); print("=================")
    else:
        for sentence in text:
            idxFound = rgx.search(sentence, keyword);
            if idxFound: result.append((sentence, idxFound)); print(sentence); print("=================")
    print(result)
    print(len(result))
    print(time.time()-start)
    
main('tes.txt', "terkonfirmasi positif", "regex")