from colorama import init
init()
from colorama import Fore, Back, Style
import math

# Function to check if the runway is dry or wet
def dry_or_wet():
    runway_condition = str(input("Runway Dry? (Y/N): ")).lower().strip()
    try:
        if runway_condition == 'y':
            return True
        elif runway_condition == 'n':
            return False
        else:
            print('Invalid Input')
            return dry_or_wet()
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return dry_or_wet()
        

# Global Variables
runway_condition = dry_or_wet()
max_dry_xwind = 35
max_wet_xwind = 25
max_tailwind = -10
runway_heading = int(input("Runway Heading: "))
wind_direction = int(input("Wind Direction: "))
wind_speed = int(input("Wind Speed: "))
angle = 0


# Function to work out difference between runway heading and wind direction
def get_difference(runway_heading, wind_direction):
	angle = (wind_direction - runway_heading) % 360.0
	if angle >= 180.0:
		angle -= 360.0
	return angle

# Getting the angle between runway heading and wind direction
wind_angle = get_difference(runway_heading, wind_direction)

# Working out the crosswind and headwind component
crosswind_component_raw = wind_speed * math.sin(math.radians(wind_angle))
crosswind_component = abs(round(crosswind_component_raw))
headwind_component = wind_speed * math.cos(math.radians(wind_angle))

# Checks runway condition and converts negative value to positive and rounds value up to whole number
if runway_condition == True and crosswind_component < max_dry_xwind or runway_condition == False and crosswind_component < max_wet_xwind:
    print("Crosswind Component:", crosswind_component, "kts -", end = " ")
    print(Fore.GREEN + Back.BLACK + Style.BRIGHT + "WITHIN LIMITS.")
    print(Style.RESET_ALL)
else:
    print("Crosswind Component:", crosswind_component, "kts -", end = " ")
    print(Fore.RED + Back.BLACK + Style.BRIGHT + "OUT OF LIMITS.")
    print(Style.RESET_ALL)

# Checks for headwind or tailwind and prints result
if headwind_component < max_tailwind:
    print("Tailwind Component:", abs(round(headwind_component)), "kts -", end = " ")
    print(Fore.RED + Back.BLACK + Style.BRIGHT + "OUT OF LIMITS.")
    print(Style.RESET_ALL)
elif headwind_component < 0:
    print("Tailwind Component:", abs(round(headwind_component)), "kts -", end = " ")
    print(Fore.GREEN + Back.BLACK + Style.BRIGHT + "WITHIN LIMITS.")
    print(Style.RESET_ALL)
else:
    print("Headwind Component:", abs(round(headwind_component)), "kts.")