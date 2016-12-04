import urllib.request
import os
from bs4 import BeautifulSoup

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

print(color.BOLD+color.YELLOW+"Google Hacking Toolkit (GHT)- Ver : 0.1 - 11 Dec 2013\nThis tool helps you to more easily be able to search in Google"+color.GREEN +" \nCODE BY Ali Yazdani -- https://github.com/Ali-Yazdani"+ color.END)
print(color.CYAN+'Tip: To use several operators add + between operators\nFor example: site:target.com+inurl:/admin/main.aspx'+color.END)
n = int(input(color.BLUE  +"Enter number of Google page for search: "+ color.END))
dork = input(color.BLUE  +"Enter DORK: "+ color.END)
try:
    f = open("tmpsite.txt","a")
    for start in range(0, n):
        url = "http://www.google.com/search?q="+dork+"&start=" + str(start*10)
        print(url)
        page = opener.open(url)
        soup = BeautifulSoup(page, 'html.parser')

        for cite in soup.findAll('cite'):
            link = cite.text
            cc = link.find("/")
            if cc == -1:
                f.write(link+"\n")
            else:
                i = 0
                j = cc
                f.write(link[i:j]+"\n")

        print("Links Page "+str(start+1)+" Saved.")
    f.close()

    lines = open("tmpsite.txt",'r').readlines()
    uniquelines = set(lines)
    open("site.txt", 'w').writelines(uniquelines)
    os.remove("tmpsite.txt")
    print("Finish")
except:
    print(color.RED+'An error has occurred. Please run the code again and Tips to Consider.'+color.END)