import numpy as np
import math

def cost_pompa(pump_price):
  res_pompa = 1*pump_price
  return res_pompa 

def cost_pipa_tampungan(d_to_rt, price): #pipe price disini pipa kelas rt
  res_pipa_tampungan = d_to_rt  * price # jarak ke RT x harga kelas pipa rt
  return res_pipa_tampungan

def cost_tampungan(total_utama, total_sekunder):
  total_tampungan = total_utama + total_sekunder #total semua dari pipa tampungan
  return total_tampungan

def utamaRW(price):
  tamp_rw = 1 * price # 1 x harga tampungan dari kelas semua total KK
  return tamp_rw

def sekunderRT(price):
  tamp_rt = 1 * price # 1 x harga tampungan pipa rt
  return tamp_rt

def total_cost(t_HPT, t_tampungan, t_drill, t_pump): ## nanti tambahin sama yang lain
  cost = t_HPT + t_tampungan + t_drill + t_pump
  return cost