# reflect and prefix metodu ile n bitlik gray code üreten betik

def GrayCodeGen(n=1,inc=["0","1"]):
    # n bit sayısı için n-1 kere döngüyü çalıştır
    for i in range(0,n-1):
        # gecici bir listeye başlangıç listesini tanımla 
        temp = []
        temp = inc[:]
        # geçici listeyi ters çevir ve başlangıç listesine ekle
        temp.reverse()
        inc = inc + temp

        # ilk listeden gelen elemanlara "0", geçici listeden gelenlere
        # "1" ön eki ekle 
        for i in range(len(inc)/2):
            inc[i] = "0" + inc[i]

        for j in range(len(inc)/2,len(inc)):
            inc[j] = "1" + inc[j]

    # elde edilen listedeki elemanları alt alta yaz
    for k in inc:
        print k


