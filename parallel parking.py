Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> # CODE CELL
#
# Write the park function so that it actually parks your vehicle.

from Car import Car
import time

def park(car):
    #  currently it just drives back and forth
    #  Note that the allowed steering angles are
    #  between -25.0 and 25.0 degrees and the 
    #  allowed values for gas are between -1.0 and 1.0
    
    # inspired from The "S" Method (http://teendriving.com/driving-tips/parking/)
    
    car.gas(-.1)
    time.sleep(.5)
    
    car.steer(25.0)
    time.sleep(3)
    
    car.steer(0)
    time.sleep(2)
    
    car.steer(-25.0)
    time.sleep(1)
    
    car.gas(.1)
    time.sleep(.5)
    car.gas(0)
    
    car.steer(0)
    car.gas(.2)
    car.steer(10)
    time.sleep(1.5)
    car.gas(-.2)
    time.sleep(1)
    car.gas(.1)
    time.sleep(0.5)
    car.gas(0)

car = Car()
park(car)
>>> 
