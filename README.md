# Bahasa Pemograman Pertemuan 13

# LatihanOOP

# Pyhton 

```
import tkinter as tk
from view.input_form import InputForm
from view.mahasiswa import MahasiswaView
from data.mahasiswa import DataMahasiswa

class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikasi Data Mahasiswa")

        # Inisialisasi DataMahasiswa
        self.data_mahasiswa = DataMahasiswa()

        # Membuat tombol-tombol pada jendela utama
        self._create_widgets()

    def _create_widgets(self):
        """Membuat tombol utama aplikasi."""
        self.button_input = tk.Button(self.master, text="Input Mahasiswa", command=self.open_input_form)
        self.button_input.pack(pady=10)

        self.button_view = tk.Button(self.master, text="Lihat Daftar Mahasiswa", command=self.open_mahasiswa_view)
        self.button_view.pack(pady=10)

    def open_input_form(self):
        """Membuka form input di jendela baru."""
        self._open_new_window(InputForm)

    def open_mahasiswa_view(self):
        """Membuka daftar mahasiswa di jendela baru."""
        self._open_new_window(MahasiswaView)

    def _open_new_window(self, view_class):
        """Membantu membuka jendela baru dengan kelas tampilan tertentu."""
        new_window = tk.Toplevel(self.master)
        view_class(new_window, self.data_mahasiswa)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
```

# Hasil Pyhton

1. tampilan awal
![Screenshot (415)](https://github.com/user-attachments/assets/444ef14f-8e64-4392-94af-8f059b62aca9)

2. masukan data (nama, nim, jurusan)
![Screenshot (419)](https://github.com/user-attachments/assets/27605805-9f1f-414a-8360-0437a7faf44a)

3. ubah data salah satu data
![Screenshot (425)](https://github.com/user-attachments/assets/f183a786-8c5a-4a65-a38d-d95fb0d4669f)

4. hapus salah satu data
![Screenshot (427)](https://github.com/user-attachments/assets/33aff9a2-fdd3-48f8-96aa-ed9bc8f93906)

