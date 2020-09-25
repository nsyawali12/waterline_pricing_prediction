import numpy as np
import math

def rukun_warga(rt):
  rw += rt + rt
  rw += rw
  return rw

def pengeboran(max_distance, pengeboran_per_meter, pipe_price):
  res_drill = (max_distance * pengeboran_per_meter) + (max_distance * pipe_price)
  return res_drill

def pompa(pump_price):
  res_pompa = 1*pump_price
  return res_pompa 

def harga_pipa_tampungan(d_to_rt, pipe_price): #pipe price disini pipa kelas rt
  res_pipa_tampungan = d_to_rt  * pipe_price # jarak ke RT x harga kelas pipa rt
  return res_pipa_tampungan

def tampungan(res_pipa_tampungan):
  total_tampungan = res_pipa_tampungan #total semua dari pipa tampungan
  return total_tampungan

def utamaRW(pipe_price):
  tamp_rw = 1 * pipe_price # 1 x harga tampungan 
  return tamp_rw

def sekunderRT(rt, pipe_price):
  tamp_rt = 1 * pipe_price # 1 x harga tampungan pipa rt
  return tamp_rt

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
kk = input("Kepala Keluarga: ")
s_min = input("Kedalaman Sumur Minimal: ")
s_max = input("Kedalaman Sumur Maksimal: ")
water_s = input("Status Kekurangan Air (Y/N): ")



