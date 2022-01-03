apProg=[]

print("\n========== Program Multiprogramming ==========")
ram = int(input("\nMasukkan Kapasitas RAM (GB)\t: "))

#Kapasitas OS
os = 500

#konversi GB ke Kbps
gb = ram * 1024

#banyak partisi
partisi = 8

#pengurangan ram dari os
Tram = gb - os

#pembagian partisi
Kpartisi = Tram / partisi

# Variabel sementara untuk looping
p = partisi
a = 0
x = 0

# Looping untuk penginputan
while a < p:
  program = float(input("\nMasukkan size program (Kbps) \t: "))
  # Melihat jika sudah mencapai batas jumlah input atau tidak
  if (a == 7):
    program = program + x
    # Melihat jika nilai input masih diatas batas kapasistas atau tidak
    if (program > Kpartisi):
      print("Partisi sudah mencapai maksimal")
      a = 99
    else:
      apProg.append(program)
  else:
    # Tahap pertama untuk input nilai
    if (x == 0):
      # Melihat nilai input lebih dari batas kapasitas atau tidak
      if (program < Kpartisi):
        apProg.append(program)
      else:
        x = program - Kpartisi
        apProg.append(Kpartisi)
    else: 
      program = program + x
      # Melihat nilai input lebih dari batas kapasitas atau tidak
      if (program < Kpartisi):
        apProg.append(program)
      else:
        x = program - Kpartisi
        apProg.append(Kpartisi)

  
  # Membatasi jumlah input dari user
  if (a >= 7):
    print("Jumlah partisi sudah mencapai batas maksimum")
    a = a + 1
  else:
    pilih = input("Ingin input lagi? (y/t) : ")
    # Menanyakan apakah masih ingin memberikan input atau tidak
    if pilih=="y":
      a = a+1
    if pilih=="t":
      # Jika tidak maka akan masukkan ke apProg  
      if (x > 0 and x < Kpartisi):
        apProg.append(x)
      elif (x > 0 and x >= Kpartisi):
        while x > Kpartisi:      
          x = x - Kpartisi
          apProg.append(Kpartisi)
          if (x <= Kpartisi):
            apProg.append(x)
      a = 10

# Jika variabel a berubah menjadi 100 setelah program di atas, program diberhentikan
if (a == 100):
  print("Masing-masing partisi terlalu besar")
else :
  # Melihat apakah jumlah partisi masih dalam batas atau tidak
        
  
  if (len(apProg)>=9):
    print("Partisi sudah mencapai batas")
  else:
    y = 1
    # Menampilkan semua partisi yang ada
    print("\n=================== Hasil ====================")
    print("\nKapasitas OS yang di gunakan \t:",os,"Kbps")
    print("Kapasitas RAM \t\t\t:",gb,"Kbps\n")
    
    for n in range(0, partisi ):
      
      # Mnampilkan semua hasil yang sudah diolah dan jika kurang dari jumlah partisi maka akan ditampilkan 0 (kosong)
      
      if (n < len(apProg)):
        
        print("Partisi",y,"(",Kpartisi,"kbps )", apProg[n])
   
        y = y + 1
      else:
        
        print("Partisi",y,"(",Kpartisi,"kbps ) 0.0")
        y = y + 1