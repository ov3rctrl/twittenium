from seleniumbase import BaseCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyfiglet
import colorful as cf


mobile_emulation = {

    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },

    "userAgent": "Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36" }

chrome_options = Options()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

ov3rctrl = pyfiglet.figlet_format("by ov3rctrl", font = "mini" ) 
banner = pyfiglet.figlet_format("TWITTENIUM", font = "3x5" )  
  
print(cf.bold_red(banner + ov3rctrl))
print(cf.bold_green("github.com/ov3rctrl\nov3rctrl.xyz\n"))    
time.sleep(1)
print(cf.bold_blue('# # # #\n'))
time.sleep(1)

print(cf.bold_red("""
\t \t \t
.x0Okkdok0Oxooooodx0XKkxO0kxxkOK0kkKXXXXKXXKOOKKX0O0KK0kxxk00OOOO00XWMMMMM          
.x0OkxdxO0kdooloddkKK0kdO0kdxkOKKOkKXXXXKKK0kk0XX0k0KK0xddd0KKOkOKXNWMMMMM          
.dOkkdldOkxdollodxkKK0kxO0xdxkOK0xxOxol:;:c:;lkKX0O0KKOkdddO0KKOO0KXWMMMMM          
.dOkOxdkOkxdoloodxOKKOxxO0xdxk0K0d;.         ..,dOkOKK0kddxO0KKO0KKKNMMMMM          
.dOkxxxkkkxdoooddxO0KOddkOxdxkO0o.   ..  ..','...;oOKK0kdddOKXKkkKKKNMMMMM          
.dOxolxOkkxolloodxO00kxdOOddxkkc...,:ccccldkkd:...'d0KOxxdok0KKkk0KKXWMMMM          
.dOdclkOOkdolloodxO00OxxOkdodkd. ..''',clc::cldo'..:OK0xdddxkOKOO0K0OXMMMM          
.dkocdO0Oxolllloxk00OOxxkkdodxl........cc'...';c'  ,OKOdddxkkOKkxOK0OXMMMM          
.dklcxOOkdllllldxO00Oxdxkxoodxc.',,,;;:xkl;,';:ol. :0Kkdodddk0KkdkKKOKWMMM          
.odcokOOkollllldxO0Oxocoxdllodc,;:c:,',coollldkkd,.l0KkdddooxO0OxxO0kONMMM          
.oocdOOOxlccllldkOkxl:;cxdllldo,';;'.   .:ooolloc,'cO0kdddoodO00xxk0OkXMMM          
.ooldkkkolccllldxxoc;''cxocllodc'.. .....';cl::cooodO0xodddodk0OddxkOkXMMM          
.clldkkxoccclllool:,...:olccloxo. ......''.;lccodxddO0xooododkOOdodkkdOWMM          
.;:ldxkdlccclllcc:,'...;lc:;:oxd'...',,;::::loodxxddkOxooooooxkkxodddokNMM          
.;:lxxxoccccccc;''''...,::;,;lxd,  ...',;,,,;clxxdodxkxoodolooxOxddoooxNMM          
.:clxxdlc:::;;:c:,.  ...,;,,;cdo.           .':lodddxxdoddooooxOxooooddKWM          
.,clddlc:cldxOKXN0:       ......              .:ooodxxdodddooooxxoddoolOWM          
':loolok0KXNXXXXOc.                           'clloxxdooooooodxxdddoooOWMM          
.:ldxOKXXXXXXXX0xc.                            ..,:oxdlloolllodxdddoookNMM          
'cxOKXXXXXKKKKKOdl'                               ..,;:loolllldkxoddoodKMM         
.ck0KXXXXXK0kdooooo:.                         ...........,clllloxxodxdoo0W          
.xKKXXXXXXK0xc,,,:c;.                      .....''...'''...':lloxxddxkxokN          
'kXXXXKKK00Od:,,'...                       ...'''....''','...,coxkddxkxoxN          
'kK0OOOkkxdc,..',,.                        .,..,,'.  .'..',,'.':dkxddkxodX          
.dkdolccc:'. ..;c:.                         ...... ......',','..,oxddxxddK          
.:c:;,''..    .,,.                            .......''..''....  .oxooddok         
.'''..    .;;.                                  .                'x0kdoldX          
....      cNK;                                                    :0XKkodK          
BERİ BAK BERİ BERİ BAK BERİ BERİ BAK BERİ BERİ BAK BERİ BERİ BAK BERİ BERİ 
BERİ BAK BERİ BERİ BAK BERİ BERİ BAK BERİ BERİ BAK BERİ BERİ BAK BERİ BERİ  
"""))

print(cf.bold_green("""
yukarıdaki ünlümüz kimdir?
"""))
cevap = input(": ")

if (cevap == "fako"): 
    k_adi = input("\nk.adi? : ")
    sifre = input("sifre? : ")
    profil = input("takipçileri takip edilecek profil? : ")
    takipsayisi = int((input("kaç kişi takip edilsin : ")))
    aralik = int((input('kaç saniye aralıkla (önerilen -> 10) : ')))

    class takipetme(BaseCase):
        def test_basic(self):
            self.open("https://mobile.twitter.com/login")
            self.click_xpath("//input[@name='session[username_or_email]']")
            self.type(f"//input[@name='session[username_or_email]']", k_adi)
            self.click("//input[@name='session[password]']")
            self.type(f"//input[@name='session[password]']", sifre)
            time.sleep(0.5)
            self.click_xpath("//span[contains(.,'Giriş yap')]")
            time.sleep(0.5)
            self.open("https://twitter.com/"+profil+"/followers")
            time.sleep(1)
            for i in range(takipsayisi):
                self.click("//span[contains(.,'Takip et')]")
                time.sleep(2)
            self.scroll_to_bottom()
            for i in range(takipsayisi):
                self.click("//span[contains(.,'Takip et')]")
                time.sleep(aralik)
            self.scroll_to_bottom()
            for i in range(takipsayisi):
                self.click("//span[contains(.,'Takip et')]")
                time.sleep(aralik)
            self.scroll_to_bottom()
            for i in range(takipsayisi):
                self.click("//span[contains(.,'Takip et')]")
                time.sleep(aralik)
            self.scroll_to_bottom()
            for i in range(takipsayisi):
                self.click("//span[contains(.,'Takip et')]")
                time.sleep(aralik)
            self.scroll_to_bottom()
            for i in range(takipsayisi):
                self.click("//span[contains(.,'Takip et')]")
                time.sleep(aralik)
            self.scroll_to_bottom()
            for i in range(takipsayisi):
                self.click("//span[contains(.,'Takip et')]")
                time.sleep(aralik)
            self.scroll_to_bottom()
            for i in range(takipsayisi):
                self.click("//span[contains(.,'Takip et')]")
                time.sleep(aralik)
            self.scroll_to_bottom()
         

else:
    time.sleep(1)
    print(cf.bold_yellow("\nGeçerli Bir Seçim Yapıp Tekrar Dene\n"))

