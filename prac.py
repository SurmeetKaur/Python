class Timer:

  def __init__(self , hh=0 , mm=0 ,ss=0):
    self.hh = hh
    self.mm = mm
    self.ss = ss

  def __str__(self):
       hh,mm,ss = str(self.hh),str(self.mm),str(self.ss)
       if self.hh < 10 : hh = '0'+hh
       if self.mm < 10 : mm = '0'+mm
       if self.ss < 10 : ss = '0'+ss
       return (hh+":"+mm+":"+ss)

  def next_second(self):
      self.ss += 1;
      if self.ss >= 60 : self.ss -= 60 ; self.mm += 1
      if self.mm >= 60 : self.mm -= 60 ; self.hh += 1
      if self.hh >= 24 : self.hh -= 24
  def prev_second(self):
       if self.ss > 1 : self.ss -=1
       else :
         self.ss = 59
       if self.mm > 1 : self.mm-= 1
       else :
        self.mm = 59
       if self.hh > 1 : self.hh -= 1
       else : self.hh= 23




timer = Timer(23, 8, 9)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
