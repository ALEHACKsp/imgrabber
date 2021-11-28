# copyright pamekasancode
import os, sys, requests
from bs4 import BeautifulSoup as bs
b = "\033[96m"
m = "\033[91m"
p = "\033[97m"
def clear():
	os.system("clear || cls")
clear()
def directory():
	try:
		os.chdir("/sdcard")
		os.mkdir("imgrab")
		os.chdir("imgrab")
	except OSError:
		os.chdir("/sdcard/imgrab")
	except OSError:
		os.mkdir("imgrab")
		os.chdir("imgrab")
print (f"""{b}
     _____
    (, /                         /)
      / ___   _     _   __  _   (/_  _  __
  ___/__// (_(_/_  (_/_/ (_(_(_/_) _(/_/ (_
(__ /       .-/   .-/
           (_/   (_/
{p}Images Grab
Author  : Pamekasancode Team
""")
url = input("Url	: ")
directory()
req = requests.get(url)
soup = bs(req.text, "html.parser")
tag = soup.find_all("img")
for img in tag:
	images = img.get("src")
	if "http" in images:
		image = requests.get(images)
		namefile = images.split("/")[-1]
		if len(namefile) > 15:
			namefile = namefile[:8]
			print (f"{b}[{p}~{b}] {p}Mendownload "+namefile+".png")
		else:
			print (f"{b}[{p}~{b}] {p}Mendownload "+namefile)
			fw = open(namefile, "wb")
			fw.write(image.content)
			fw.close()
	elif not "http" in images:
		image = requests.get(url+"/"+images)
		namefile = images.split("/")[-1]
		if len(namefile) > 15:
			namefile = namefile[:8]
			print (f"{b}[{p}~{b}] {p}Mendownload "+namefile+".png")
		else:
			print (f"{b}[{p}~{b}] {p}Mendownload "+namefile)
			fw = open(namefile, "wb")
			fw.write(image.content)
			fw.close()
	else:
		print (f"{m}\n[x] Gambar Tidak Dapat Ditemukan{p}")
pass
print ("\n[√] Gambar disimpan di "+os.getcwd())
