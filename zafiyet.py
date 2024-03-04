import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BHECY")
os.system("figlet ZAAFİYET ANALİZİ")
os.system("apt-get install uniscan")

print("RUS ZAFİYET TOOLUNA HOJGELDİN	")
 
hedefip=input("Hedef ip giriniz : ")
os.system("uniscan -u -d "+hedefip)