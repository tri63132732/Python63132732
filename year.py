Can=['Canh','Tan','Nham','Quy','Giap','At','Binh','Dinh','Mau','ky']
Chi=['Than', 'Dau', 'Tuat', 'Hoi', 'Ty', 'Suu', 'Dan', 'Meo', 'Thin', 'Ty', 'Ngo', 'Mui']
#Nhap nam duong lich
namDL = int(input("Nhap nam duong lich: "))

#Tinh can
can = namDL % 10

#Tinh chi
chi = namDL %12

#Xuat nam am lich
print(Can[can] + " " + Chi[chi])

