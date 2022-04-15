def ekstrasi_data():
    """
    Tanggal: 15 April 2022
    Waktu: 18:27:29 WIB
    Magnitudo: 4.6
    Kedalaman: 48 km
    Lokasi: LU=4.04 BT=95.83
    Pusat gempa: Pusat gempa berada di laut 34 km Barat Daya Meulaboh
    Dirasakan: Dirasakan (Skala MMI): III Takengon, II Sigli Pidie
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '15 April 2022'
    hasil['waktu'] = '18:27:29 WIB'
    hasil['magnitudo'] = 4.6
    hasil['lokasi'] = {'lu': 4.04, 'bt': 95.83}
    hasil['pusat'] = 'Pusat gempa berada di laut 34 km Barat Daya Meulaboh'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): III Takengon, II Sigli Pidie'

    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi: LU={result['lokasi']['lu']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")

# if __name__ == '__main__':
#     print('Ini adalah package gempa terkini')