import os
import math


inverted_s_box = [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3,
                  0x9e, 0x81, 0xf3, 0xd7, 0xfb, 0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f,
                  0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb, 0x54,
                  0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b,
                  0x42, 0xfa, 0xc3, 0x4e, 0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24,
                  0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25, 0x72, 0xf8,
                  0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d,
                  0x65, 0xb6, 0x92, 0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda,
                  0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84, 0x90, 0xd8, 0xab,
                  0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3,
                  0x45, 0x06, 0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1,
                  0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b, 0x3a, 0x91, 0x11, 0x41,
                  0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6,
                  0x73, 0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9,
                  0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e, 0x47, 0xf1, 0x1a, 0x71, 0x1d,
                  0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
                  0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0,
                  0xfe, 0x78, 0xcd, 0x5a, 0xf4, 0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07,
                  0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f, 0x60,
                  0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f,
                  0x93, 0xc9, 0x9c, 0xef, 0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5,
                  0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61, 0x17, 0x2b,
                  0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55,
                  0x21, 0x0c, 0x7d]

s_box = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67,
         0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59,
         0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7,
         0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1,
         0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05,
         0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83,
         0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29,
         0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
         0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa,
         0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c,
         0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc,
         0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec,
         0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19,
         0x73, 0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee,
         0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49,
         0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
         0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4,
         0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6,
         0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70,
         0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9,
         0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e,
         0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1,
         0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0,
         0x54, 0xbb, 0x16]

r_con = [0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36,
         0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97,
         0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72,
         0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66,
         0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04,
         0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d,
         0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3,
         0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61,
         0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a,
         0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
         0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc,
         0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5,
         0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a,
         0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d,
         0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c,
         0xd8, 0xab, 0x4d, 0x9a, 0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35,
         0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4,
         0xd3, 0xbd, 0x61, 0xc2, 0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc,
         0x83, 0x1d, 0x3a, 0x74, 0xe8, 0xcb, 0x8d, 0x01, 0x02, 0x04, 0x08,
         0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a,
         0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d,
         0xfa, 0xef, 0xc5, 0x91, 0x39, 0x72, 0xe4, 0xd3, 0xbd, 0x61, 0xc2,
         0x9f, 0x25, 0x4a, 0x94, 0x33, 0x66, 0xcc, 0x83, 0x1d, 0x3a, 0x74,
         0xe8, 0xcb]



def encrypt(giris_dizisi, mod, anahtar, IV):
    global modlar
    if len(anahtar) % 16 or len(IV) % 16:
        return None
    sifre_metni_sonucu = []
    if giris_dizisi is not None:
        sifre_metni_sonucu = enc(giris_dizisi, mod, anahtar, IV)
    return sifre_metni_sonucu


son_sifre = []


def enc(giris_dizisi, mod, anahtar, IV):
    global son_sifre
    giris = [0] * 16
    sifre_metni_sonucu = []
    sifre_metni = [0] * 16
    ilk_tur = True
    for j in range(int(math.ceil(float(len(giris_dizisi)) / 16))):
        basla = j * 16
        bitir = j * 16 + 16
        if bitir > len(giris_dizisi):
            bitir = len(giris_dizisi)
        plaintext = ceviri(giris_dizisi, basla, bitir, mod)
        if mod == modlar.get("OFB"):
            ilk_tur, giris, plaintext, sifre_metni, sifre_metni_sonucu = enc_ofb(ilk_tur,
                                                                                 giris, IV, anahtar, plaintext,
                                                                                 sifre_metni, sifre_metni_sonucu,
                                                                                 bitir - basla)
        elif mod == modlar.get("CBC"):
            ilk_tur, sifre_metni, giris, sifre_metni_sonucu = enc_cbc(ilk_tur, giris,
                                                                      anahtar, plaintext, IV, sifre_metni,
                                                                      sifre_metni_sonucu)

        son_sifre = sifre_metni_sonucu[-16:]
    return sifre_metni_sonucu


def enc_ofb(ilk_tur, giris, IV, anahtar, plaintext, sifre_metni, sifre_metni_sonucu, sayac):
    if ilk_tur:
        cikis = encrypt_decrypt(IV, anahtar, True)
        ilk_tur = False
    else:
        cikis = encrypt_decrypt(giris, anahtar, True)
    for i in range(0, 16):
        plaintext_boyutu = len(plaintext)
        cikis_boyutu = len(cikis)
        if plaintext_boyutu - 1 < i:
            sifre_metni[i] = 0 ^ cikis[i]
        elif cikis_boyutu - 1 < i:
            sifre_metni[i] = plaintext[i] ^ 0
        elif plaintext_boyutu - 1 < i and cikis_boyutu < i:
            sifre_metni[i] = 0 ^ 0
        else:
            sifre_metni[i] = plaintext[i] ^ cikis[i]
    for k in range(0, sayac):
        sifre_metni_sonucu.append(sifre_metni[k])
    return ilk_tur, cikis, plaintext, sifre_metni, sifre_metni_sonucu


def enc_cbc(ilk_tur, giris, anahtar, plaintext, IV, sifre_metni, sifre_metni_sonucu):
    for i in range(0, 16):
        if ilk_tur:
            giris[i] = plaintext[i] ^ IV[i]
        else:
            giris[i] = plaintext[i] ^ sifre_metni[i]
    ilk_tur = False
    sifre_metni = encrypt_decrypt(giris, anahtar, True)
    # CBC dolgusu icin 16 bayt
    for k in range(0, 16):
        sifre_metni_sonucu.append(sifre_metni[k])
    return ilk_tur, sifre_metni, giris, sifre_metni_sonucu


def anahtar_genisletimi(anahtar, yeni_boyut):
    yeni_anahtar = [0] * yeni_boyut
    for j in range(0, 16):
        yeni_anahtar[j] = anahtar[j]
    boyut = 16
    sayac = 1
    while True:
        if boyut >= yeni_boyut:
            break
        yedek_anahtar = yeni_anahtar[boyut - 4:boyut]
        if boyut % 16 == 0:
            yedek_anahtar = ozut(yedek_anahtar, sayac)
            sayac += 1
        for gosterge in range(0, 4):
            yeni_anahtar[boyut] = yeni_anahtar[boyut - 16] ^ yedek_anahtar[gosterge]
            boyut += 1
    return yeni_anahtar


def anahtar_olustur(genisletilmis_anahtar, sayac):
    """
    Verilen genişletilmiş anahtardan ve
    genişletilmiş anahtar içindeki konumdan yuvarlak bir anahtar oluşturur.
    """
    anahtar = [0] * 16
    for dongu in range(0, 4):
        for dongu2 in range(0, 4):
            anahtar[dongu2 * 4 + dongu] = genisletilmis_anahtar[dongu2 + sayac + dongu * 4]
    return anahtar


# (3a5w6f7g) == 5w6f7g3a
def sol_dondur(kelime):
    return kelime[1:] + kelime[:1]


def alt_kume_duz(konumlar):
    global s_box
    for i in range(0, 16):
        konumlar[i] = s_box[konumlar[i]]
    return konumlar


def alt_kume_ters(konumlar):
    global inverted_s_box
    for i in range(0, 16):
        konumlar[i] = inverted_s_box[konumlar[i]]
    return konumlar


# ters turun 4 işlemini sırayla uygular
def aes_ters_turu(konumlar, anahtar):
    konumlar = satirlar_shift_ters(konumlar)
    konumlar = alt_kume_ters(konumlar)
    konumlar = anahtar_ekle(konumlar, anahtar)
    konumlar = sutunlar_galois(konumlar, True)
    return konumlar


def satirlar_shift_duz(konumlar):
    for i in range(0, 4):
        konumlar = satir_shift_ters(konumlar, i * 4, i)
    return konumlar


def satirlar_shift_ters(konumlar):
    for i in range(0, 4):
        konumlar = satir_shift_duz(konumlar, i * 4, i)
    return konumlar


def satir_shift_ters(konumlar, konum_gosterici, n):
    for i in range(0, n):
        konumlar[konum_gosterici:konum_gosterici + 4] = \
            konumlar[konum_gosterici + 3:konum_gosterici + 4] + \
            konumlar[konum_gosterici:konum_gosterici + 3]
    return konumlar


def satir_shift_duz(konumlar, konum_gosterici, n):
    for i in range(0, n):
        konumlar[konum_gosterici:konum_gosterici + 4] = \
            konumlar[konum_gosterici + 1:konum_gosterici + 4] + \
            konumlar[konum_gosterici:konum_gosterici + 1]
    return konumlar


def galois(x, y):
    h = 0
    for sayac in range(0, 8):
        if y & 1:
            h ^= x
        bit_kumesi = x & 0x80
        x <<= 1
        x &= 0xFF
        if bit_kumesi:
            x ^= 0x1b
        y >>= 1
    return h


# ileri aes operasyonları, her tur icin bir anahtar olusturma
def aes_main(konumlar, genisletilmis_anahtar, tur):
    konumlar = anahtar_ekle(konumlar, anahtar_olustur(genisletilmis_anahtar, 0))
    i = 1
    while True:
        if i >= tur:
            break
        konumlar = aes_turu(konumlar, anahtar_olustur(genisletilmis_anahtar, 16 * i))
        i += 1
    konumlar = alt_kume_duz(konumlar)
    konumlar = satirlar_shift_duz(konumlar)
    konumlar = anahtar_ekle(konumlar, anahtar_olustur(genisletilmis_anahtar, 16 * tur))
    return konumlar


# ters aes işlemleri
def aes_ters_main(konumlar, genisletilmis_anahtar, tur):
    konumlar = anahtar_ekle(konumlar, anahtar_olustur(genisletilmis_anahtar, 16 * tur))
    i = tur - 1
    while i > 0:
        konumlar = aes_ters_turu(konumlar, anahtar_olustur(genisletilmis_anahtar, 16 * i))
        i -= 1
    konumlar = satirlar_shift_ters(konumlar)
    konumlar = alt_kume_ters(konumlar)
    konumlar = anahtar_ekle(konumlar, anahtar_olustur(genisletilmis_anahtar, 0))
    return konumlar


def ozut(kelime, sayac):
    global s_box
    # 32 bitlik kelimeyi 8 bit dondur
    # 32 bit kelimenin 4 parçasının tümüne S-Box uygula
    # XOR uygula
    kelime = sol_dondur(kelime)
    for i in range(0, 4):
        kelime[i] = s_box[kelime[i]]
    kelime[0] = kelime[0] ^ r_con[sayac]
    return kelime


# 4x4 matrisinin galois carpimi
def sutunlar_galois(konumlar, ters):
    for i in range(0, 4):
        sutun = konumlar[i:i + 16:4]
        sutun = sutun_galois(sutun, ters)
        konumlar[i:i + 16:4] = sutun
    return konumlar


# 4x4 matrisinin 1 sütununun galois çarpımı
def sutun_galois(sutun, ters):
    if ters:
        dizi = [14, 9, 13, 11]
    else:
        dizi = [2, 1, 1, 3]
    yedek_dizi = list(sutun)
    sutun = sutun_galois_devam(yedek_dizi, dizi, sutun)
    return sutun


def sutun_galois_devam(yedek_dizi, dizi, sutun):
    sifir_sifir = galois(yedek_dizi[0], dizi[0])
    sifir_bir = galois(yedek_dizi[0], dizi[1])
    sifir_iki = galois(yedek_dizi[0], dizi[2])
    sifir_uc = galois(yedek_dizi[0], dizi[3])
    bir_sifir = galois(yedek_dizi[1], dizi[0])
    bir_bir = galois(yedek_dizi[1], dizi[1])
    bir_iki = galois(yedek_dizi[1], dizi[2])
    bir_uc = galois(yedek_dizi[1], dizi[3])
    iki_sifir = galois(yedek_dizi[2], dizi[0])
    iki_bir = galois(yedek_dizi[2], dizi[1])
    iki_iki = galois(yedek_dizi[2], dizi[2])
    iki_uc = galois(yedek_dizi[2], dizi[3])
    uc_sifir = galois(yedek_dizi[3], dizi[0])
    uc_bir = galois(yedek_dizi[3], dizi[1])
    uc_iki = galois(yedek_dizi[3], dizi[2])
    uc_uc = galois(yedek_dizi[3], dizi[3])
    sutun[0] = sifir_sifir ^ uc_bir ^ iki_iki ^ bir_uc
    sutun[1] = bir_sifir ^ sifir_bir ^ uc_iki ^ iki_uc
    sutun[2] = iki_sifir ^ bir_bir ^ sifir_iki ^ uc_uc
    sutun[3] = uc_sifir ^ iki_bir ^ bir_iki ^ sifir_uc
    return sutun


def anahtar_ekle(konumlar, anahtar):
    for i in range(0, 16):
        konumlar[i] ^= anahtar[i]
    return konumlar


def encrypt_decrypt(giris, anahtar, ters_duz):
    n_tur = 10
    genis_yeni_boyut = 16 * (n_tur + 1)
    blok = blok_doldur(giris)
    genis_anahtar = anahtar_genisletimi(anahtar, genis_yeni_boyut)
    # genis_anahtar kullanarak blok sifreleme
    blok = blok_turla(blok, genis_anahtar, n_tur, ters_duz)
    # blgğu tekrar çıktıya esitle ve dondur
    return cikis_esitle(blok)


def blok_doldur(giris):
    blok = [0] * 16
    for i in range(0, 4):
        for j in range(0, 4):
            blok[(i + (j * 4))] = giris[(i * 4) + j]
    return blok


def blok_turla(blok, genis_anahtar, n_tur, ters_duz):
    if ters_duz:
        blok = aes_main(blok, genis_anahtar, n_tur)
    else:
        blok = aes_ters_main(blok, genis_anahtar, n_tur)
    return blok


def cikis_esitle(blok):
    cikis = [0] * 16
    for i in range(0, 4):
        for j in range(0, 4):
            cikis[(i * 4) + j] = blok[(i + (j * 4))]
    return cikis


modlar = dict(OFB=0, CBC=1)
yapilacak_mod = "CBC"
sifreleme_anahtari = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
giris_vektoru = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]


# karakter dizisini sayi dizisine cevirir
def ceviri(giris, sifir, son, mod):
    global modlar
    dizi, sifir, son = duzenle(sifir, son, mod)
    return ceviri_sonucu(giris, sifir, son, dizi)


def ceviri_sonucu(giris, basla, bitir, dizi):
    i = basla
    j = 0
    while len(dizi) < bitir - basla:
        dizi.append(0)
    while i < bitir:
        dizi[j] = ord(giris[i])
        j += 1
        i += 1
    return dizi


def dosya_sifreleme(giris_byte):
    global son_sifre, sifreleme_anahtari, giris_vektoru
    return encrypt(giris_byte, modlar.get("CBC"), sifreleme_anahtari, giris_vektoru)


def ozut_alma(giris_byte):
    global sifreleme_anahtari, giris_vektoru, son_sifre
    encrypt(giris_byte, modlar.get("CBC"), sifreleme_anahtari, giris_vektoru)
    hash_ = []
    for i in son_sifre:
        hash_.append(chr(i))
    return encrypt(hash_, modlar.get("OFB"), sifreleme_anahtari, giris_vektoru)


# ileri turun 4 islemini sırayla uygular
def aes_turu(konumlar, anahtar):
    konumlar = alt_kume_duz(konumlar)
    konumlar = satirlar_shift_duz(konumlar)
    konumlar = sutunlar_galois(konumlar, False)
    konumlar = anahtar_ekle(konumlar, anahtar)
    return konumlar


def dosyaya_byte_list_yazdirma(byte_list, dosya):
    for i in byte_list:
        dosya.write(i)


def int_dizi_ceviri_byte_dizi(dizi):
    byte_dizi = []
    for i in dizi:
        byte_dizi.append(bytes([i]))
    return byte_dizi


# dizi duzenler
def duzenle(basla, bitir, mod):
    global modlar
    if bitir - basla > 16:
        bitir = basla + 16
    if mod == modlar.get("CBC"):
        dizi = [0] * 16
        return dizi, basla, bitir
    else:
        dizi = []
        return dizi, basla, bitir


def decrypt(sifre_metni, gercek_uzunluk, mod, anahtar, IV):
    global modlar
    if len(anahtar) % 16:
        return None
    if len(IV) % 16:
        return None
    karakterler = []
    if sifre_metni is not None:
        karakterler = dec(sifre_metni, gercek_uzunluk, mod, anahtar, IV)
    return "".join(karakterler)


def dec(sifre_metni, gercek_uzunluk, mod, anahtar, IV):
    giris = []
    karakterler = []
    ilk_tur = True
    for j in range(int(math.ceil(float(len(sifre_metni)) / 16))):
        basla = j * 16
        bitir = j * 16 + 16
        if j * 16 + 16 > len(sifre_metni):
            bitir = len(sifre_metni)
        sifre_metni_sonucu = sifre_metni[basla:bitir]
        if mod == modlar.get("OFB"):
            giris, ilk_tur = dec_ofb(ilk_tur, anahtar, IV, giris,
                                     sifre_metni_sonucu, bitir - basla, karakterler)
        elif mod == modlar.get("CBC"):
            giris, ilk_tur, karakterler = dec_cbc(sifre_metni_sonucu,
                                                  anahtar, ilk_tur, IV,
                                                  gercek_uzunluk, bitir,
                                                  basla, giris, karakterler)
    return karakterler


def dec_ofb(ilk_tur, anahtar, IV, giris, sifre_metni_sonucu, sayac, karakterler):
    plaintext = [0] * 16
    if ilk_tur:
        cikis = encrypt_decrypt(IV, anahtar, True)
        ilk_tur = False
    else:
        cikis = encrypt_decrypt(giris, anahtar, True)
    for i in range(0, 16):
        if len(cikis) - 1 < i:
            plaintext[i] = 0 ^ sifre_metni_sonucu[i]
        elif len(sifre_metni_sonucu) - 1 < i:
            plaintext[i] = cikis[i] ^ 0
        elif len(cikis) - 1 < i and len(sifre_metni_sonucu) < i:
            plaintext[i] = 0 ^ 0
        else:
            plaintext[i] = cikis[i] ^ sifre_metni_sonucu[i]
    for k in range(sayac):
        karakterler.append(chr(plaintext[k]))
    return cikis, ilk_tur


def dec_cbc(sifre_metni_sonucu, anahtar, ilk_tur, IV, gercek_uzunluk, bitir, basla, giris, karakterler):
    plaintext = [0] * 16
    cikis = encrypt_decrypt(sifre_metni_sonucu, anahtar, False)
    for i in range(0, 16):
        if ilk_tur:
            plaintext[i] = IV[i] ^ cikis[i]
        else:
            plaintext[i] = giris[i] ^ cikis[i]
    ilk_tur = False
    if gercek_uzunluk is not None and gercek_uzunluk < bitir:
        for k in range(gercek_uzunluk - basla):
            karakterler.append(chr(plaintext[k]))
    else:
        for k in range(bitir - basla):
            karakterler.append(chr(plaintext[k]))
    return sifre_metni_sonucu, ilk_tur, karakterler


def dosya_okuma(dosya_ismi):
    giris_dosyasi = open(dosya_ismi, "rb")
    giris_byte = []
    byte = giris_dosyasi.read(1)
    while byte:
        giris_byte.append(byte)
        byte = giris_dosyasi.read(1)
    giris_dosyasi.close()
    return giris_byte


def dosyaya_ozutu_yazma(ozutu, dosya_ismi):
    ozutu = bytearray(ozutu)
    cikis_dosyasi = open(dosya_ismi, "ab+")
    cikis_dosyasi.write(ozutu)
    cikis_dosyasi.close()


def dosyaya_yeni_metin_ekleme(yeni_metin, eski_metin, dosya_ismi):
    yeni_metin = bytearray(yeni_metin)
    cikis_dosyasi = open(dosya_ismi, "wb")
    dosyaya_byte_list_yazdirma(eski_metin, cikis_dosyasi)
    cikis_dosyasi.write(yeni_metin)
    cikis_dosyasi.close()


def ozut_bul_dosyaya_ekle(dosya_ismi):
    giris_byte = dosya_okuma(dosya_ismi)
    ozutu = ozut_alma(giris_byte)
    print(ozutu)
    dosyaya_ozutu_yazma(ozutu, dosya_ismi)


def testA():
    global sifreleme_anahtari, giris_vektoru, yapilacak_mod
    print("------ TEST A ------")
    metin = "Bugun hava 35 derece."
    print(metin)
    sifreli_metin = encrypt(metin, modlar.get(yapilacak_mod), sifreleme_anahtari, giris_vektoru)
    print(sifreli_metin)
    print(decrypt(sifreli_metin, len(metin), modlar.get(yapilacak_mod), sifreleme_anahtari, giris_vektoru))
    print("------ TEST A ------")


def testB():
    global sifreleme_anahtari, giris_vektoru, yapilacak_mod
    print("------ TEST B ------")
    metin = "Bugun hava 35 derece."
    print(metin)
    print("------ CBC Mod ------")
    yapilacak_mod = "CBC"
    sifreli_metin = encrypt(metin, modlar.get(yapilacak_mod), sifreleme_anahtari, giris_vektoru)
    print(sifreli_metin)
    print(decrypt(sifreli_metin, len(metin), modlar.get(yapilacak_mod), sifreleme_anahtari, giris_vektoru))
    print("------ OFB Mod ------")
    yapilacak_mod = "OFB"
    sifreli_metin = encrypt(metin, modlar.get(yapilacak_mod), sifreleme_anahtari, giris_vektoru)
    print(sifreli_metin)
    print(decrypt(sifreli_metin, len(metin), modlar.get(yapilacak_mod), sifreleme_anahtari, giris_vektoru))
    print("------ TEST B ------")


def testC(dosya_ismi):
    print("------ TEST C ------")
    print("dosya okumasi uzun surebilir lutfen kapatmayiniz")
    ozut_bul_dosyaya_ekle(dosya_ismi)
    print("------ TEST C ------")


def testD(dosya_ismi):
    print("------ TEST D ------")
    print("dosya okumasi uzun surebilir lutfen kapatmayiniz")
    giris_byte = dosya_okuma(dosya_ismi)
    ilk_ozutu = giris_byte[-16:]
    ilk_metin = giris_byte[:-16]
    ozutu = ozut_alma(ilk_metin)
    ozutu = int_dizi_ceviri_byte_dizi(ozutu)
    print(ilk_ozutu)
    print(ozutu)
    if ilk_ozutu == ozutu:
        print("ozutler uyusmaktadir dosya degisikligi yoktur")
    else:
        print("ozutler uyusmadi")
    yeni_metin = "\ndosyaya yeni yazilan metin"
    yeni_metin = list(map(ord, yeni_metin))
    dosyaya_yeni_metin_ekleme(yeni_metin, ilk_metin, dosya_ismi)
    ozut_bul_dosyaya_ekle(dosya_ismi)
    print("dosya okumasi uzun surebilir lutfen kapatmayiniz")
    dosya_byte = dosya_okuma(dosya_ismi)
    gecici_ozutu = dosya_byte[-16:]
    kalan_metin = dosya_byte[:-16]
    ozutu = ozut_alma(kalan_metin)
    ozutu = int_dizi_ceviri_byte_dizi(ozutu)
    print(gecici_ozutu)
    print(ozutu)
    if gecici_ozutu == ozutu:
        print("ozutler uyusmaktadir dosya baskasi tarafindan degismemistir")
        if gecici_ozutu == ilk_ozutu:
            print("ozutler uyusmaktadir dosya degisikligi yoktur")
        else:
            print("dosya degisikligi yaptik")
    else:
        print("ozutler uyusmadi baskasi tarafindan degismistir")
    print("dosya baskasi tarafindan degisiyor!!!!")
    yeni_metin = "\ndosyaya yeni yazilan metin"
    yeni_metin = list(map(ord, yeni_metin))
    dosyaya_yeni_metin_ekleme(yeni_metin, ilk_metin, dosya_ismi)
    print("dosya baskasi tarafindan degisildi!!!!")
    print("dosya okumasi uzun surebilir lutfen kapatmayiniz")
    dosya_byte = dosya_okuma(dosya_ismi)
    gecici_ozutu = dosya_byte[-16:]
    kalan_metin = dosya_byte[:-16]
    ozutu = ozut_alma(kalan_metin)
    ozutu = int_dizi_ceviri_byte_dizi(ozutu)
    print(gecici_ozutu)
    print(ozutu)
    if gecici_ozutu == ozutu:
        print("ozutler uyusmaktadir dosya baskasi tarafindan degismemistir")
        if gecici_ozutu == ilk_ozutu:
            print("ozutler uyusmaktadir dosya degisikligi yoktur")
        else:
            print("dosya degisikligi yaptik")
    else:
        print("ozutler uyusmadi baskasi tarafindan degismistir")
    print("------ TEST D ------")


if __name__ == "__main__":
    testA()
    testB()
    testC("deneme.txt")
    testD("deneme.txt")
