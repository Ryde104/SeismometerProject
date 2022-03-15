import requests
import time
import random

while True:
   
    data = {
        'psi' : str(random.randrange(0, 3500))
    }

    r = requests.post('http://seismic:5000/post', json=data)
    #r = requests.post('http://52.162.94.65:5000/post', json=data)
    
    print (data)
    time.sleep(5)