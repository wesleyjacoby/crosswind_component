from colorama import init
init()
from colorama import Fore, Back, Style
import math


# Global variables for B737-800 aircraft type
max_dry_xwind = 35
max_wet_xwind = 25
max_tailwind = -10
angle = 0.0


def dry_or_wet():
    """
    Asks the user if the runway is dry

    Returns:
        True or False (bool) - depends on the users input
    """
    runway_condition = input("Runway Dry? (Y/N): ").lower().strip()
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
        

def parameters():
    runway_heading = int(input('Runway Heading: '))
    wind_direction = int(input('Wind Direction: '))
    wind_speed = int(input('Wind Speed: '))
    return runway_heading, wind_direction, wind_speed


# Function to work out difference between runway heading and wind direction
def get_difference(runway_heading, wind_direction):
	angle = (wind_direction - runway_heading) % 360.0
	if angle >= 180.0:
		angle -= 360.0
	return angle


def get_components(runway_heading, wind_direction, wind_speed):
    # Getting the angle between runway heading and wind direction
    wind_angle = get_difference(runway_heading, wind_direction)

    # Working out the crosswind and headwind component
    crosswind_component_raw = wind_speed * math.sin(math.radians(wind_angle))
    crosswind_component = abs(round(crosswind_component_raw))
    headwind_component = wind_speed * math.cos(math.radians(wind_angle))
    return crosswind_component, headwind_component


def user_interface(runway_condition, crosswind_component, headwind_component):
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


def main():
    while True:
        runway_condition = dry_or_wet()
        runway_heading, wind_direction, wind_speed = parameters()

        get_difference(runway_heading, wind_direction)
        crosswind_component, headwind_component = get_components(runway_heading, wind_direction, wind_speed)
        user_interface(runway_condition, crosswind_component, headwind_component)

        restart = input('Would you like to restart (Y/N): ').strip().lower()
        if restart == 'y' or restart == 'yes':
            continue
        else:
            print('Program terminating...')
            break


if __name__ == "__main__":
    main()