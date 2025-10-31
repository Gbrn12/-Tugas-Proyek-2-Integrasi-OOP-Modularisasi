class Penilaian:
    """Kelas untuk mengelola nilai akademik mahasiswa"""
    
    def __init__(self):
        self._quiz = 0.0
        self._tugas = 0.0
        self._uts = 0.0
        self._uas = 0.0
    
    def _validate_nilai(self, value):
        """Validasi nilai antara 0-100"""
        if not (0 <= value <= 100):
            raise ValueError("Nilai harus antara 0-100")
        return value
    
    @property
    def quiz(self):
        return self._quiz
    
    @quiz.setter
    def quiz(self, value):
        self._quiz = self._validate_nilai(value)
    
    @property
    def tugas(self):
        return self._tugas
    
    @tugas.setter
    def tugas(self, value):
        self._tugas = self._validate_nilai(value)
    
    @property
    def uts(self):
        return self._uts
    
    @uts.setter
    def uts(self, value):
        self._uts = self._validate_nilai(value)
    
    @property
    def uas(self):
        return self._uas
    
    @uas.setter
    def uas(self, value):
        self._uas = self._validate_nilai(value)
    
    def nilai_akhir(self):
        """Menghitung nilai akhir dengan bobot"""
        return (self.quiz * 0.15 + 
                self.tugas * 0.25 + 
                self.uts * 0.25 + 
                self.uas * 0.35)