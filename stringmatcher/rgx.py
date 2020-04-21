import re
import datetime

def search(text, pattern):
    regex = re.compile(pattern, re.IGNORECASE)
    return [m.start() for m in regex.finditer(text)]

def searchDigit(sentence):
  number = searchDigit2(sentence)
  if number[0] == '': number = searchDigit1(sentence)
  return number

def searchDigit1(text):
    '''Search number with digit format'''
    return [x.group() for x in re.finditer( r'[ "]\d+[\.,]?\d+( ?%)? ?(?:puluh|ratus|ribu|juta)? (?:\d+)?|^\d+[\.,]?\d+( ?%)? ?(?:puluh|ratus|ribu|juta)? (?:\d+)?', text)]

def searchDigit2(sentence):
  '''Search number with alphabetic format'''
  all = re.findall(r"((?:^(?:\d+)(?:,\d+)? ?|(?:lebih|kurang (?:dari )?)?(?:[sS]atu |[dD]ua |[tT]iga |[eE]mpat |[lL]ima |[eE]nam |[tT]ujuh |[dD]elapan |[sS]embilan ))?(?: ?%|persen|puluh|ratus|ribu|juta)?)",sentence)
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
    pattern = "(?:Kemarin (?:lusa)? ?,?)?((?:[sS]enin)?|(?:[sS]elasa)?|(?:[rR]abu)?|(?:[kK]amis)?|(?:[jJ]umat)?|(?:[sS]abtu)?|(?:[mM]inggu)?)[,-]? ?((0?[1-9])|([12][0-9])|3[01])[ -/](?:[jJ]an(?:uari)?|[fF]eb(?:ruari)?|[mM]ar(?:et)?|[aA]pr(?:il)?|[mM]ei|[jJ]uni?|[jJ]uli?|[aA]gustus|[sS]ept?(?:ember)?|[oO]kt(?:ober)?|[nN]ov(?:ember)?|[dD]es(?:ember)?)[ -/]\d{4}[ -/]? ?(?:[pP]ukul)?(?:\d{2}:\d{2})? ?(?:([wW][iI])([tT][aA]?|[bB]))?(?:(?:yang )?lalu)?"
    regex = re.compile(pattern)
    if regex.search(sentence): result.append(regex.search(sentence).group())
    return result

def searchDate5(sentence):
    '''Search date with pattern: Day (Date/Month/Year or Date-Month-Year)  Time TimeRegion'''
    result = []
    pattern = "(?:Kemarin (?:lusa)? ?,?)?((?:[sS]enin)?|(?:[sS]elasa)?|(?:[rR]abu)?|(?:[kK]amis)?|(?:[jJ]umat)?|(?:[sS]abtu)?|(?:[mM]inggu)?)[,-]? ?\(?((0?[1-9])|([12][0-9])|3[01])[ -/](0?[1-9]|1[12])[ -/]\d{4}[ -/]? ?(?:[pP]ukul)? ?(?:\d{2}[.:]?\d{2})? ?(?:([wW][iI])([tT][aA]?|[bB]))?(?:(?:yang )?lalu)?"
    regex = re.compile(pattern)
    if regex.search(sentence): result.append(regex.search(sentence).group())
    return result

# text = '''
# 421 Orang di Jabar Terkonfirmasi Positif COVID-19
# Yudha Maulana - detikNews
# Sabtu, 11 Apr 2020 20:07 WIB
# Bandung - Angka positif virus Corona atau COVID-19 di Jawa Barat menembus angka 400 kasus.
# Laman Pusat Informasi dan Koordinasi COVID-19 Jabar (Pikobar) pada Sabtu (11/4/2020) pukul 18.43
# WIB , mencatat terdapat 421 orang yang terkonfirmasi positif COVID-19.
# Dibandingkan sehari sebelumnya , jumlah tercatat yaitu 388 orang. Terjadi penambahan 8,5 persen
# atau 33 kasus per harinya. Sementara itu, secara nasional terdapat 3.842 kasus positif COVID-19.
# Dari 421 kasus tersebut, 40 orang meninggal dunia dengan keterangan terpapar COVID-19 .
# Sedangkan, angka kesembuhan di Jabar masih tetap berada di angka 19 orang.
# Per hari jumlah Orang Dalam Pemantauan (ODP) di Jabar mencapai 28.775 orang. Sebanyak 15.363
# di antaranya masih menjalani proses pemantauan dan 13.412 orang lainnya telah selesai menjalani
# proses pemantauan.  terkonfirmasi positifterkonfirmasi positif
# Sementara itu jumlah Pasien Dalam Pengawasan (PDP) mencapai 2.27 8 orang. Tercatat 1.344 orang
# masih menjalani proses pengawasan dan 934 orang lainnya telah selesai menjalani proses
# pengawasan. terkonfirmasi positif
# '''

# print(searchDate4(text))