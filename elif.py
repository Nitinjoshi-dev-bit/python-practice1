import time 

time=int(time.strftime('%H'))
if(6<time<=12):
    print("good morning nitin ")


elif(12<time<=18):
    print("good afternoon nitin ji")


elif(18<time<=20):
    print("good evening nitin sir ji")

elif(20<time<=24):
    print("good night nitin sir jii")


else:
    print("ye system to mereko bhi samajh ni aaya ree aaila")