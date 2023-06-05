# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 23:31:01 2023

@author: dogan
"""



import cv2 #open cv kütüphanesi 

#degeri büyüdükçe resimi yakınlaştırıyoruz.
def zoom_function(img, zoom_value=2):

    m = img.shape[0]# y koordinatı olarak yer alır yani sutün mantığı ile 
    n = img.shape[1]# x koordinatı olarak yer alır yani satır mantığı ile
    
#resimlerdeki satır ve sutün  dizilimleri ve matrix mantığı ile bir dizi linner işlemler doğrultusunda zoom değeri ile oynayarak resimi yakınlaştırmayı sağladık yani zoom in işlemi gerçekleşmiş oldu.
    x1 = int(0.5*n*(1-1/zoom_value))
    x2 = int(n-0.5*n*(1-1/zoom_value))
    y1 = int(0.5*m*(1-1/zoom_value))
    y2 = int(m-0.5*m*(1-1/zoom_value))

  
    img_zoom = img[y1:y2,x1:x2] #resim için tek boyutlu diziye koordinasyonları aktarıldı.
    
    return cv2.resize(img_zoom, None, fx=zoom_value, fy=zoom_value)#fonksiyonun çalışması için x ve y eksenlerine resim değerleri atandı.


img = cv2.imread('img.jpg')#resim okuma işlemi gerçekleştirildi
cv2.imshow("org", img)# resim gösterme

img_zoomed = zoom_function(img)#fonksiyon  zoomede atama işlemi gerçekleştirildi.



cv2.imshow("zoom in",img_zoomed) #resim fonksiyon uygulanarak ekranda yakınlaşmış şekilde görünecektir

k=cv2.waitKey(0)
if k==ord('q'):
    cv2.destroyAllWindows()