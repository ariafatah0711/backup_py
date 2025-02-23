# backup
```bash
sudo python3 main.py list_path.txt
```

# extract
```bash
tar -xvf namafile.tar.gz -C /path/tujuan/
sudo chown -R user:group /path/tujuan/

tar --no-same-owner -xvf namafile.tar.gz -C /path/tujuan/
```

# split tar.gz if u want put in vfat or fat32
```bash
split -b 1G namafile.tar.gz bagian_
```

# menggabungkan kembali
```bash
cat bagian_* > namafile.tar.gz
# Atau, bisa juga pakai tar langsung saat split:
tar -czvf - namafolder/ | split -b 1G - bagian_

# Untuk ekstrak setelah digabungkan:
tar -xzvf namafile.tar.gz
```