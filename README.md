# Crosswind Component Calculator using Python
A personal project using Python to calculate the crosswind component for pilots.

# Project Overview
In this project, I made use of Python to create a calculator that works out the crosswind component based on the users inputs. The calculator will then tell the pilot if the wind components are within or outside of his/her aircrafts capabilities.

### How To Run The Program:
You need Python 3.6 or above installed. Then, in your terminal, run:
```
 python crosswind_component.py
 ```
 for Windows, or:
 ``` 
 python 3 crosswind_component.py
 ```
 for Mac.

### Program Details:
The programs asks the user the following questions:

* If the runway is wet or dry.
* The runway heading.
* The wind direction.
* The wind speed

From the above inputs, it will then calculate whether the crosswind component is within, or out of, limits for the users aircraft type. The output is also colour coded for easier recognition. Red being out of limits and green being within limits.

# Software Requirements
* Programming Language: Python 3.7.7
* Libraries: math, colorama

# Built With
* [Python 3.7.7](https://www.python.org/) - The programming language used.
* [math](https://docs.python.org/3/library/math.html) - A Python library that was used.
* [colorama](https://pypi.org/project/colorama/) - A Python library that was used, particulary, the init(), Fore, Back and Style modules.

# Issues
* This code is only useful to the user if they are flying a B737-800 type aircraft. More aircraft need to be added, with their crosswind limitations.

# Credits
* [Python Documentation](https://docs.python.org/3/index.html) - Official Python Documentation.
* [Math Documentation](https://docs.python.org/3/library/math.html) - Official Math Documentation.
* [Colorama Documentation](https://pypi.org/project/colorama/) - Official Colorama Documentation.