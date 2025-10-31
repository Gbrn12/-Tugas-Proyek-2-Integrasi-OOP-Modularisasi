class Mahasiswa:
    """Kelas untuk merepresentasikan data mahasiswa"""
    
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self._hadir_persen = 0.0
    
    @property
    def hadir_persen(self):
        """Property untuk mendapatkan persentase kehadiran"""
        return self._hadir_persen
    
    @hadir_persen.setter
    def hadir_persen(self, value):
        """Setter dengan validasi persentase kehadiran"""
        if not (0 <= value <= 100):
            raise ValueError("Persentase kehadiran harus antara 0-100")
        self._hadir_persen = value
    
    def info(self):
        """Menampilkan informasi profil mahasiswa"""
        return f"{self.nim} - {self.nama} (Kehadiran: {self.hadir_persen}%)"