#!/usr/bin/env python3
"""
Aplikasi Student Performance Tracker
"""

import os
from tracker import RekapKelas, build_markdown_report, save_text

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_menu():
    """Menampilkan menu utama"""
    print("\n" + "="*40)
    print("    Student Performance Tracker")
    print("="*40)
    print("1) Muat data dari CSV")
    print("2) Tambah mahasiswa")
    print("3) Ubah presensi")
    print("4) Ubah nilai")
    print("5) Lihat rekap")
    print("6) Simpan laporan Markdown")
    print("7) Tampilkan nilai rendah (<70)")
    print("8) Keluar")
    print("="*40)

def input_angka(prompt, min_val=None, max_val=None):
    """Helper untuk input angka dengan validasi"""
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Nilai tidak boleh kurang dari {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Nilai tidak boleh lebih dari {max_val}")
                continue
            return value
        except ValueError:
            print("Harap masukkan angka yang valid!")

def main():
    rekap_kelas = RekapKelas()
    
    # Data contoh untuk testing
    rekap_kelas.tambah_mahasiswa("230101001", "Ana")
    rekap_kelas.set_hadir("230101001", 92.0)
    rekap_kelas.set_penilaian("230101001", 85, 90, 88, 92)
    
    rekap_kelas.tambah_mahasiswa("230101002", "Bimo")
    rekap_kelas.set_hadir("230101002", 60.0)
    rekap_kelas.set_penilaian("230101002", 55, 60, 65, 70)
    
    while True:
        clear_screen()
        tampilkan_menu()
        
        pilihan = input("\nPilih menu (1-8): ").strip()
        
        if pilihan == '1':
            print("\nFitur muat CSV akan diimplementasikan di sini...")
            input("Tekan Enter untuk melanjutkan...")
            
        elif pilihan == '2':
            print("\n--- Tambah Mahasiswa Baru ---")
            nim = input("NIM: ").strip()
            nama = input("Nama: ").strip()
            
            try:
                rekap_kelas.tambah_mahasiswa(nim, nama)
                print(f"✓ Mahasiswa {nama} berhasil ditambahkan!")
            except ValueError as e:
                print(f"✗ Error: {e}")
            input("Tekan Enter untuk melanjutkan...")
            
        elif pilihan == '3':
            print("\n--- Ubah Presensi ---")
            nim = input("NIM: ").strip()
            hadir = input_angka("Persentase kehadiran (0-100): ", 0, 100)
            
            try:
                rekap_kelas.set_hadir(nim, hadir)
                print("✓ Presensi berhasil diupdate!")
            except ValueError as e:
                print(f"✗ Error: {e}")
            input("Tekan Enter untuk melanjutkan...")
            
        elif pilihan == '4':
            print("\n--- Ubah Nilai ---")
            nim = input("NIM: ").strip()
            quiz = input_angka("Nilai Quiz (0-100): ", 0, 100)
            tugas = input_angka("Nilai Tugas (0-100): ", 0, 100)
            uts = input_angka("Nilai UTS (0-100): ", 0, 100)
            uas = input_angka("Nilai UAS (0-100): ", 0, 100)
            
            try:
                rekap_kelas.set_penilaian(nim, quiz, tugas, uts, uas)
                print("✓ Nilai berhasil diupdate!")
            except ValueError as e:
                print(f"✗ Error: {e}")
            input("Tekan Enter untuk melanjutkan...")
            
        elif pilihan == '5':
            print("\n--- Rekap Kelas ---")
            records = rekap_kelas.rekap()
            
            if not records:
                print("Belum ada data mahasiswa.")
            else:
                print("\n{:<12} {:<15} {:<10} {:<12} {:<8}".format(
                    "NIM", "Nama", "Hadir(%)", "Nilai Akhir", "Predikat"))
                print("-" * 65)
                
                for record in records:
                    print("{:<12} {:<15} {:<10.1f} {:<12.2f} {:<8}".format(
                        record['nim'], record['nama'], record['hadir_persen'],
                        record['nilai_akhir'], record['predikat']))
            input("\nTekan Enter untuk melanjutkan...")
            
        elif pilihan == '6':
            print("\n--- Simpan Laporan Markdown ---")
            records = rekap_kelas.rekap()
            
            if not records:
                print("Belum ada data untuk dibuat laporan.")
            else:
                # Pastikan folder out exists
                os.makedirs('out', exist_ok=True)
                
                markdown_content = build_markdown_report(records)
                save_text('out/report.md', markdown_content)
                print("✓ Laporan berhasil disimpan di 'out/report.md'")
                
                # Tampilkan preview
                print("\nPreview laporan:")
                print("-" * 50)
                print(markdown_content)
            input("\nTekan Enter untuk melanjutkan...")
            
        elif pilihan == '7':
            print("\n--- Mahasiswa dengan Nilai Rendah (<70) ---")
            nilai_rendah = rekap_kelas.filter_nilai_rendah()
            
            if not nilai_rendah:
                print("Tidak ada mahasiswa dengan nilai di bawah 70.")
            else:
                for record in nilai_rendah:
                    print(f"- {record['nama']} ({record['nim']}): {record['nilai_akhir']:.2f}")
            input("\nTekan Enter untuk melanjutkan...")
            
        elif pilihan == '8':
            print("\nTerima kasih telah menggunakan Student Performance Tracker!")
            break
            
        else:
            print("\nPilihan tidak valid! Silakan pilih 1-8.")
            input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()