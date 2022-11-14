# Friday_technical_task

The project contains two python files. The functions.py contains all the necessary functions to transform the string into  a json object. The second file whichcis main.py will help to run some test cases from the text file "address.txt" to show case the correctness of the solution

## Asumption made regarding the address formats are as follows
 - The street name has more alphabetic letter than the housename
 - The string will only contain street name and house name
 
 ## steps in processing
  - removing un wanted characters like (,!,? etc
  - checking for simple scenarios where the string contains only two words seperated by space or comma
  - in more complexe cases we check for the presons of the number and we use it to determine the house number by looking at the substring before and after the number the street name should contain more alpahabetic characters
  
  
  
No need to install any python packages
Run main.py code will print results on the stdout terminal.
