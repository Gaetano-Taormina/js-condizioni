# Exercise
* An amusement park requires a minimum height of 140cm and at least 14 years of age for the rollercoaster. Ask the user for this data and print if they can access the rollercoaster.

## Reasoning v1.0
* request height
* request age

* use if to check the requirements
* if the requirements are not met use an alert to indicate the lack of minimum requirements

## Reasoning v1.1
* request age
    * if age is under 14 do not request height

* after checking age and finding the minimum age, request height
    * if height is under 140 cm declare the user's lack of requirements
