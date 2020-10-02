import numpy as np
import math

def rukun_warga(rt):
  rw += rt + rt
  rw += rw
  return rw

def pengeboran(max_distance, pengeboran_per_meter, price):
  distance_drill = (max_distance * pengeboran_per_meter)
  distance_price = (max_distance * price)
  res_drill = distance_drill + distance_price
  return res_drill

def cost_pompa(pump_price):
  res_pompa = 1*pump_price
  return res_pompa 

def cost_pipa_tampungan(d_to_rt, price): #pipe price disini pipa kelas rt
  res_pipa_tampungan = d_to_rt  * price # jarak ke RT x harga kelas pipa rt
  return res_pipa_tampungan

def tampungan(total_2nd, total_utama):
  total_tampungan = res_tampungan #total semua dari pipa tampungan
  return total_tampungan

def utamaRW(price):
  tamp_rw = 1 * price # 1 x harga tampungan dari kelas semua total KK
  return tamp_rw

def sekunderRT(price):
  tamp_rt = 1 * price # 1 x harga tampungan pipa rt
  return tamp_rt

def total_cost(total_drill, total_pump): ## nanti tambahin sama yang lain
  cost = total_drill + total_pump
  return cost

def pricing_pipe(jum_kk):
  if (jum_kk >= 0) and (jum_kk <= 200):
    #untuk pipa 0.5 cm
    #print("pipa 0.5 cm")
    pipe_price = 2000
  
  elif (jum_kk > 200) and (jum_kk <= 600):
    #untuk pipa 1 cm
    #print(" Pipa 1 cm")
    pipe_price = 4000
  
  elif (jum_kk > 600) and (jum_kk <= 1000):
    #untuk pipa 1.5 cm
    #print("Pipa 1.5 cm")
    pipe_price = 6000
  
  return pipe_price

def pricing_tampung(jum_kk):
  if (jum_kk >= 0) and (jum_kk <= 200):
    #untuk tampungan 1x1 meter
    # print("tampungan 1x1 m")
    tamp_price = 500000
  
  elif (jum_kk >= 200) and (jum_kk <= 600):
    #untuk tampungan 2x2 meter
    # print("tampungan 2x2 m") 
    tamp_price = 1000000
  
  elif (jum_kk > 600) and (jum_kk <= 1000):
    #untuk tampungan 3x3 meter
    # print("tampungan 3x3m")
    tamp_price = 1500000
  
  return tamp_price

# no_rw = 0 #variable no rw
# jum_rt = 0 #variable jumlah rt
# KK = 0 #variable jumlah
# s_min = 0 #kedalaman sumur minimal
# s_max = 0 #kedalaman sumur maksimal
# water_s = Y?N # status air

### Accepting Several User Input ###

print("Welcome to Waterline Pricing")
print("----------------------------")
print("----Input Several Valeus----")
no_rw = input("Nomor RW: ")

jum_rt = int(input("Jumlah RT: "))

#----------- LOOPING RT ----------- #
kk_rt = [] ## variabbel jumlah orang per rt
range_rt = [] ## list masing masing jarak rt
i_rt = [] ## Index RT Ke berapa?

## looping keterangan per rt
for n_rt in range (jum_rt):
  rt_ke = int(input("RT KE: "))
  rt_p = int(input("Jumlah Kepala Keluarga di RT: "))
  r_rt = int(input("Jarak Lingkungan RT: "))

  i_rt.append(rt_ke)
  kk_rt.append(rt_p)
  range_rt.append(r_rt)


###################################

total_kk = sum(kk_rt) 
## !!! Hati hati siapa tau perhitungan bukan dari 
#jumlah seluruh KK, soalnya kan klasifikasi harganya dari sini
#siapa tau beda pipa

#kk = int(input("Kepala Keluarga: "))
print("Jumlah seluruh kepala keluarga: ", total_kk)

s_min = int(input("Kedalaman Sumur Minimal: "))
s_max = int(input("Kedalaman Sumur Maksimal: "))
water_s = input("Status Kekurangan Air (Y/N): ")

jangkauan = total_kk

class_pipe = [] ### List tipe tipe pipa dari jumlah kk rt
class_tampungan = [] ### list tipe tipe tampungan dari jumlah kk rt

print("Pricing list")

# bikin si looping klasifikasi pipe dan tampungan harganya disini

# Classification Pipe
for n in kk_rt:
  p_pipe = pricing_pipe(n)
  class_pipe.append(p_pipe)
  
sekunder_list = [] ## list sekunder dari RT

for t in kk_rt:
  p_tamp = pricing_tampung(n)
  s_tamp = sekunderRT(p_tamp) ## sekunder tampungan
  class_tampungan.append(p_tamp)
  sekunder_list.append(s_tamp)
### Temporary ####
## cuma pengen tau panjang array kelas pipa setelah diklasifikasi
print("Panjang Array Klasifikasi Pipa: ", len(class_pipe))
print("Panjang Array Klasifikasi Tampungan: ", len(class_tampungan))
print("Panjang Array Sekunder: ", len(sekunder_list))
