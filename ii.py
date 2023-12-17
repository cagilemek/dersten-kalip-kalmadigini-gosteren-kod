"Bir dersin ortalaması girilen öğrencinin o dersten geçip geçmediğini gösteren python kodunu yazınız."
"(50’den büyükse geçti değilse kaldı yazdıran örnek python kodu)"
a = input ("birinci sınav notu: ")
b = input ("ikinci sınav notu: ")
ort = int(a)*0.4 + int(b)*0.6
print (ort)

if (ort >= 50):
    print ("dersi geçtiniz")

if (ort <= 50):
    print ("dersten kaldınız")

