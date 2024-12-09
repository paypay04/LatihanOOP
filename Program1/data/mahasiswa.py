class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        if not nama or not nim or not jurusan:
            raise ValueError("Nama, NIM, dan jurusan tidak boleh kosong")
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def __str__(self):
        return f"Nama: {self.nama}\nNIM: {self.nim}\nJurusan: {self.jurusan}"


class DataMahasiswa:
    def __init__(self):
        self.mahasiswa_list = []

    def tambah_mahasiswa(self, mahasiswa):
        if any(m.nim == mahasiswa.nim for m in self.mahasiswa_list):
            raise ValueError("Mahasiswa dengan NIM ini sudah ada.")
        self.mahasiswa_list.append(mahasiswa)

    def hapus_mahasiswa(self, nim):
        for mahasiswa in self.mahasiswa_list:
            if mahasiswa.nim == nim:
                self.mahasiswa_list.remove(mahasiswa)
                return True
        return False

    def ubah_mahasiswa(self, nim, nama=None, jurusan=None):
        for mahasiswa in self.mahasiswa_list:
            if mahasiswa.nim == nim:
                if nama:
                    mahasiswa.nama = nama
                if jurusan:
                    mahasiswa.jurusan = jurusan
                return True
        return False

    def cari_mahasiswa(self, nim):
        for mahasiswa in self.mahasiswa_list:
            if mahasiswa.nim == nim:
                return mahasiswa
        return None

    def get_mahasiswa_list(self):
        return self.mahasiswa_list

    def get_mahasiswa_by_jurusan(self, jurusan):
        return [m for m in self.mahasiswa_list if m.jurusan == jurusan]

    def get_mahasiswa_by_nama(self, nama):
        return [m for m in self.mahasiswa_list if m.nama == nama]
