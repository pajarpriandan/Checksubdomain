
---

## Checksubdomain - Subdomain Takeover Checker

**Checksubdomain** adalah tool Python sederhana untuk mendeteksi kemungkinan subdomain takeover secara otomatis dari daftar subdomain yang ditentukan.

### Fitur:
- Cek status HTTP dan CNAME dari subdomain
- Deteksi kemungkinan vulnerable takeover
- Output hasil ke file `hasil.txt`
- Mudah digunakan, cocok untuk pemula hingga profesional

---

### Instalasi

1. Clone repositori ini:

```bash
git clone https://github.com/pajarpriandan/Checksubdomain.git
cd Checksubdomain

```

2. Install dependensi:

```bash

pip install -r requirements.txt

---

### Penggunaan

1. Buat file target subdomain dengan `nano`:

```bash
nano targets.txt
```

Contoh isi `targets.txt`:

```
sub1.example.com
sub2.example.com
blog.example.com
```

Setelah selesai mengetik, tekan:

- `CTRL + X` untuk keluar
- Tekan `Y` lalu `Enter` untuk menyimpan

2. Jalankan tools:

```bash
python3 pajartakeover.py targets.txt

```

---

### Output

- Semua hasil akan tersimpan di file `hasil.txt`
- Jika subdomain terdeteksi vulnerable, akan muncul:

```
[VULN] subdomain.example.com kemungkinan bisa di-takeover!
```

---

### Peringatan

Tools ini dibuat untuk tujuan edukasi dan pengujian keamanan yang legal.  
**Saya tidak bertanggung jawab atas penyalahgunaan tools ini oleh pihak lain.**  
Gunakan dengan bijak dan hanya pada domain yang kamu miliki atau memiliki izin.

Credit
Dibuat oleh @pajarpriandana
Follow IG: @ox_pajarpriandana
---

