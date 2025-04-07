
---

# Checksubdomain

Checksubdomain adalah tools sederhana untuk mengecek kemungkinan subdomain takeover pada daftar subdomain yang kamu miliki. Tools ini sangat cocok digunakan oleh pentester, bug bounty hunter, dan para praktisi keamanan siber lainnya.

## Fitur

- Cek kemungkinan subdomain takeover  
- Menampilkan status domain: vuln / not vuln  
- Menyimpan hasil ke `hasil.txt`  
- Tampilan ASCII banner menarik  

## Cara Install

```bash
git clone https://github.com/pajarpriandan/Checksubdomain
cd Checksubdomain
pip install -r requirements.txt
```

## Cara Penggunaan

1. Siapkan daftar subdomain dalam file `.txt`, misalnya: `targets.txt`  
2. Jalankan perintah berikut:

```bash
python3 pajartakeover.py
```

3. Masukkan nama file target saat diminta, contoh:

```
[?] Masukkan nama file target: targets.txt
```

4. Tools akan mulai memeriksa tiap subdomain dan memberi tahu apakah rentan terhadap takeover atau tidak.

## Output

- Hasil akan ditampilkan di terminal  
- Semua subdomain yang vuln akan disimpan ke `hasil.txt`

## Contoh

```
[!] Memulai scan...
[+] Memeriksa: blog.example.com
[VULN] Subdomain VULNERABLE: blog.example.com
```

## Credit

Dibuat oleh @pajarpriandana  
Follow IG: @ox_pajarpriandana

---

