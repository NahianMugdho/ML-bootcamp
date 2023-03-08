# Defining  Trigger and Echo pins
trigger = Pin(13, Pin.OUT)
echo = Pin(22, Pin.IN)
# Defining  Servo pin and PWM object
servoPin = Pin(15)
servo = PWM(servoPin)
duty_cycle = 0 # Defining and initializing duty cycle PWM
# Defining frequency for servo and enable pins
servo.freq(50)
def get_distance():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   dist = (timepassed * 0.0343) / 2
   return dist

#Defining function to set servo angle
def setservo(angle):
    duty_cycle = int(angle*(7803-1950)/180) + 1950
    servo.duty_u16(duty_cycle)

setservo(90)



def auto():
    while True:
        distance=get_distance() #Getting distance in cm
    
    #Defining direction based on conditions
        if distance < 15:
            stop()
            backward()
            time.sleep(1)
            stop()
            time.sleep(0.5)
            setservo(30) #Servo angle to 30 degree
            time.sleep(1)
            right_distance=get_distance()
        #print(right_distance)
            time.sleep(0.5)
            setservo(150) #Servo angle to 150 degree
            time.sleep(1)
            left_distance=get_distance()
        #print(left_distance)
            time.sleep(0.5)
            setservo(90)
        
            if right_distance > left_distance:
                right()
                time.sleep(2)
                stop()
            else:
                left()
                time.sleep(2)
                stop()
        else:
            forward()

        time.sleep(0.5)
        
########

