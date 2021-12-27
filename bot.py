#!/usr/bin/python
# Creator : Kingtebe
# Support : https://t.me/Captain_bulls
# Follow my github https://github.com/Musk-ID
import os,re,sys,time,random,datetime
from lib.setup import *
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    exit("\n [!] Module not installed !\n")

c = '\033[1;36m'
p = '\033[1;37m'
h = '\033[1;32m'
k = '\033[1;33m'
m = '\033[1;31m'
q = '\033[30m'
t = '\033[0;32m'
u = '\033[0;37m'
z = '\033[2;107m'
o = '\033[0m'
r = '\033[0;36m'

class mainbot:
    def __init__(self):
        self.ses = requests.Session()
        self.time = datetime.datetime.now().strftime("%H:%M:%S")
        self.logo = f"\n{r}  {r}▄    ▄▄▄▄▄▄▄    ▄\n {r}▀▀▄─▄█████████▄─▄▀▀  {r}╔╗ {p}┬┌┬┐┌┐ ┌─┐┬ ┬   {r}╔═╗{p}┬ ┬┌─┐┌┐┌┌─┐┬\n {r}    ██ {k}▀{r}███{k}▀ {r}██      {r}╠╩╗{p}│ │ ├┴┐│ │└┬┘{q}───{r}║  {p}├─┤├─┤│││├┤ │\n {r}  ▄─▀████{k}▀{r}████▀─▄    {r}╚═╝{p}┴ ┴ └─┘└─┘ ┴    {r}╚═╝{p}┴ ┴┴ ┴┘└┘└─┘┴─┘\n {u}▀█    ██▀█▀██   █▀   {z}{q} By : Kingtebe | Yt : Bitboy Channel {o}{p}\n"

    def get_user(self):
        url = "https://shibaads.com/dashboard.php"
        req = BeautifulSoup(self.ses.get(url).text,"html.parser")
        try:
            username = req.find("h3",attrs={"class":"font-weight-bold"}).text
            balance = req.find("span",attrs={"class":"fs-30 mb-2"}).text
            refer = req.find("input",{"type":"text","class":"form-control link"})
            return username,balance,refer
        except AttributeError:
            os.remove(".cookie")
            exit("# Cookie has expired")

    def get_faucet(self):
        while True:
            url = "https://shibaads.com/inc/faucet.php"
            req = self.ses.get(url).text
            if "done" in req:
                self.masuk = self.get_user()
                print(f"  {r}[{p}{self.time}{r}] {p}Success get reward 4 SHIB {q}- {p}now "+self.masuk[1]+" SHIB")
                setup().countdown(int(60*5))
            else:
                exit(f"  {r}[{p}{self.time}{r}] {p}Claim SHIB failed\n")

    def get_surf_ads(self):
        while True:
            url = "https://shibaads.com/surfad.php"
            req = self.ses.get(url).text
            adsid = re.search(r'href="([^>]+)"<',req).group(1)
            data = {"adid":adsid.removeprefix("surfsec.php?adc=")}
            url = "https://shibaads.com/inc/sf01credit.php"
            req = self.ses.post(url,data=data).text
            if len(adsid) == 0:
                exit(f"  {r}[{p}{self.time}{r}] {p}Surf ads not available\n")
            else:
                self.masuk = self.get_user()
                print(f"  {r}[{p}{self.time}{r}] {p}Surf ads success get reward 4 SHIB {q}- {p}now "+self.masuk[1])
                setup().countdown(int(5))

    def get_mainbot(self):
        if not os.path.exists(".cookie"):
           os.system('cls' if os.name=='nt' else 'clear')
           setup().message(self.logo)
           open(".cookie","w").write(input(f"  {t}⏣ {p}Cookie {q}: {r}"))
        self.ses.headers.update({"cookie":open(".cookie").read()})
        os.system('cls' if os.name=='nt' else 'clear')
        self.account = self.get_user()
        setup().message(self.logo)
        setup().message(f"  {t}⏣ {p}Username {q}:{p}"+self.account[0].removeprefix("Welcome")+f"\n  {t}⏣ {p}Balance  {q}: {p}"+self.account[1]+f" SHIB \n  {t}⏣ {p}Referral {q}: {p}"+self.account[2].get("value")+f"\n\n  {r}      [{p}1{r}] {p}Claim faucet \n  {r}      [{p}2{r}] {p}Surf ads\n  {r}      [{p}3{r}] {p}Exit")
        pilpel = input(f"  {t}>> {p}")
        print("")
        if pilpel in ["1","01"]:
             self.get_faucet()
        elif pilpel in ["2","02"]:
             self.get_surf_ads()
        elif pilpel in ["3","03"]:
             exit(f"  {r}[{p}{self.time}{r}] {p}Byeee !!\n")
        else:
             exit(f"  {r}[{p}{self.time}{r}] {p}Your selection no available \n")

if __name__=='__main__':
    mainbot().get_mainbot()
