from tracker.mahasiswa import Mahasiswa
from tracker.penilaian import Penilaian


class RekapKelas:
    """Kelas untuk mengelola rekap data seluruh mahasiswa"""
    
    def __init__(self):
        self.data_mahasiswa = {}
    
    def tambah_mahasiswa(self, nim, nama):
        """Menambahkan mahasiswa baru ke sistem"""
        if nim in self.data_mahasiswa:
            raise ValueError(f"Mahasiswa dengan NIM {nim} sudah terdaftar")
        
        mahasiswa_baru = Mahasiswa(nim, nama)
        penilaian_baru = Penilaian()
        
        self.data_mahasiswa[nim] = {
            'mhs': mahasiswa_baru,
            'nilai': penilaian_baru
        }
    
    def set_hadir(self, nim, persentase):
        """Mengatur persentase kehadiran mahasiswa"""
        if nim not in self.data_mahasiswa:
            raise ValueError(f"Mahasiswa dengan NIM {nim} tidak ditemukan")
        
        self.data_mahasiswa[nim]['mhs'].hadir_persen = persentase
    
    def set_penilaian(self, nim, quiz, tugas, uts, uas):
        """Mengatur nilai akademik mahasiswa"""
        if nim not in self.data_mahasiswa:
            raise ValueError(f"Mahasiswa dengan NIM {nim} tidak ditemukan")
        
        nilai_obj = self.data_mahasiswa[nim]['nilai']
        nilai_obj.quiz = quiz
        nilai_obj.tugas = tugas
        nilai_obj.uts = uts
        nilai_obj.uas = uas
    
    def predikat(self, nilai_akhir):
        """Menentukan predikat berdasarkan nilai akhir"""
        if nilai_akhir >= 80:
            return 'A'
        elif nilai_akhir >= 70:
            return 'B'
        elif nilai_akhir >= 60:
            return 'C'
        elif nilai_akhir >= 50:
            return 'D'
        else:
            return 'E'
    
    def rekap(self):
        """Generate rekap data semua mahasiswa"""
        records = []
        for nim, data in self.data_mahasiswa.items():
            mhs = data['mhs']
            nilai_obj = data['nilai']
            nilai_akhir = nilai_obj.nilai_akhir()
            predikat = self.predikat(nilai_akhir)
            
            records.append({
                'nim': mhs.nim,
                'nama': mhs.nama,
                'hadir_persen': mhs.hadir_persen,
                'nilai_akhir': nilai_akhir,
                'predikat': predikat
            })
        
        return records
    
    def filter_nilai_rendah(self, batas=70):
        """Bonus: Filter mahasiswa dengan nilai di bawah batas tertentu"""
        semua_rekap = self.rekap()
        return [record for record in semua_rekap if record['nilai_akhir'] < batas]