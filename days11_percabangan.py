#percabangan ( If, Else, dan Elif  statement )
#contoh 1
nama = "rahma"
if nama == "rahma": #jika nilai kondisi utama true ( nama == "rahma")
    print ("hai.. Rahma how are you today") # maka statements akan di eksekusi oleh sistem dan proram stop
#tapi jika kondisi false ia akan mencari kondisi selanjutnya.
else:
    print("kamu bukan rahma")

# contoh ke 2 perbandinan nilai

nilai = int (input("masukkan nilai anda:"))

if nilai >= 90 and nilai <=100 : #kondisi utama
    print ( "nilai anda A")
elif nilai >= 80 and nilai <=90 : #kondisi tambahan
    print ( "nilai anda B")

elif nilai >= 70 and nilai <=80 : # kondisi tambahan
    print ( "nilai anda c")
else: #kondisi akhir
    print (" nilai tidak ditemukan")


#contoh ke3 kalkulator BMI

berat=int(input("masukkan berat anda:"))
tinggi= float(input("masukkan tinggi badan:"))
BMI= berat /(tinggi*tinggi)

if BMI <17.0:
    print("kurus,kekurangan berat badan")
    
elif BMI <18.4 and BMI >17.0:
    print("kurus,kekurangan berat badan ringan")
    
elif BMI < 25.0 and BMI>18.4:
    print("normal")
    
elif BMI < 27.0 and BMI>25.0:
    print("gemuk,kelebihan berat badan tingkat ringan")
    
else:
    print("kelebihan berat badan tingkat berat")


    






          
                                        
