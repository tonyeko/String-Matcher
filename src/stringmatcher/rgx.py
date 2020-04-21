import re
import datetime

def search(text, pattern):
    '''String matching with Regex'''
    regex = re.compile(pattern, re.IGNORECASE)
    return [m.start() for m in regex.finditer(text)]

def searchDigit(sentence):
  number = searchDigit2(sentence)
  if number[0] == '': number = searchDigit1(sentence)
  return number

def searchDigit1(text):
    '''Search number with digit format'''
    return [x.group() for x in re.finditer( r'[ "]\d+[\.,]?\d+( ?%)? ?(?:[pP]uluh|[rR]atus|[rR]ibu|[jJ]uta)? (?:\d+)?|^\d+[\.,]?\d+( ?%)? ?(?:[pP]uluh|[rR]atus|[rR]ibu|[jJ]uta)? (?:\d+)?', text)]

def searchDigit2(sentence):
  '''Search number with alphabetic format'''
  all = re.findall(r"((?:^(?:\d+)(?:,\d+)? ?|(?:[lL]ebih|[kK]urang (?:dari )?)?(?:[sS]atu |[dD]ua |[tT]iga |[eE]mpat |[lL]ima |[eE]nam |[tT]ujuh |[dD]elapan |[sS]embilan ))?(?: ?%|[pP]ersen|[pP]uluh|[rR]atus|[rR]ibu|[jJ]uta)?)",sentence)
  return all


def searchDate(sentence):
    result = searchDate5(sentence)
    if not result: result = searchDate4(sentence)
    if not result: result = searchDate3(sentence, "/")
    if not result: result = searchDate3(sentence, "-")
    if not result: result = searchDate2(sentence, "/")
    if not result: result = searchDate2(sentence, "-")
    return result

def searchDate2(sentence, separator):
    '''Search date with pattern: DD/MM/YY or DD-MM-YY'''
    result = []
    pattern = '\d{1,2}'+separator+'\d{1,2}'+separator+'\d{2}'
    dateformat = "%d"+separator+"%m"+separator+"%y"
    regex = re.compile(pattern)
    for match in regex.finditer(sentence):
        try:
            datetime.datetime.strptime(match.group(), dateformat)
            result.append(match.group())
        except ValueError:
            pass
    return result

def searchDate3(sentence, separator):
    '''Search date with pattern: DD/MM/YYYY or DD-MM-YYYY'''
    result = []
    pattern = '\d{1,2}'+separator+'\d{1,2}'+separator+'\d{4}'
    dateformat = "%d"+separator+"%m"+separator+"%Y"
    regex = re.compile(pattern)
    for match in regex.finditer(sentence):
        try:
            datetime.datetime.strptime(match.group(0), dateformat)
            result.append(match.group(0))
        except ValueError:
            pass
    return result

def searchDate4(sentence):
    '''Search date with pattern: Day Date Month Year Time TimeRegion'''
    result = []
    pattern = "(?:Kemarin (?:lusa)? ?,?)?((?:[sS]enin)?|(?:[sS]elasa)?|(?:[rR]abu)?|(?:[kK]amis)?|(?:[jJ]umat)?|(?:[sS]abtu)?|(?:[mM]inggu)?)[,-]? ?((0?[1-9])|([12][0-9])|3[01])[ -/](?:[jJ]an(?:uari)?|[fF]eb(?:ruari)?|[mM]ar(?:et)?|[aA]pr(?:il)?|[mM]ei|[jJ]uni?|[jJ]uli?|[aA]gustus|[sS]ept?(?:ember)?|[oO]kt(?:ober)?|[nN]ov(?:ember)?|[dD]es(?:ember)?)[ -/](?:\d{4})?[ -/]? ?(?:[pP]ukul)?(?:\d{2}:\d{2})? ?(?:([wW][iI])([tT][aA]?|[bB]))?(?:(?:yang )?lalu)?"
    regex = re.compile(pattern)
    if regex.search(sentence): result.append(regex.search(sentence).group())
    return result

def searchDate5(sentence):
    '''Search date with pattern: Day (Date/Month/Year or Date-Month-Year)  Time TimeRegion'''
    result = []
    pattern = "(?:Kemarin (?:lusa)? ?,?)?((?:[sS]enin)?|(?:[sS]elasa)?|(?:[rR]abu)?|(?:[kK]amis)?|(?:[jJ]umat)?|(?:[sS]abtu)?|(?:[mM]inggu)?)[,-]? ?\(?((0?[1-9])|([12][0-9])|3[01])[ -/](0?[1-9]|1[12])[ -/](?:\d{4})?[ -/]? ?(?:[pP]ukul)? ?(?:\d{2}[.:]?\d{2})? ?(?:([wW][iI])([tT][aA]?|[bB]))?(?:(?:yang )?lalu)?"
    regex = re.compile(pattern)
    if regex.search(sentence): result.append(regex.search(sentence).group())
    return result
