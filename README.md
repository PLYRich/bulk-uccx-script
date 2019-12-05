# bulk-uccx-script
bulk uccx add script

Developed on a ubuntu box with python. There are some caveats that I would like to outline. 

test10skills.csv
Format the CSV for each user and substitute a throwaway skill if they require less than 10 skills. 
Meaning, make a skill in UCCX and assign it a name and gather the ID, after the upload I go back in and delete the throwaway skills which
gets bulked removed from each agent. I struggled with a lot of the formatting needed for the API, this worked best in my case. 

listOfNumbers.txt
The list of numbers you are updating, our end user profiles are the same as the phone number. 

assign10skills.py
Reads the CSV
Writes each line of the CSV to another file in correctly formatted .json
Creates the number.json file formatted the way CCX likes. 
I use pandas to create a grid and I format that grid with python to create the formatted .json files to update each CCX account.
This was what made the most sense to me - I did look at other methods to achieve the same result - none of which worked for me. 
This one worked. 
It is commented where each section for the 10 skills begins. 

main.py
you'll need to update...
URL
Username
Password

This takes in the directory of the .json files that were made, and does the delivery to CCX. It has print responses
to find out how the server is accepting each .json file. 


