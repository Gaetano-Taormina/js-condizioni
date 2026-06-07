# Exercise
* Ask for a grade from 1 to 10. Print "Insufficient" if < 6, "Sufficient" if between 6 and 7, "Good" if between 8 and 9, "Excellent" if 10.

## Reasoning
* read a value 
* check if given value is between 1 and 10 

* if n < 6 print insufficient
    * otherwise if n < 8 print sufficient
        * otherwise if n < 10 print good 
            * otherwise print excellent
