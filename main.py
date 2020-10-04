import numpy as np
import math

### Importing function from other files
from drill import pengeboran
from pricing import pricing_pipe, pricing_tampung
from cost import cost_pipa_tampungan, sekunderRT, utamaRW, cost_tampungan,\
    cost_pompa, total_cost


print("Welcome to Waterline Pricing")
print("----------------------------")
print("---- Input Several Values ----")
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

#----- Classification Pipe -----#
for n in kk_rt:
  p_pipe = pricing_pipe(n)
  class_pipe.append(p_pipe)
#################################

#----- Classification Tampungan -----#  
sekunder_list = [] ## list sekunder dari RT

# Classification Tampungan and Sekunder
for t in kk_rt:
  p_tamp = pricing_tampung(t)
  s_tamp = sekunderRT(p_tamp) ## sekunder tampungan
  class_tampungan.append(p_tamp)
  sekunder_list.append(s_tamp)
#######################################

### Temporary ####

### Tampungan UTAMA ###
### Tampungan kelas RW 
### Kalau mau otomatis harganya, berarti pake dari hasil klasifikasi tampungan kepala keluarga
t_rw = 1500000 
tamp_utama = utamaRW(t_rw) ## Total harga utama
t_2nd = sum(sekunder_list) ## Total Semua harga tampungan sekunder
tampungan = cost_tampungan(tamp_utama, t_2nd)

## cuma pengen tau panjang array kelas pipa setelah diklasifikasi
print("-----------------------------------------------")
print("Panjang Array Klasifikasi Pipa: ", len(class_pipe))
print("Panjang Array Klasifikasi Tampungan: ", len(class_tampungan))
print("Panjang Array Sekunder: ", len(sekunder_list))
print("-----------------------------------------------")

print("-----------------------------------------------")
print("Perhitungan Tampungan Utama & Sekunder ")
### Perhitungan Tampungan
idx_s = 1 ## Buat tau index sekundernya
for nd in sekunder_list:
  print("Tampungan Sekunder Ke", idx_s, ":" , nd)
  idx_s += 1

print("Total Harga Tampungan Sekunder: ", t_2nd)
print("Harga Tampungan Utama: ", tamp_utama)
print("Harga Tampungan: ", tampungan)
print("-----------------------------------------------")

### Perhitungan Harga Pipa Tampungan ###
total_HPT = '' ## temporary nanti di masukkin setelah harga per tampungannya ada
HPT_list = []

print("-----------------------------------------------")
print("Perhitungan Harga Pipa Tampungan")
idx_hpt = 1
for r_rt, c_pipe in zip(range_rt, class_pipe):
  hpt = cost_pipa_tampungan(r_rt, c_pipe)
  print("harga HPT ke ", idx_hpt, ":", hpt)
  HPT_list.append(hpt)
  idx_hpt += 1

total_HPT = sum(HPT_list)
print("Total semua HPT: ", total_HPT)
print("-----------------------------------------------")

#######################################
print("-----------------------------------------------")
print("Perhitungan Harga Pengeboran")
#--- Pengeboran ---#
meter_bor = 100000
p_pipe_for_bor = pricing_pipe(total_kk) ## baru diambil dari klasifikasi pipe, bukan dari kelas pipa utama
total_drill = pengeboran(s_max, meter_bor, p_pipe_for_bor)
print("Total Pengeboran: ", total_drill)

print("-----------------------------------------------")
#------------------#
print("-----------------------------------------------")
print("Perhitungan Pompa")
#--- Pompa ---#
price_pump = 3000000
pump = cost_pompa(price_pump)
total_pump = pump
print("Harga Pompa: ", total_pump)
###############
print("-----------------------------------------------")

print("-----------------------------------------------")
print("Total Biaya")
#--- Total Cost ---#
total_biaya = total_cost(total_HPT, tampungan, total_drill, total_pump)
print("Total Cost Keseluruhan: ", total_biaya)
####################
print("-----------------------------------------------")