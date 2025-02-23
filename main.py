import os
import sys
import tarfile
from datetime import datetime

def baca_path_dari_file(nama_file):
    path_list = []
    
    try:
        with open(nama_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                path = line.strip()
                if os.path.exists(path):
                    path_list.append(path)
                else:
                    print(f"[WARNING] Path tidak ditemukan: {path}")
    except FileNotFoundError:
        print(f"[ERROR] File tidak ditemukan: {nama_file}")
        sys.exit(1)
    
    return path_list

def pilih_lokasi_backup():
    print("\nMasukkan path tujuan backup:")
    backup_location = input("> ")
    
    if not os.path.exists(backup_location):
        print("[INFO] Lokasi tujuan tidak ada, membuat folder...")
        os.makedirs(backup_location)
    
    return backup_location

def buat_backup(source_paths, backup_location):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"backup_{timestamp}.tar.gz"
    backup_filepath = os.path.join(backup_location, backup_filename)

    with tarfile.open(backup_filepath, "w:gz") as tar:
        for path in source_paths:
            if os.path.isfile(path):
                print(f"[INFO] Menambahkan file: {path}")
                tar.add(path, arcname=os.path.basename(path))
            elif os.path.isdir(path):
                print(f"[INFO] Menambahkan folder: {path}")
                folder_name = os.path.basename(path.rstrip('/'))
                tar.add(path, arcname=folder_name)
    
    print(f"\n[SUCCESS] Backup selesai! Hasil backup: {backup_filepath}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 backup.py namafile.txt")
        sys.exit(1)
    
    nama_file = sys.argv[1]
    print("=== Tool Backup Folder dan File ===")
    
    source_paths = baca_path_dari_file(nama_file)
    
    if not source_paths:
        print("[ERROR] Tidak ada path valid yang dibaca dari file.")
        return
    
    backup_location = pilih_lokasi_backup()
    buat_backup(source_paths, backup_location)

if __name__ == "__main__":
    main()
