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
  res_pipa_tampungan = d_to_rt * pipe_price
  return res_pipa_tampungan

print("Welcome to Waterline Pricing")
