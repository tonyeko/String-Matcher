from nltk import tokenize

def decomposition(path):
    file = open(path)
    text = tokenize.sent_tokenize(file.read())
    result = []
    for sentence in text:
        result.append(sentence.replace("\n", " "))
    return result
