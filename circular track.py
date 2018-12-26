Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> from Car import Car
import time
%%HTML
<button id="launcher">Launch Car Simulator</button>
<script src="setupLauncher.js"></script>
Launch Car Simulator

<script src="setupLauncher.js"></script>
def circle(car):
    car.steer(5)
    car.gas(0.50)
    
car = Car()

circle(car)
