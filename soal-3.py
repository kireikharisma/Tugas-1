up=float(input("Nilai Ujian Praktek : "))
ut=float(input("Nilai Ujian Teori : "))
if ut >=70 and up>=70 :
    print("Selamat, Anda lulus!")
elif ut >=70 and up<70 :
    print("Anda harus mengulang ujian praktek.")
elif ut <70 and up>=70 :
    print("Anda harus mengulang ujian teori.")
else :
    print("Anda harus mengulang ujian teori dan praktek.")