# copyright pamekasancode
import os, requests
from bs4 import BeautifulSoup as bs

def clear():
	os.system("cls || clear")

def banner():
	clear()
	print("""\033[91m
 _____                          _     
|_   _|                        | |    
  | | _ __ ___   __ _ _ __ __ _| |__  
  | || '_ ` _ \ / _` | '__/ _` | '_ \ 
 _| || | | | | | (_| | | | (_| | |_) |
 \___/_| |_| |_|\__, |_|  \__,_|_.__/  V.1.0
                 __/ |                
                |___/                 

\033[90mAuthor: Pamekasancode Team

\033[97m""")
banner()

def saveImg(nameImage, image):
	fw = open(nameImage, "wb")
	fw.write(image.content)
	fw.close()
def changeDir():
	try:
		os.chdir("imgrab")
	except:
		os.mkdir("imgrab")
		os.chdir("imgrab")
def main(url):
	changeDir()
	r = requests.get(url)
	soup = bs(r.text, "html.parser")
	tag = soup.find_all('img')
	for img in tag:
		images = img.get('src')
		nameImage = images .split("/")[-1]
		if len(nameImage) > 13:
			nameImage = nameImage[:13]
		if not ".jpg" in nameImage:
			nameImage = nameImage+".jpg"
		if "http" in images:
			image = requests.get(images)
			saveImg(nameImage, image)
			print("\033[92m[+] \033[97m"+nameImage)
		else:
			image = requests.get(url+"/"+images)
			saveImg(nameImage, image)
			print("\033[92m[+] \033[97m"+nameImage)
link = input("Link Webpage: \033[92m")
main(link)
print ("\n\033[92m[√] Gambar disimpan di \033[97m"+os.getcwd())
