# Histogram
# project-awwards

>[Becky-Nayere](https://github.com/beckynayere)  
  
# Description  
This project allows users to post their projects and repos for other users to rate according to design, usability and content 
##  Live Link  
 Click [View Site]()  to visit the site
  
## Screenshots 
###### Home page
 
 
## User Story  
  
* A user sees an executable that reads the intervals and waits for the incoming insertion and metrics reques.  
* A user can test thus, demonstrate that erroneous inputs in the Histogram definition are flagged. 
* The Histogram must report the input errors in the interval definitions (e.g., invalid intervals, overlapping intervals) in its log. It must be resilient to any error case (by discarding the invalid inputs).

   
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/beckynayere/Histogram/
```
##### Navigate into the folder and install requirements  
 ```bash 
cd project-awwards pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations awwards
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
 
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [nereahhopebecky@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/beckynayere/Project_Awwards/blob/master/LICENSE)  
* Copyright (c) 2023 **Becky Nayere**

