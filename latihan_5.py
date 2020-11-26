kontak = {"Ari": "085215565501", "Dina": "08788767778"}
print("Daftar Kontak")
print("Nama | Nomor Telepon")
print(kontak)

print("\nKontak Ari")
print(kontak['Ari'])

print("\nMenambahkan kontak baru dengan nama Riko - 087654544")
kontak['Riko'] = '087654544'
print(kontak['Riko'])

print("\nMerubah kontak Dina dengan nomor baru 088999776")
kontak['Dina'] = '088999776'
print(kontak['Dina'])

print("\nNama - Nama pada kontak")
print(kontak.keys())

print("\nNomor - Nomor pada kontak")
print(kontak.values())

print("\nDaftar Kontak")
print(kontak.items())

print("\nMenghapus kontak Dina")
del kontak['Dina']
print(kontak)
