import numpy as np
import math

def rukun_warga(rt):
  rw += rt + rt
  rw += rw
  return rw

def pengeboran(max_distance, pengeboran_per_meter, price):
  res_drill = (max_distance * pengeboran_per_meter) + (max_distance * price)
  return res_drill

def pompa(pump_price):
  res_pompa = 1*pump_price
  return res_pompa 

def harga_pipa_tampungan(d_to_rt, price): #pipe price disini pipa kelas rt
  res_pipa_tampungan = d_to_rt  * price # jarak ke RT x harga kelas pipa rt
  return res_pipa_tampungan

def tampungan(res_pipa_tampungan):
  total_tampungan = res_pipa_tampungan #total semua dari pipa tampungan
  return total_tampungan

def utamaRW(price):
  tamp_rw = 1 * price # 1 x harga tampungan 
  return tamp_rw

def sekunderRT(rt, price):
  tamp_rt = 1 * price # 1 x harga tampungan pipa rt
  return tamp_rt

def allprice(price):
  all_p =+ price
  return all_p

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
jum_rt = input("Jumlah RT: ")
kk = int(input("Kepala Keluarga: "))
s_min = int(input("Kedalaman Sumur Minimal: "))
s_max = int(input("Kedalaman Sumur Maksimal: "))
water_s = input("Status Kekurangan Air (Y/N): ")

## Jangkauan layanan = Jumlah kapasitas kepala keluarga
jangkauan = kk 

## PRicing dari database jumlah KK
print('Pricing')
if (kk >= 0) and (kk <= 200):
  print('Pipa 0.5m')
  pipe_price = 2000
  print('tampungan 1x1m')
  t_price = 500000
  

elif (kk > 200) and (kk <= 600):
  print('Pipa 1m')
  pipe_price = 4000
  print('tampungan 2x2m')
  t_price = 1000000

  
elif (kk > 600) and (kk<1000):
  print('Pipa 1.5')
  price = 6000
  print('tampungan 3x3m')
  t_price = 1500000

## database harga diluar kondisi
## seperti harga permeter
meter_bor = 100000 ## harga pengeboran per meternya
pompa = 3000000 ## harga satuan pompa

## Main Calculation

p_pengeboran = ''
pipe_uses = ''






print('Output Prediksi Harga')

print("Lokasi Sumur: ", no_rw)
print("Jangkauan Layanan: ", jangkauan)