import numpy as np
import math

def pengeboran(max_distance, pengeboran_per_meter, price):
  distance_drill = (max_distance * pengeboran_per_meter)
  distance_price = (max_distance * price)
  res_drill = distance_drill + distance_price
  return res_drill