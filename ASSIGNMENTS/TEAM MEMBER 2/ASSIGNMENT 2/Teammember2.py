import random 
import time 
import winsound 
while (1): 
 temp = random.randint(0,100) 
 humidity = random.randint(0,100) 
 if temp>70:
     print("ALERT!! Detected temperature: "+str(temp)+"°C") 
     duration=5000 
     freq=500 
     winsound.Beep(freq,duration) 
 else: 
     print("ALERT!! stop : "+str(temp)+"°C")
     time.sleep(1)
