#Menghitung luas lingkaran
phi=22/7
r=int(input("Jari-jari lingkaran : "))
luas_lingkaran = phi*r*r
print("Luas lingkaran dengan jari-jari {} cm adalah {} cm\u00b2".format(r, luas_lingkaran))
#untuk menampilkan tanda kuadrat gunakan print(“\u00b2”)

"""mengubah format luas menjadi 2 angka 
dibelakang koma Hint: Ubah string format untuk float
menjadi{:.2f}"""
print("Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2".format(r, luas_lingkaran))