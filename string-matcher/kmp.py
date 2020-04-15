def computeLPS(pattern):
    lps = [0 for i in range(len(pattern))]
    lastLps = 0 #variabel untuk mencatat lps 
    indexNow = 1 #pencarian lps dari index-1 (lps[0] pasti 0)
    while indexNow < len(pattern):
        if pattern[indexNow] == pattern[lastLps]:
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
    lps = computeLPS(pattern)
    idxText = idxPattern = 0
    idxFound = []
    while idxText < len(text):
        if (pattern[idxPattern] == text[idxText]):
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


text = '''
421 Orang di Jabar Terkonfirmasi Positif COVID-19
Yudha Maulana - detikNews
Sabtu, 11 Apr 2020 20:07 WIB
Bandung - Angka positif virus Corona atau COVID-19 di Jawa Barat menembus angka 400 kasus.
Laman Pusat Informasi dan Koordinasi COVID-19 Jabar (Pikobar) pada Sabtu (11/4/2020) pukul 18.43
WIB , mencatat terdapat 421 orang yang terkonfirmasi positif COVID-19.
Dibandingkan sehari sebelumnya , jumlah tercatat yaitu 388 orang. Terjadi penambahan 8,5 persen
atau 33 kasus per harinya. Sementara itu, secara nasional terdapat 3.842 kasus positif COVID-19.
Dari 421 kasus tersebut, 40 orang meninggal dunia dengan keterangan terpapar COVID-19 .
Sedangkan, angka kesembuhan di Jabar masih tetap berada di angka 19 orang.
Per hari jumlah Orang Dalam Pemantauan (ODP) di Jabar mencapai 28.775 orang. Sebanyak 15.363
di antaranya masih menjalani proses pemantauan dan 13.412 orang lainnya telah selesai menjalani
proses pemantauan.  terkonfirmasi positifterkonfirmasi positif
Sementara itu jumlah Pasien Dalam Pengawasan (PDP) mencapai 2.27 8 orang. Tercatat 1.344 orang
masih menjalani proses pengawasan dan 934 orang lainnya telah selesai menjalani proses
pengawasan. terkonfirmasi positif
'''
print(search(text, "terkonfirmasi positif"))
print(text[333:333+len("terkonfirmasi positif")])
print(text[930:930+len("terkonfirmasi positif")])
print(text[951:951+len("terkonfirmasi positif")])
print(text[1167:1167+len("terkonfirmasi positif")])