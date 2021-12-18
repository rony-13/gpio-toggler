#!/usr/bin/python3
import sys
import time
import argparse

parser = argparse.ArgumentParser(description='I/O Control')
parser.add_argument("-i", "--input", type=int,help="Select the input")
parser.add_argument("-o", "--output", type=int,help="Select the output")

args = parser.parse_args()
input_pin = args.input
output_pin = args.output

if(input_pin == None or output_pin == None):
    sys.exit('Need to select both Input and Output')

def set_pin_dir(pin_no,pin_dir):
    # Export GPIO as In/Out
    try:
        sysfs_handle = open("/sys/class/gpio/export", "w", 2)
    except Exception as err:
        print(str(err))
        return False

    if (sysfs_handle):
        sysfs_handle.write(f"{pin_no}")
        print(f"GPIO {pin_no} opened for EXPORT")
    else:
        print("Can't open gpio/export.  Something went wrong. Check for root access.")
        sysfs_handle.close()
        return False
    
    # Set In/Out for exported GPIO
    try:
        sysfs_handle = open(f"/sys/class/gpio/gpio{pin_no}/direction", "w")
    except Exception as err:
        print(str(err))
        return False

    if(sysfs_handle):
        sysfs_handle.write(f"{pin_dir}")
        print(f"GPIO pin {pin_no} set as {pin_dir}")
    else:
        print("Can't open gpio/direction. Check for root access.")
        sysfs_handle.close()
        return False

    # Setting Default as turned off
    if(pin_dir=='out')
        sysfs_handle = open(f"/sys/class/gpio/gpio{pin_no}/value", "w")
        if(sysfs_handle):
            sysfs_handle.write("0")
            print(f"GPIO pin {pin_no} is 0")
        else:
            print(f"Can't open gpio{pin_no}/value. ")
            sysfs_handle.close()
            return False
    
    return True

def pin_control(pin_in,pin_out):
    # Input Pin Status Read
    try:
        sysfs_handle = open(f"/sys/class/gpio/gpio{pin_in}/value", "r")
    except Exception as err:
        print(str(err))
        return False

    if(sysfs_handle):
        in_pin_status = sysfs_handle.read()
        print(f"GPIO pin {pin_in} is {in_pin_status}")
    else:
        print(f"Can't read gpio{pin_in}/value.")
        sysfs_handle.close()
        return False

    # Output Pin Current Status Read
    try:
        sysfs_handle = open(f"/sys/class/gpio/gpio{pin_out}/value", "r")
    except Exception as err:
        print(str(err))
        return False

    if(sysfs_handle):
        out_pin_status = sysfs_handle.read()
        print(f"GPIO pin {pin_out} is {pin_status}")
    else:
        print(f"Can't read gpio{pin_in}/value.")
        sysfs_handle.close()
        return False
    
    # PIN Control
    sysfs_handle = open(f"/sys/class/gpio/gpio{pin_out}/value", "w")
    if(sysfs_handle):
        if(in_pin_status==1)
            sysfs_handle.write(f"{int(not(out_pin_status))}")
            print(f"GPIO pin {pin_out} is {int(not(out_pin_status))}")
        else:
            sysfs_handle.write("0")
            print(f"GPIO pin {pin_out} is 0")
    else:
        print(f"Can't open gpio{pin_out}/value. ")
        sysfs_handle.close()
        return False


if __name__ == "__main__":
    set_input = set_pin_dir(input_pin,'in')
    if(set_input):
        set_output = set_pin_dir(output_pin,'out')
    else:
        sys.exit('Could not set input properly')
    if(set_output):
        sys.exit('Could not set output properly')
    # just for simplicity now
    i = 0
    while(i<10):
        success = pin_control(input_pin,output_pin)
        time.sleep(1)
        if(not success):
            break
    print('Finally end for now')
