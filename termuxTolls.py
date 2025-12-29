import os
import sys
import time

# --- PENGURUSAN WARNA ---
R = '\033[31m' # Merah
G = '\033[32m' # Hijau
Y = '\033[33m' # Kuning
B = '\033[34m' # Biru
C = '\033[36m' # Cyan
W = '\033[0m'  # Putih

def header():
    os.system("clear")
    print(f"{C}==================================================")
    print(f"{C}       TERMUX MULTI-TOOL INSTALLER V3.0          ")
    print(f"{C}          Dicipta : Man Force X            ")
    print(f"{C}=================================================={W}")

def run(cmd):
    """Fungsi untuk jalankan command terminal"""
    os.system(cmd)

def install_system():
    print(f"\n{B}[+] Mengemaskini Sistem & Base Packages...{W}")
    # Update repo dan pasang tools asas pengurusan fail
    pkgs = "update && pkg upgrade -y && pkg install -y coreutils termux-api tar zip unzip wget curl nano vim htop"
    run(f"pkg {pkgs}")

def install_dev():
    print(f"\n{G}[+] Memasang Persekitaran Programming...{W}")
    # Pasang bahasa pengaturcaraan utama
    langs = "python python-pip nodejs golang php ruby rust clang make"
    run(f"pkg install {langs} -y")
    # Library python yang selalu digunakan untuk scripting
    run("pip install requests colorama bs4 scapy pushbullet-py")

def install_hacking():
    print(f"\n{R}[!] Memasang Tools Hacking & Network Security...{W}")
    # Tools networking dan pentesting asas
    nets = "nmap hydra nikto dnsutils net-tools openssh"
    run(f"pkg install {nets} -y")
    
    # Buat folder khas untuk tool dari GitHub
    run("mkdir -p ~/hacking_tools")
    os.chdir(os.path.expanduser("~/hacking_tools"))
    
    # Klon repo hacking popular
    tools = {
        "Sqlmap": "https://github.com/sqlmapproject/sqlmap.git",
        "Metasploit": "https://github.com/rapid7/metasploit-framework.git", # Amaran: Ini sangat besar!
        "Social-Engineer-Toolkit": "https://github.com/trustedsec/social-engineer-toolkit.git",
        "Sherlock": "https://github.com/sherlock-project/sherlock.git"
    }
    
    for name, url in tools.items():
        print(f"{Y}--- Mengambil {name} ---{W}")
        if not os.path.exists(name):
            run(f"git clone {url}")

def customize_termux():
    print(f"\n{C}[+] Menghias Terminal (Oh-My-Zsh & Neofetch)...{W}")
    run("pkg install zsh neofetch -y")
    # Set neofetch supaya keluar setiap kali buka Termux
    run("echo 'neofetch' >> ~/.bashrc")

def menu():
    while True:
        header()
        print(f"{G}1. {W}Pasang Semua (Full Setup - Lambat)")
        print(f"{G}2. {W}Pakej Sistem Sahaja (Asas)")
        print(f"{G}3. {W}Programming Tools (Dev Mode)")
        print(f"{G}4. {W}Hacking Tools (Cybersecurity)")
        print(f"{G}5. {W}Hias Termux (Bagi Lawa)")
        print(f"{R}0. {W}Keluar")
        
        pilihan = input(f"\n{Y}Pilih kategori (0-5): {W}")

        if pilihan == '1':
            install_system()
            install_dev()
            install_hacking()
            customize_termux()
            print(f"\n{G}SEMUA SIAP! Sila restart Termux.{W}")
            break
        elif pilihan == '2':
            install_system()
        elif pilihan == '3':
            install_dev()
        elif pilihan == '4':
            install_hacking()
        elif pilihan == '5':
            customize_termux()
        elif pilihan == '0':
            print("Keluar...")
            sys.exit()
        else:
            print(f"{R}Pilihan tidak sah!{W}")
            time.sleep(2)

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(f"\n{R}Proses dibatalkan oleh pengguna.{W}")
