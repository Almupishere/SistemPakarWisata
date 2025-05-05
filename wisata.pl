% Fakta: wisata(Nama, Lokasi, Jenis, Harga, Kegiatan)
wisata(pantai_sanur, bali, pantai, murah, berenang).
wisata(gunung_bromo, jawa_timur, pegunungan, sedang, mendaki).
wisata(danau_toba, sumatera_utara, danau, murah, naik_perahu).
wisata(candi_borobudur, jawa_tengah, sejarah, sedang, belajar).
wisata(trans_studio, bandung, hiburan, mahal, bermain).
wisata(kawah_putih, ciwidey, pegunungan, murah, foto).
wisata(monumen_nasional, jakarta, sejarah, murah, belajar).
wisata(pantai_parangtritis, yogyakarta, pantai, murah, berenang).

% Aturan: rekomendasi(Nama, Jenis, Harga, Kegiatan)
rekomendasi(Nama, Jenis, Harga, Kegiatan) :-
    wisata(Nama, _, Jenis, Harga, Kegiatan).
