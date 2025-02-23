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