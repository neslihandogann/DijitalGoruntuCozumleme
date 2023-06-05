


import matplotlib.pyplot as plt #çizim kitaplığıdır

plt.title("Bresenham çizgi Algoritması")
plt.xlabel("X ekseni")#eksen ataması yapıldı
plt.ylabel("Y ekseni")

def bresenham(x1,y1,x2,y2):#fonksiyon oluşturuldu.
    x,y = x1,y1
    dx = abs(x2 - x1) #sayıların mutlak değerlerini alarak doğrusal eksende eğim ve eksen arasındaki çizgiyi çizdirmeyi sağlayacaktır
    dy = abs(y2 -y1)
    egim= dy/float(dx)
#eğim 1'den büyükse doğrunun y-eksenindeki uzunluğu kadar, 1'den küçükse x-eksenindeki uzunluğu kadar işlemler tekrarlanır (uzunluklar piksel sayısı ile ölçülür). 
    if egim > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2*dy - dx
    print(f"x = {x}, y = {y}")
    # Çizim noktaların başlatılıyor
    xkoordinat = [x]
    ykoordinat = [y]
#bu işlem koordinat düzlemde verielecek olan değerin bitiş noktasına kadar olan uzaklığının keşisen yerleri dahil eğim ve mutlak değer hesaplanarak grafik arayüzüne aktarmayı sağlar 
    for k in range(2, dx + 2):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy
#bu kısım x ekseninin bitiş kısmına kadar olan hesaplama işlemini yapar
        x = x + 1 if x < x2 else x - 1

        print(f"x = {x}, y = {y}")
        xkoordinat.append(x)
        ykoordinat.append(y)

    plt.plot(xkoordinat, ykoordinat)
    plt.show()


def main():
    x1 = int(input("x'in Başlangıç ​​noktasını girin: "))
    y1 = int(input("y'nin Başlangıç ​​noktasını girin: "))
    x2 = int(input("x'in bitiş noktasını girin: "))
    y2 = int(input("y'nin bitiş noktasını girin: "))

    bresenham(x1, y1, x2, y2)

if __name__ == "__main__":
    main()