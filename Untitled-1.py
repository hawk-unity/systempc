import platform
first=" Sistem   :" ,platform.system()
second="İsim   :", platform.node()
three="İşletim Sistemi   :", platform.platform()
four="İşlemci   :" ,platform.processor()
five="Bit   :" ,platform.machine()
six="Genel   :" ,platform.uname()
print(""" 
 - WarriorTurks Python3 Örnekleri -    
 1 - Sistem 
 2- İsim
 3 - İşletim Sistemi 
 4 -İşlemci 
 5 - Bit
 6 - Genel 
 7 - HEPSİ 
      """)
örnek = "hatalı seçim yaptın dostum"
seçim = input("Neyi Öğrenmek istersin : ")
if seçim == "1":
    print(first) 
elif seçim == "2":
    print(second)
elif seçim == "3":
    print(three)
elif seçim == "4":
    print(four)
elif seçim == "5":
    print(five)
elif seçim == "6":
    print(six)
elif seçim == "7":
    print(first , "\n" , second , "\n" , three , "\n" , four , "\n" , five , "\n" , six )
else : 
    print(örnek)