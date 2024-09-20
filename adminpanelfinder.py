#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Coded by      @charliecpln
# Discord:      @charliecpln
# Telegram:     @charliecpln
# Github:       @charliecpln


import os
import asyncio


def turkce():
	def sil():
	    os.system('cls' if os.name == 'nt' else 'clear')
	
	def kurulum():
	    try:
	        print("Kütüphaneler denetleniyor...")
	        from colorama import Fore, Back, Style, init
	        import requests
	        import logging
	        import aiohttp
	        sil()
	    except ImportError:
	        print("Eksik kütüphaneler bulundu, otomatik indiriliyor...")
	        os.system("pip install colorama requests logging aiohttp")
	        sil()
	
	kurulum()
	
	from colorama import Fore, Back, Style, init
	import logging
	import requests
	import aiohttp
	
	logging.basicConfig(filename='error_log.txt', level=logging.ERROR)
	init(autoreset=True)
	
	def log_hata(url, hata_mesaji):
	    logging.error(f"Hata {url} için: {hata_mesaji}")
	
	def url_sonu_kontrol_ve_ekle(url, path):
	    if not path.startswith('/'):
	        path = '/' + path
	    return url.rstrip('/') + path
	
	import asyncio
	from colorama import Fore
	
	async def url_test_et_async(session, url, yollar):
	    tasks = []
	    denenen = 0
	    basarili = 0
	    basarisiz = 0
	    hatali = 0
	    yols = len(yollar)
	    
	    for yol in yollar:
	        test_url = url_sonu_kontrol_ve_ekle(url, yol)
	        tasks.append(test_url)
	    
	    results = await asyncio.gather(*[async_get(session, test_url) for test_url in tasks])
	    
	    for test_url, status in results:
	        try:
	            if status == 200:
	                denenen += 1
	                basarili += 1
	                print(Fore.GREEN + f"[✓] {test_url} ({denenen}/{yols})")
	                with open("adminfinder.txt", "a") as dosya:
	                    dosya.write(f"[✓] {test_url}\n")
	            else:
	                denenen += 1
	                basarisiz += 1
	                print(Fore.RED + f"[X] {test_url} ({denenen}/{yols})")
	        except Exception as e:
	            hatali += 1
	            print(Fore.YELLOW + f"[!] {test_url} test edilirken hata oluştu: {str(e)}")
	    
	    toplam = basarili + basarisiz
	    print(Style.BRIGHT + Fore.CYAN + f"""
	    			[ANALİZLER]
	    			
	    Başarılı tarama: {basarili}
	    Başarısız tarama: {basarisiz}
	    Hatalı tarama: {hatali}
	    Toplam tarama: {toplam}
	    
	    Özet: {basarili}/{toplam}
	    """)
	    input(Fore.MAGENTA + "\n\nÇıkmak için 'enter' tuşuna basınız...")
	    exit()
	
	async def async_get(session, url):
	    try:
	        async with session.get(url) as response:
	            return url, response.status
	    except aiohttp.ClientError as e:
	        print(Back.RED + "[!]" + Back.RESET + f" {url} domain yanlış")
	        log_hata(url, str(e))
	        return url, None
	    except Exception as e:
	        print(Fore.RED + f"Hata: {e}")
	        log_hata(url, str(e))
	        return url, None
	
	async def main(urls, yollar):
	    async with aiohttp.ClientSession() as session:
	        tasks = [url_test_et_async(session, url, yollar) for url in urls]
	        await asyncio.gather(*tasks)
	
	def yol_listesi_yukle():
	    try:
	        print(Fore.MAGENTA + "\nÖzel yol listesi yoksa boş bırakınız!\n")
	        yol_dosyasi = input(Fore.YELLOW + "Özel yol listesi dosyası: ")
	        sil()
	        if yol_dosyasi.strip() == "":
	            return None
	        with open(yol_dosyasi, "r") as dosya:
	            yollar = [yol.strip() for yol in dosya]
	        print(Fore.CYAN + f"{len(yollar)} adet yol yükleniyor...")
	        print(Back.RED + f"[!] Bu işlem biraz uzun sürebilir!\n")
	        return yollar
	    except FileNotFoundError:
	        print(Fore.MAGENTA + "Dosya bulunamadı. Varsayılan yollar kullanılacak.")
	        return None
	
	varsayilan_yollar = [
	    '/phpmyadmin', '/wp-admin', '/cpanel', '/admin', '/webmail',
	    '/adminer', '/plesk', '/git', '/user', '/setup',
	    '/admin_login', '/administrator', '/admincp', '/dashboard',
	    '/controlpanel', '/myadmin', '/siteadmin', '/superadmin',
	    '/admin_area', '/site_admin', '/manage', '/console', '/backend',
	    '/app/admin', '/portal/admin', '/admin_dashboard', '/site_control',
	    '/adminpanel', '/control', '/settings', '/adminarea', '/management',
	    '/sysadmin', '/panel', '/system', '/config',
	    '/admin_settings', '/admin_tools', '/admin_access', '/admin_console',
	    '/admin_interface', '/admin_zone', '/admin_home', '/admin_index',
	    '/administration', '/admin_page', '/admin_section', '/admin_modules',
	    '/admin_mgmt', '/webadmin', '/admin_main', '/admin_portal',
	    '/admin_control', '/admin_options', '/admin_workspace', '/admin_homepage',
	    '/admin_directory', '/admin_link', '/admin_manager', '/admin_host',
	    '/admin_setup', '/admin_view', '/admin_service', '/server_admin',
	    '/login', '/control_panel', '/user_admin', '/backend',
	    '/site_control', '/admin_site', '/admin_view', '/admin_zone',
	    '/mysqladmin', '/sqlbuddy', '/dbadmin', '/myadmin',
	    '/webadmin', '/sqladmin', '/mysqlmanager', '/controlpanel',
	    '/dashboard', '/manage', '/portal', '/console',
	    '/site_control', '/system', '/settings', '/webmail'
	]
	
	try:
	    urltxt = input(Fore.YELLOW + "URL'lerin olduğu txt dosyası: ")
	    with open(urltxt, "r") as dosya:
	        urllistesi = [url.strip() for url in dosya]
	
	    yollar = yol_listesi_yukle() or varsayilan_yollar
	
	    if not urllistesi:
	        print(Fore.RED + "URL listesi boş. Program sonlandırılıyor.")
	    elif not yollar:
	        print(Fore.RED + "Yol listesi boş. Program sonlandırılıyor.")
	    else:
	        asyncio.run(main(urllistesi, yollar))
	
	except Exception as e:
	    print(Fore.RED + f"Hata: {e}")
	    log_hata("Genel", str(e))
	    
	    
	    
def ingilizce():
	def sil():
	    os.system('cls' if os.name == 'nt' else 'clear')
	
	def kurulum():
	    try:
	        print("Libraries are being checked...")
	        from colorama import Fore, Back, Style, init
	        import requests
	        import logging
	        import aiohttp
	        sil()
	    except ImportError:
	        print("Missing libraries found, downloading automatically...")
	        os.system("pip install colorama requests logging aiohttp")
	        sil()
	
	kurulum()
	
	from colorama import Fore, Back, Style, init
	import logging
	import requests
	import aiohttp
	
	logging.basicConfig(filename='error_log.txt', level=logging.ERROR)
	init(autoreset=True)
	
	def log_hata(url, hata_mesaji):
	    logging.error(f"Error for {url}: {hata_mesaji}")
	
	def url_sonu_kontrol_ve_ekle(url, path):
	    if not path.startswith('/'):
	        path = '/' + path
	    return url.rstrip('/') + path
	
	import asyncio
	from colorama import Fore
	
	async def url_test_et_async(session, url, yollar):
	    tasks = []
	    denenen = 0
	    basarili = 0
	    basarisiz = 0
	    hatali = 0
	    yols = len(yollar)
	    
	    for yol in yollar:
	        test_url = url_sonu_kontrol_ve_ekle(url, yol)
	        tasks.append(test_url)
	    
	    results = await asyncio.gather(*[async_get(session, test_url) for test_url in tasks])
	    
	    for test_url, status in results:
	        try:
	            if status == 200:
	                denenen += 1
	                basarili += 1
	                print(Fore.GREEN + f"[✓] {test_url} ({denenen}/{yols})")
	                with open("adminfinder.txt", "a") as dosya:
	                    dosya.write(f"[✓] {test_url}\n")
	            else:
	                denenen += 1
	                basarisiz += 1
	                print(Fore.RED + f"[X] {test_url} ({denenen}/{yols})")
	        except Exception as e:
	            hatali += 1
	            print(Fore.YELLOW + f"[!] An error occurred while testing {test_url}: {str(e)}")
	    
	    toplam = basarili + basarisiz
	    print(Style.BRIGHT + Fore.CYAN + f"""
	    			[ANALYSES]
    		
    Successful scans: {basarili}
    Failed scans: {basarisiz}
    Erroneous scans: {hatali}
    Total scans: {toplam}
    
    Summary: {basarili}/{toplam}
	    """)
	    input(Fore.MAGENTA + "\n\nPress 'Enter' to exit...")
	    exit()
	
	async def async_get(session, url):
	    try:
	        async with session.get(url) as response:
	            return url, response.status
	    except aiohttp.ClientError as e:
	        print(Back.RED + "[!]" + Back.RESET + f" {url} domain is incorrect")
	        log_hata(url, str(e))
	        return url, None
	    except Exception as e:
	        print(Fore.RED + f"Error: {e}")
	        log_hata(url, str(e))
	        return url, None
	
	async def main(urls, yollar):
	    async with aiohttp.ClientSession() as session:
	        tasks = [url_test_et_async(session, url, yollar) for url in urls]
	        await asyncio.gather(*tasks)
	
	def yol_listesi_yukle():
	    try:
	        print(Fore.MAGENTA + "\nIf there is no special path list, leave it empty!\n")
	        yol_dosyasi = input(Fore.YELLOW + "Special path list file:")
	        sil()
	        if yol_dosyasi.strip() == "":
	            return None
	        with open(yol_dosyasi, "r") as dosya:
	            yollar = [yol.strip() for yol in dosya]
	        print(Fore.CYAN + f"{len(yollar)} Loading quantity path...")
	        print(Back.RED + f"[!] This process may take a while!\n")
	        return yollar
	    except FileNotFoundError:
	        print(Fore.MAGENTA + "File not found. Default paths will be used.")
	        return None
	
	varsayilan_yollar = [
	    '/phpmyadmin', '/wp-admin', '/cpanel', '/admin', '/webmail',
	    '/adminer', '/plesk', '/git', '/user', '/setup',
	    '/admin_login', '/administrator', '/admincp', '/dashboard',
	    '/controlpanel', '/myadmin', '/siteadmin', '/superadmin',
	    '/admin_area', '/site_admin', '/manage', '/console', '/backend',
	    '/app/admin', '/portal/admin', '/admin_dashboard', '/site_control',
	    '/adminpanel', '/control', '/settings', '/adminarea', '/management',
	    '/sysadmin', '/panel', '/system', '/config',
	    '/admin_settings', '/admin_tools', '/admin_access', '/admin_console',
	    '/admin_interface', '/admin_zone', '/admin_home', '/admin_index',
	    '/administration', '/admin_page', '/admin_section', '/admin_modules',
	    '/admin_mgmt', '/webadmin', '/admin_main', '/admin_portal',
	    '/admin_control', '/admin_options', '/admin_workspace', '/admin_homepage',
	    '/admin_directory', '/admin_link', '/admin_manager', '/admin_host',
	    '/admin_setup', '/admin_view', '/admin_service', '/server_admin',
	    '/login', '/control_panel', '/user_admin', '/backend',
	    '/site_control', '/admin_site', '/admin_view', '/admin_zone',
	    '/mysqladmin', '/sqlbuddy', '/dbadmin', '/myadmin',
	    '/webadmin', '/sqladmin', '/mysqlmanager', '/controlpanel',
	    '/dashboard', '/manage', '/portal', '/console',
	    '/site_control', '/system', '/settings', '/webmail'
	]
	
	try:
	    urltxt = input(Fore.YELLOW + "The txt file containing the URLs: ")
	    with open(urltxt, "r") as dosya:
	        urllistesi = [url.strip() for url in dosya]
	
	    yollar = yol_listesi_yukle() or varsayilan_yollar
	
	    if not urllistesi:
	        print(Fore.RED + "The URL list is empty. Terminating the program.")
	    elif not yollar:
	        print(Fore.RED + "The path list is empty. Terminating the program..")
	    else:
	        asyncio.run(main(urllistesi, yollar))
	
	except Exception as e:
	    print(Fore.RED + f"Error: {e}")
	    log_hata("General", str(e))
	    
def dilsec():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        dil = input("Lütfen bir dil seçiniz // Please select a language (tr/en): ".lower())
        if dil == "tr" or dil == "t":
            os.system('cls' if os.name == 'nt' else 'clear')
            turkce()
        elif dil == "en" or dil == "e":
            os.system('cls' if os.name == 'nt' else 'clear')
            ingilizce()
        else:
            dilsec()

dilsec()
