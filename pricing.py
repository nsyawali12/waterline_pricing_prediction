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
  
  elif (jum_kk > 200) and (jum_kk <= 600):
    #untuk tampungan 2x2 meter
    # print("tampungan 2x2 m") 
    tamp_price = 1000000
  
  elif (jum_kk > 600) and (jum_kk <= 1000):
    #untuk tampungan 3x3 meter
    # print("tampungan 3x3m")
    tamp_price = 1500000
  
  return tamp_price