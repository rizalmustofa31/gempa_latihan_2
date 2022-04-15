"""
aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE

"""
import gempaterkini2


if __name__ == '__main__':
    print('Aplikasi Utama')
    result = gempaterkini2.ekstrasi_data()
    gempaterkini2.tampilkan_data(result)