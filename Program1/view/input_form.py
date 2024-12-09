import tkinter as tk
from tkinter import messagebox
from data.mahasiswa import Mahasiswa

class InputForm:
    def __init__(self, master, data_mahasiswa):
        self.master = master
        self.master.title("Input Mahasiswa")
        self.data_mahasiswa = data_mahasiswa

        self._create_widgets()

    def _create_widgets(self):
        """Membuat input form untuk mahasiswa."""
        tk.Label(self.master, text="Nama:").pack(pady=5)
        self.entry_nama = tk.Entry(self.master)
        self.entry_nama.pack(pady=5)

        tk.Label(self.master, text="NIM:").pack(pady=5)
        self.entry_nim = tk.Entry(self.master)
        self.entry_nim.pack(pady=5)

        tk.Label(self.master, text="Jurusan:").pack(pady=5)
        self.entry_jurusan = tk.Entry(self.master)
        self.entry_jurusan.pack(pady=5)

        self.button_submit = tk.Button(self.master, text="Tambah Mahasiswa", command=self.tambah_mahasiswa)
        self.button_submit.pack(pady=10)

    def tambah_mahasiswa(self):
        """Menambahkan mahasiswa baru ke daftar."""
        nama = self.entry_nama.get().strip()
        nim = self.entry_nim.get().strip()
        jurusan = self.entry_jurusan.get().strip()

        if not nama or not nim or not jurusan:
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return

        # Validasi NIM agar unik
        if self.data_mahasiswa.cari_mahasiswa(nim):
            messagebox.showwarning("Peringatan", "Mahasiswa dengan NIM ini sudah ada!")
            return

        mahasiswa = Mahasiswa(nama, nim, jurusan)
        self.data_mahasiswa.tambah_mahasiswa(mahasiswa)
        messagebox.showinfo("Info", "Mahasiswa berhasil ditambahkan!")
        self.master.destroy()
