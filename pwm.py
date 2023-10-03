#importing required libraries
from gpiozero import DistanceSensor, PWMOutputDevice
import time

#GPIO pins
trigger_pin = 17  
echo_pin = 27 
buzzer_pin = 22   

#initializing distance sensor
ultrasonic_sensor = DistanceSensor(trigger=trigger_pin, echo=echo_pin, max_distance=1.0)

#buzzer for pwm control
buzzer = PWMOutputDevice(buzzer_pin)

try:
    while True: 
        time.sleep(0.5)   
             
        distance_cm = ultrasonic_sensor.distance * 100 
        print("Distance (in cm): %.2f" %distance_cm) 
        buzz =  1.0 - (distance_cm / 100)
        print("Buzz: %.2f" % buzz)
        
        #setting buzzer mapped value
        buzzer.value = buzz

except KeyboardInterrupt:
    print("Program Ended") 
