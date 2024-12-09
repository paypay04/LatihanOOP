import tkinter as tk
from tkinter import messagebox

class MahasiswaView:
    def __init__(self, master, data_mahasiswa):
        self.master = master
        self.master.title("Daftar Mahasiswa")
        self.data_mahasiswa = data_mahasiswa

        self._create_widgets()
        self.tampilkan_data()

    def _create_widgets(self):
        """Membuat daftar mahasiswa, tombol pengelolaan, pencarian, dan keluar."""
        tk.Label(self.master, text="Daftar Mahasiswa").pack()

        # Komponen pencarian
        tk.Label(self.master, text="Cari Mahasiswa (Nama atau NIM):").pack(pady=5)
        self.entry_cari = tk.Entry(self.master)
        self.entry_cari.pack(pady=5)
        self.button_cari = tk.Button(self.master, text="Cari", command=self.cari_data)
        self.button_cari.pack(pady=5)

        # Listbox untuk menampilkan data
        self.listbox_mahasiswa = tk.Listbox(self.master, width=50)
        self.listbox_mahasiswa.pack()

        # Tombol pengelolaan data
        self.button_refresh = tk.Button(self.master, text="Refresh Data", command=self.tampilkan_data)
        self.button_refresh.pack(pady=5)

        self.button_hapus = tk.Button(self.master, text="Hapus Data", command=self.hapus_data)
        self.button_hapus.pack(pady=5)

        self.button_ubah = tk.Button(self.master, text="Ubah Data", command=self.ubah_data)
        self.button_ubah.pack(pady=5)

        # Tombol keluar
        self.button_keluar = tk.Button(self.master, text="Keluar", command=self.keluar)
        self.button_keluar.pack(pady=10)

    def tampilkan_data(self):
        """Menampilkan semua data mahasiswa di listbox."""
        self.listbox_mahasiswa.delete(0, tk.END)
        for mahasiswa in self.data_mahasiswa.get_mahasiswa_list():
            self.listbox_mahasiswa.insert(tk.END, f"{mahasiswa.nama} - {mahasiswa.nim} - {mahasiswa.jurusan}")

    def hapus_data(self):
        """Menghapus mahasiswa yang dipilih."""
        try:
            selected_index = self.listbox_mahasiswa.curselection()[0]
            selected_item = self.listbox_mahasiswa.get(selected_index)
            nim = selected_item.split(" - ")[1]
            if self.data_mahasiswa.hapus_mahasiswa(nim):
                messagebox.showinfo("Info", "Mahasiswa berhasil dihapus!")
                self.tampilkan_data()
            else:
                messagebox.showwarning("Peringatan", "Mahasiswa tidak ditemukan!")
        except IndexError:
            messagebox.showwarning("Peringatan", "Pilih mahasiswa yang ingin dihapus terlebih dahulu!")

    def ubah_data(self):
        """Mengubah data mahasiswa yang dipilih."""
        try:
            selected_index = self.listbox_mahasiswa.curselection()[0]
            selected_item = self.listbox_mahasiswa.get(selected_index)
            nim = selected_item.split(" - ")[1]  # Mendapatkan NIM dari string yang dipilih

            # Membuka jendela baru untuk ubah data
            self.ubah_window = tk.Toplevel(self.master)
            self.ubah_window.title("Ubah Data Mahasiswa")

            tk.Label(self.ubah_window, text="Nama Baru:").pack(pady=5)
            self.entry_nama = tk.Entry(self.ubah_window)
            self.entry_nama.pack(pady=5)

            tk.Label(self.ubah_window, text="Jurusan Baru:").pack(pady=5)
            self.entry_jurusan = tk.Entry(self.ubah_window)
            self.entry_jurusan.pack(pady=5)

            # Tombol untuk menyimpan perubahan
            self.button_simpan = tk.Button(self.ubah_window, text="Simpan Perubahan",
                                            command=lambda: self.simpan_perubahan(nim))
            self.button_simpan.pack(pady=10)

            # Mengisi field dengan data yang ada
            self.entry_nama.insert(0, selected_item.split(" - ")[0])
            self.entry_jurusan.insert(0, selected_item.split(" - ")[2])

        except IndexError:
            messagebox.showwarning("Peringatan", "Pilih mahasiswa yang ingin diubah terlebih dahulu!")

    def simpan_perubahan(self, nim):
        """Menyimpan perubahan data mahasiswa."""
        nama_baru = self.entry_nama.get().strip()
        jurusan_baru = self.entry_jurusan.get().strip()

        if not nama_baru or not jurusan_baru:
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return

        if self.data_mahasiswa.ubah_mahasiswa(nim, nama=nama_baru, jurusan=jurusan_baru):
            messagebox.showinfo("Info", "Data mahasiswa berhasil diubah!")
            self.tampilkan_data()
            self.ubah_window.destroy()
        else:
            messagebox.showwarning("Peringatan", "Mahasiswa tidak ditemukan!")

    def cari_data(self):
        """Mencari mahasiswa berdasarkan nama atau NIM."""
        keyword = self.entry_cari.get().strip().lower()
        if not keyword:
            messagebox.showwarning("Peringatan", "Masukkan kata kunci untuk mencari!")
            return

        hasil_cari = [
            mahasiswa for mahasiswa in self.data_mahasiswa.get_mahasiswa_list()
            if keyword in mahasiswa.nama.lower() or keyword in mahasiswa.nim
        ]

        self.listbox_mahasiswa.delete(0, tk.END)
        if hasil_cari:
            for mahasiswa in hasil_cari:
                self.listbox_mahasiswa.insert(tk.END, f"{mahasiswa.nama} - {mahasiswa.nim} - {mahasiswa.jurusan}")
        else:
            messagebox.showinfo("Info", "Tidak ada mahasiswa yang cocok dengan kata kunci pencarian.")

    def keluar(self):
        """Menutup aplikasi."""
        self.master.destroy()
