# Exercise

* Ask the age and gender ("M" or "F"). If it is a man and has >= 67 years or a woman and has >= 62 years, print "You can retire", otherwise "You still have to work".

## Reasoning

* gender initialization
* do
  * read gender from user;
  * declaration of two arrays for M and F;
  * if array M includes;
    * g gets M as value
  * otherwise if array F includes;
    * g gets F as value;
* while to correct the user in case of incorrect terms for gender;

* read user age;
* if gender === M && age >= 67 || gender === F && age >= 62
  * print you can retire;
* else
  * print you still have to work.
