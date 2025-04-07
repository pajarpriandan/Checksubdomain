import requests
import sys
from colorama import Fore, Style, init
init(autoreset=True)

# ASCII BANNER UPDATED
print(Fore.CYAN + r"""
  ██████╗██╗  ██╗███████╗ ██████╗ ██████╗ ███████╗██████╗ 
 ██╔════╝██║  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
 ██║     ███████║█████╗  ██║   ██║██████╔╝█████╗  ██████╔╝
 ██║     ██╔══██║██╔══╝  ██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗
 ╚██████╗██║  ██║███████╗╚██████╔╝██║     ███████╗██║  ██║
  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝
      Checker Domain Takeover by @pajarpriandana
""")

error_signatures = [
    "NoSuchBucket", "There isn't a GitHub Pages site here",
    "Do you want to register", "Sorry, this shop is currently unavailable",
    "No settings were found for this domain", "project not found",
    "Heroku | No such app", "The requested URL was not found on this server",
    "Help Center Closed", "Unknown repository", "The feed has not been found",
]

def scan_subdomain(url):
    try:
        res = requests.get(f"http://{url}", timeout=10)
        for err in error_signatures:
            if err.lower() in res.text.lower():
                print(Fore.RED + f"[VULN ini kudu dipeluk dulu] Potensi Subdomain Takeover: {url}")
                with open("hasil_takeover.txt", "a") as f:
                    f.write(f"[VULN] {url}\n")
                return
        print(Fore.GREEN + f"[OK] Tidak rentan ya sayang muach: {url}")
    except:
        print(Fore.YELLOW + f"[?] Tidak bisa mengakses ini ya sayang: {url}")

def main(file):
    try:
        with open(file, "r") as f:
            targets = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(Fore.RED + "[!] File tidak ditemukan.")
        return

    print(Fore.YELLOW + f"[*] Mulai scan {len(targets)} subdomain...\n")
    for url in targets:
        scan_subdomain(url)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.CYAN + f"Usage: python3 {sys.argv[0]} subdomains.txt")
    else:
        main(sys.argv[1])
