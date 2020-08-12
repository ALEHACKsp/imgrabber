# Copyright Wibucode
# ------------------
import requests, os, sys
from bs4 import BeautifulSoup as bs
os.system("clear")
print """\033[91m
     _____
    (, /                         /)
      / ___   _     _   __  _   (/_  _  __
  ___/__// (_(_/_  (_/_/ (_(_(_/_) _(/_/ (_
(__ /       .-/   .-/
           (_/   (_/
\033[97mImages Grab
Author	: Firmansyahken
"""
url = raw_input("\033[91mUrl	   :\033[97m ")
fn = raw_input("\033[91mNama Folder:\033[97m ")
os.system("mkdir "+fn)
os.chdir(fn)
r = requests.get(url)
soup = bs(r.text, "html.parser")
tag = soup.find_all("img")
for img in tag:
	internal = img.get("src")
	if not "http" in internal:
		res = url+"/"+internal
		result = requests.get(res)
		img = res.split("/")[-1]
		print "Mendownload gambar "+img
                f = open(img, "wb")
                f.write(result.content)
                f.close()
	elif "http" in internal:
		res = internal
		result = requests.get(res)
		img = res.split("/")[-1]
		print "Mendownload gambar "+img
		f = open(img, "wb")
		f.write(result.content)
		f.close()
	else:
		print "\033[91mGambar tidak ditemukan\033[97m"
pass
print "\nHasil download berada di folder "+fn
