import math
import datetime
import os

while True:
    
    current_time = datetime.datetime.now()

    def my_banner():
        print("+================================================================================================================+")
        print("---------------------------------------------------WAKTU SOLAT----------------------------------------------------")
        print("----------------------------------------------------MALAYSIA------------------------------------------------------")
        print("-------------------------------------Dibina oleh : AHMAD FAIZ BIN IBRAHIM-----------------------------------------")
        print("----------------------------------------------Pada 6 Februari 2023------------------------------------------------")
        print("---------------------------------------Assalamuaikum dan selamat datang-------------------------------------------")
        print("---------------------------------------------" + str(current_time) + "---------------------------------------------")
        print("+================================================================================================================+\n\n")
        return

    my_banner()

    num = int(input('Sila pilih negeri anda: \n\n1.  PERLIS\n2.  KEDAH\n3.  PULAU PINANG\n4.  PERAK\n5.  SELANGOR\n6.  WILAYAH PERSEKUTUAN\n7.  NEGERI SEMBILAN\n8.  MELAKA\n9.  JOHOR\n10. PAHANG\n11. KELANTAN\n12. TERENGGANU\n13. SABAH\n14. SARAWAK\n\nPilihan :'))

    os.system('cls' if os.name=='nt' else 'clear')

    my_banner()

    print("\nSenarai Latitude dan Longitude bagi setiap zon :\n")

    if num == 1:
        print("\nPERLIS\nZon 1 : Kangar, Padang Besar dan Arau\n")
        
    elif num == 2:
        print("\nKEDAH\n\nZon 2 : Daerah-daerah Kubang Pasu, Kota Setar, Pendang, Kulim, Bandar Bharu, Kuala Muda dan Yan\n\nZon 3 : Daerah-daerah Baling, Sik dan Padang Terap\n\nZon 4 : Daerah Langkawi\n\nZon 5 : Gunung Jerai\n")

    elif num == 3:
        print("\nPULAU PINANG\n\nZon 6 : Georgetown, Balik Pulau, Bukit Mertajam, Butterworth, Kepala Batas dan Nibong Tebal\n\nZon 7 : Bukit Bendera\n")

    elif num == 4:
        print("\nPERAK\n\nZon 8 : Daerah Hulu Perak, Kuala Kangsar,  Kinta dan  Batang Padang\n\nZon 9 : Daerah Kerian, Larut Matang dan Selama, Perak Tengah, Hilir Perak dan Manjong\n\nZon 10 : Bukit Larut\n") 

    elif num == 5:
        print("\nSELANGOR\n\nZon 11 : Daerah Hulu Selangor, Rawang, Hulu Langat, Sepang, Petaling dan Shah Alam\n\nZon 12 : Sabak Bernam, Kuala Selangor, Klang dan Kuala Langat\n")

    elif num == 6:
        print("\nWILAYAH PERSEKUTUAN\n\nZon 13 : Kuala Lumpur dan Putrajaya\n\nZon 14 : Labuan")

    elif num == 7:
        print("\nNEGERI SEMBILAN\n\nZon 15 : Daerah Jempol dan Tampin\n\nZon 16 : Daerah Port Dickson, Seremban, Kuala Pilah, Jelebu dan Rembau\n")
        
    elif num == 8:
        print("\nMELAKA\n\nZon 17 : Bandar Melaka, Alor Gajah, Jasin, Masjid Tanah, Merlimau dan Nyalas\n")

    elif num == 9:
        print("\nJOHOR\n\nZon 18 : Pulau Aur dan Pemanggil\n\nZon 19 : Kota Tinggi, Mersing dan Johor Bahru\n\nZon 20 : Kluang dan Pontian\n\nZon 20 : Batu Pahat, Muar, Segamat dan Gemas Johor")

    elif num == 10:
        print("\nPAHANG\n\nZon 22 : Pulau Tioman\n\nZon 23 : Kuantan, Pekan, Rompin dan Muadzam Shah\n\nZon 24 : Maran, Chenor, Temerloh, Bera dan Jerantut\n\nZon 25 : Bentong, Raub dan Lipis\n\nZon 26 : Bukit Fraser, Genting Highlands dan Bukit Tinggi\n\nZon 27 : Cameron Highlands\n")

    elif num == 11:
        print("\nKELANTAN\n\nZon 28 : Jajahan Kota Bharu, Bachok, Pasir Puteh, Tumpat, Pasir Mas, Tanah Merah, Machang,\nKuala Krai dan Daerah Chiku (Jajahan Gua Musang)\n\nZon 29 : Jajahan Jeli dan Gua Musang termasuk Daerah Galas dan Bertam\n")

    elif num == 12:
        print("\nTERENGGANU\n\nZon 30 : Daerah Kuala Terengganu dan Marang\n\nZon 31 : Daerah Besut dan Setiu\n\nZon 32 : Daerah Hulu Terengganu\n\nZon 33 : Daerah Dungun dan Kemaman\n")

    elif num == 13:
        print("\nSABAH")
        print("Zon 34 : Bandar Sandakan, Bukit Garam, Semawang, Temanggong dan Tambisan")
        print("")
        print("Zon 35 : Pinangah, Terusan, Beluran, Kuamut dan Telupid")
        print("")
        print("Zon 36 : Lahad Datu, Kunak, Silabukan, Tungku, Sahabat dan Semporna")
        print("")
        print("Zon 37 : Bandar Tawau, Balong, Merotai dan Kalabakan")
        print("")
        print("Zon 38 :. Kudat, Kota Marudu, Pitas dan Pulau Banggi")
        print("")
        print("Zon 39 : Gunung Kinabalu")
        print("")
        print("Zon 40 : Kota Kinabalu, Penampang, Tuaran, Papar, Kota Belud dan Ranau")
        print("")
        print("Zon 41 : Pensiangan, Keningau, Tambunan dan Nabawan")
        print("")
        print("Zon 42 : Sipitang, Membakut, Beaufort, Kuala Penyu, Weston, Tenom dan Long Pa Sia")
        print("")

    elif num == 14:
        print("\nSARAWAK")
        print("Zon 43 : Limbang, Sundar, Trusan dan Lawas")
        print("")
        print("Zon 44 : Niah, Belaga, Sibuti, Miri, Bekenu dan Marudi")
        print("")
        print("Zon 45 : Song, Belingian, Sebauh, Bintulu, Tatau dan Kapit")
        print("")
        print("Zon 46 : Igan, Kanowit, Sibu, Dalat dan Oya")
        print("")
        print("Zon 47 : Belawai, Matu, Daro, Sarikei, Julau, Bintangor dan Rajang")
        print("")
        print("Zon 48 : Kabong, Lingga, Sri Aman, Engkelili, Betong, Spaoh, Pusa, Saratok, Roban dan Debak")
        print("")
        print("Zon 49 : Kota Samarahan")
        print("")
        print("Zon 50 : Kuching, Bau, Lundu dan Sematan")
        print("")

    else :
        print("")

    zon = ["Perlis", "kd1", "kd2", "kd3", "kd4", "pp1", "pp2", "pr1", "pr2", "pr3", "Hulu Selangor", "Kuala Selangor", "wp1", "wp2", "ns1", "ns2", "Melaka", "jhr1", "jhr2", "jhr3", "jhr4", "ph1", "ph2", "ph3", "ph4", "ph5", "ph6", "kln1", "kln2", "tr1", "tr2", "tr3", "tr4", "sbh1", "sbh2", "sbh2", "sbh3", "sbh4", "sbh5", "sbh6", "sbh7", "sbh8", "sbh9", "srw1", "srw2", "srw3", "srw4", "srw5", "srw6", "srw7", "srw8"]
    longlat = {
    "Perlis": (6.4333333333333, 100.1833333333333, 0, 18), 
    "kd1": (6.2833333333333, 100.2166666666667, 0, 18), 
    "kd2": (6.25, 100.6166666666667, 0, 18), 
    "kd3": (6.3666666666667, 99.6833333333333, 0, 18), 
    "kd4": (5.7875212, 100.4251341, 1214, 18), 
    "pp1": (5.4166666666667, 100.2, 0, 18), 
    "pp2": (5.4167168, 100.2639766, 743, 18), 
    "pr1": (4.7666666666667, 100.9333333333333, 0, 18), 
    "pr2": (5.1333333333333, 100.4666666666667, 0, 18), 
    "pr3": (4.8666666666667, 100.8, 945, 18),
    "Hulu Selangor": (3.7333333333333, 3.7333333333333, 0, 18),
    "Kuala Selangor": (3.7666666666667, 100.8833333333333, 0, 18),
    "wp1": (3.7333333333333, 101.3833333333333, 0, 18), 
    "wp2": (5.2833333333333, 115.2333333333333, 0, 18), 
    "ns1": (2.9, 102.3166666666667, 0, 18), 
    "ns2": (2.5333333333333, 101.8, 0, 18), 
    "Melaka": (2.3833333333333, 101.9833333333333, 0, 18), 
    "jhr1": (2.5833333333333, 104.3166666666667, 0, 18), 
    "jhr2": (1.7166666666667, 103.5333333333333, 0, 18), 
    "jhr3": (1.65, 103.2, 0, 18), 
    "jhr4": (2.2666666666667, 102.5333333333333, 0, 18), 
    "ph1": (2.8, 104.15, 0, 18), 
    "ph2": (3.0833333333333, 102.7833333333333, 0, 18), 
    "ph3": (3.4666666666667, 102.1166666666667, 0, 18), 
    "ph4": (3.9833333333333, 101.7333333333333, 0, 18), 
    "ph5": (3.4333333333333, 101.8, 1700, 18), 
    "ph6": (4.5, 101.4, 1600, 18), 
    "kln1": (6.0166666666667, 101.9833333333333, 0, 17), 
    "kln2": (4.95, 101.5, 0, 17), 
    "tr1": (5.25, 102.9666666666667, 0, 18), 
    "tr2": (5.4166666666667, 102.4166666666667, 0, 18), 
    "tr3": (5.0, 102.5333333333333, 0, 18), 
    "tr4": (4.5, 102.8666666666667, 0, 18), 
    "sbh1": (5.5, 117.8, 0, 18), 
    "sbh2": (5.2166666666667, 116.8166666666667, 0, 18), 
    "sbh3": (5.0166666666667, 118.3333333333333, 0, 18), 
    "sbh4": (4.4166666666667, 117.5, 0, 18), 
    "sbh5": (6.8833333333333, 116.8333333333333, 0, 18), 
    "sbh6": (6.0833333333333, 116.5333333333333, 4101, 18), 
    "sbh7": (5.7333333333333, 115.9333333333333, 0, 18), 
    "sbh8": (5.3333333333333, 116.1666666666667, 0, 18), 
    "sbh9": (5.0833333333333, 115.55, 0, 18), 
    "srw1": (4.7833333333333, 114.8333333333333, 0, 18), 
    "srw2": (3.8833333333333, 113.7166666666667, 0, 18), 
    "srw3": (2.8833333333333, 112.8666666666667, 0, 18), 
    "srw4": (2.8333333333333, 111.7, 0, 18), 
    "srw5": (2.2333333333333, 111.2166666666667, 0, 18), 
    "srw6": (1.7833333333333, 111.1166666666667, 0, 18), 
    "srw7": (1.4666666666667, 110.4833333333333, 0, 18), 
    "srw8": (1.8166666666667, 109.7666666666667, 0, 18)
    }

    user_input_number = input("Sila pilih zon bagi kawasan anda(Contoh: 14) : ")

    selected_zone = zon[int(user_input_number) - 1]
    latitude, longitude, ketinggian, h_isyak = longlat[selected_zone]

    Latitude = float(latitude)
    Longitude = float(longitude)
    TT = int(ketinggian)
    hn_isyak = int(h_isyak)

    kerendahan_ufuk = (1.76 / 60) * (math.sqrt(TT))
    ref = 34/60
    sd = 16/60
    ho = - (1 + kerendahan_ufuk)

    z = math.radians(Latitude)

    current_datetime = datetime.datetime.now()

    Year = int(current_datetime.year)
    Month = int(current_datetime.month)
    Day = int(current_datetime.day)

    os.system('cls' if os.name=='nt' else 'clear')

    my_banner()
    
    Hour = 12
    Minute = 0
    Second = 0
    Zone = int(8)
    DST = 0

    def DY2k(Year,Month,Day,Hour,Zone):
        if Month  <= 2 :
            Year  = Year - 1
            Month = Month + 12
        AAAA      = int(Year / 100)
        BBBB      = 2 - AAAA + int(AAAA / 4)
        CCCC      = int(365.25 * Year)
        DDDD      = int(30.6001 * (Month + 1))
        JD        = BBBB + CCCC + DDDD + Day + (Hour-Zone)/24.- 730550.5
        return JD

    def EoT(Year,Month,Day,Hour,Minute,Second,Zone,DST):
        Days_since_Epoch  = DY2k(Year,Month,Day,Hour,Zone)
        Mean_Long_Sun_d   = (280.46 + 0.9856474  * Days_since_Epoch) % 360.
        Mean_Anomaly_d    = (357.528 + 0.9856003 * Days_since_Epoch) % 360.
        Mean_Anomaly_r    = math.radians(Mean_Anomaly_d)
        Ecliptic_Long_d   = Mean_Long_Sun_d + 1.915 *math.sin(Mean_Anomaly_r) + 0.020 * math.sin(2*Mean_Anomaly_r)
        Ecliptic_Long_r   = math.radians(Ecliptic_Long_d)
        Obliquity_d       = 23.439 - 0.0000004 * Days_since_Epoch
        Obliquity_r       = math.radians(Obliquity_d)
        Right_Ascension_r = math.atan2(math.cos(Obliquity_r) * math.sin(Ecliptic_Long_r),math.cos(Ecliptic_Long_r))
        Right_Ascension_d = (math.degrees(Right_Ascension_r)) % 360.
        Right_Ascension_h = Right_Ascension_d/15.
        
        Declination_r     = math.asin(math.sin(Obliquity_r) * math.sin(Ecliptic_Long_r))
        Declination_d     = math.degrees(Declination_r)
        
        EoT_d             = Mean_Long_Sun_d - Right_Ascension_d
        if EoT_d > 50 : EoT_d -= 360
        EoT_m             = -EoT_d * 4 # Gnomonical EoT
        return EoT_m

    def DoS(Year,Month,Day,Hour,Minute,Second,Zone,DST):
        Days_since_Epoch  = DY2k(Year,Month,Day,Hour,Zone)
        Mean_Long_Sun_d   = (280.46 + 0.9856474  * Days_since_Epoch) % 360.
        Mean_Anomaly_d    = (357.528 + 0.9856003 * Days_since_Epoch) % 360.
        Mean_Anomaly_r    = math.radians(Mean_Anomaly_d)
        Ecliptic_Long_d   = Mean_Long_Sun_d + 1.915 *math.sin(Mean_Anomaly_r) + 0.020 * math.sin(2*Mean_Anomaly_r)
        Ecliptic_Long_r   = math.radians(Ecliptic_Long_d)
        Obliquity_d       = 23.439 - 0.0000004 * Days_since_Epoch
        Obliquity_r       = math.radians(Obliquity_d)
        Right_Ascension_r = math.atan2(math.cos(Obliquity_r) * math.sin(Ecliptic_Long_r),math.cos(Ecliptic_Long_r))
        Right_Ascension_d = (math.degrees(Right_Ascension_r)) % 360.
        Right_Ascension_h = Right_Ascension_d/15.
        
        Declination_r     = math.asin(math.sin(Obliquity_r) * math.sin(Ecliptic_Long_r))
        return Declination_r

    DoS_r = DoS(Year,Month,Day,Hour,Minute,Second,Zone,DST)

    DoS_su = DoS(Year,Month,Day,5,Minute,Second,Zone,DST)
    DoS_sy = DoS(Year,Month,Day,6,Minute,Second,Zone,DST)
    DoS_a = DoS(Year,Month,Day,15,Minute,Second,Zone,DST)
    DoS_m = DoS(Year,Month,Day,18,Minute,Second,Zone,DST)
    DoS_i = DoS(Year,Month,Day,19,Minute,Second,Zone,DST)

    jd2 = EoT(Year,Month,Day,Hour,Minute,Second,Zone,DST)

    def decimal_to_hms(decimal):
        decimal = float(decimal)
        hours = int(decimal)
        minutes = int((decimal - hours) * 60)
        seconds = int((((decimal - hours) * 60) - minutes) * 60)
        return "{}:{}:{}".format(hours, minutes, seconds)

    h_Subuh = math.radians(-18 - kerendahan_ufuk)
    h_Syuruk = math.radians(ho)
    h_Asar = math.atan(1 / (1 + math.tan(abs((z - DoS_a)))))
    h_Maghrib = math.radians(ho)
    h_Isyak = math.radians(-hn_isyak - kerendahan_ufuk)

    t_Subuh = (math.degrees(math.acos((math.sin(h_Subuh) - (math.sin(DoS_su) * math.sin(z))) / (math.cos(DoS_su) * math.cos(z))))) / 15
    t_Syuruk = (math.degrees(math.acos((math.sin(h_Syuruk) - (math.sin(DoS_sy) * math.sin(z))) / (math.cos(DoS_sy) * math.cos(z))))) / 15
    t_Asar = (math.degrees(math.acos((math.sin(h_Asar) - (math.sin(DoS_a) * math.sin(z))) / (math.cos(DoS_a) * math.cos(z))))) / 15
    t_Maghrib = (math.degrees(math.acos((math.sin(h_Maghrib) - (math.sin(DoS_m) * math.sin(z))) / (math.cos(DoS_m) * math.cos(z))))) / 15
    t_Isyak = (math.degrees(math.acos((math.sin(h_Isyak) - (math.sin(DoS_i) * math.sin(z))) / (math.cos(DoS_i) * math.cos(z))))) / 15

    waktu_istiwa = (12 + (jd2/60)) + ((120 - Longitude)/15)
    waktu_zohor = waktu_istiwa + (2/60)
    waktu_subuh = waktu_istiwa - t_Subuh
    waktu_asar = waktu_istiwa + t_Asar
    waktu_syuruk = waktu_istiwa - t_Syuruk
    waktu_isyak = waktu_istiwa + t_Isyak
    waktu_maghrib = waktu_istiwa + t_Maghrib
    waktu_imsak = waktu_subuh - (10/60)

    print("Perata Waktu/Taadil Zamani : " + str(decimal_to_hms(jd2/60)) + "\n")
    print("Deklinasi Matahari/Mail asy-Syams : " + str(decimal_to_hms(math.degrees(DoS_r))) + "\n")

    print('Waktu Imsak : ' + str(decimal_to_hms(waktu_imsak)))
    print('Waktu Subuh : ' + str(decimal_to_hms(waktu_subuh)))
    print('Waktu Syuruk : ' + str(decimal_to_hms(waktu_syuruk)))
    print('Waktu Istiwa : ' + str(decimal_to_hms(waktu_istiwa)))
    print('Waktu Zohor : ' + str(decimal_to_hms(waktu_zohor)))
    print('Waktu Asar : ' + str(decimal_to_hms(waktu_asar)))
    print('Waktu Mahgrib : ' + str(decimal_to_hms(waktu_maghrib)))
    print('Waktu Isyak : ' + str(decimal_to_hms(waktu_isyak))) 

    repeat = input("\nInginkan waktu solat bagi zon yang lain? (y/n) ")

    if repeat.lower() == "n":
        break
