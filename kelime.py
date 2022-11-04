import random

dosya = open("kelime.txt","r")
kelime = dosya.read()
kelimeler = []

i = 0
for x in range(len(kelime)):
	if(ord(kelime[x])==10):
		k = ""
		for y in kelime[i:x]:
			if(ord(y)>64 and ord(y)<91):
				k += chr(ord(y)+32)
			else:
				k += y
		kelimeler.append(k)
		i = x+1
#kelimeler dizisi
print("sadece küçük harf")
ilkKarakter = chr(random.randint(97,122))
puan = 0
yasakKelime = [""]
while True:
	print(ilkKarakter)
	girilenKelime = input()
	var = False
	for x in kelimeler:
		if(x==girilenKelime and girilenKelime[0]==ilkKarakter and girilenKelime not in yasakKelime):
			var = True
			puan += 1
			ilkKarakter = girilenKelime[len(girilenKelime)-1]
			yasakKelime.append(girilenKelime)
	print(var)
	if(var == False):
		print("puan=" +str(puan))
		break
