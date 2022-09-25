import time
import os
import math
import RPi.GPIO as GPIO

#gpio setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
hallpin = 2
GPIO.setup(hallpin, GPIO.IN)

#creating a file with the results
count = 1
wantingResults = True
try:
    while wantingResults:
        #getting values from sensors for voltage(V) and current(A)
        voltage = 5
        current = 3
        RPM = 0
        
        #calculations
        resistance = voltage / current
        watts = voltage * current
        
        #calculating RPM of the turbine
        rotation = 0
        start_time = time.time()

        while True:
            if (GPIO.input(hallpin) == 1):
                rotation = (rotation + 1) / 2
                end_time = time.time()
                total_time = start_time - end_time
            if total_time == 60:
                break

            RPM = rotation

        #status of the flow rate
        status = ""
        
        #finding the status of the turbine and the pip flow
        if RPM > 10:
            status = "Flow is Good"
        elif RPM == 0:
            status = "Flow has stopped"
        elif RPM < 10:
            status = "Flow is Bad"
            
        #printing results to a new file
        file_name = "Status" + str(count)
        new_file = open(file_name, "w")
        
        new_file.write("Watts Generated: ")
        new_file.write(str(watts))
        new_file.write("\n")
        
        new_file.write("Voltage Generated: ")
        new_file.write(str(voltage))
        new_file.write("\n")
        
        new_file.write("Resistance Generated: ")
        new_file.write(str(resistance))
        new_file.write("\n")
        
        new_file.write("Current Generated: ")
        new_file.write(str(current))
        new_file.write("\n")
        
        new_file.write("Status of flow: ")
        new_file.write(status)
        new_file.write("\n")
        count = count + 1
        
        print("Operations Complete")
        time.sleep(60)
        wantingResults = False
    
except keyboardInterrupt:
    GPIO.cleanup() #clean up all GPIO