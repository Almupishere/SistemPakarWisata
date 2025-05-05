import tkinter as tk
from tkinter import ttk, messagebox
from pyswip import Prolog

# Inisialisasi Prolog
prolog = Prolog()
prolog.consult("wisata.pl")

def cari_rekomendasi():
    jenis = jenis_var.get()
    harga = harga_var.get()
    kegiatan = kegiatan_var.get()

    if not jenis or not harga or not kegiatan:
        messagebox.showwarning("Peringatan", "Semua pilihan harus diisi!")
        return

    query = f"rekomendasi(Nama, {jenis}, {harga}, {kegiatan})"
    hasil = list(prolog.query(query))

    if hasil:
        hasil_teks = "\n".join([str(item["Nama"]).replace('_', ' ').title() for item in hasil])
        hasil_label.config(text=f"Rekomendasi:\n{hasil_teks}")
    else:
        hasil_label.config(text="Tidak ada rekomendasi ditemukan.")

# GUI
root = tk.Tk()
root.title("Sistem Pakar Rekomendasi Wisata")

frame = ttk.Frame(root, padding=20)
frame.grid()

ttk.Label(frame, text="Pilih Jenis Wisata:").grid(column=0, row=0, sticky='w')
jenis_var = tk.StringVar()
ttk.Combobox(frame, textvariable=jenis_var, values=["pantai", "pegunungan", "danau", "sejarah", "hiburan"]).grid(column=1, row=0)

ttk.Label(frame, text="Pilih Harga:").grid(column=0, row=1, sticky='w')
harga_var = tk.StringVar()
ttk.Combobox(frame, textvariable=harga_var, values=["murah", "sedang", "mahal"]).grid(column=1, row=1)

ttk.Label(frame, text="Pilih Kegiatan:").grid(column=0, row=2, sticky='w')
kegiatan_var = tk.StringVar()
ttk.Combobox(frame, textvariable=kegiatan_var, values=["berenang", "mendaki", "naik_perahu", "belajar", "bermain", "foto"]).grid(column=1, row=2)

ttk.Button(frame, text="Cari Rekomendasi", command=cari_rekomendasi).grid(column=0, row=3, columnspan=2, pady=10)

hasil_label = ttk.Label(frame, text="", foreground="blue")
hasil_label.grid(column=0, row=4, columnspan=2)

print("Menjalankan GUI...")
root.mainloop()
