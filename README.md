# Golf_Project

Track golf outing events.

This is a Django webapp that tries to provide a easy way to manage golf trips. Typically managing a golf trip can get confusing and complicated. This application will provide a easy way to see who is on the trip, what courses are on the trip, the tee times involved, tracking team competition, and gambling.

The current intent for this proejct is to be used for the golf trip 2023 to understand practical applications, and then will take feedback to build a customer focused product, allowing for customization and a lot more forms for the user to create database objects. The initial version is intended for admin use only.

Page Overview:
![image](https://user-images.githubusercontent.com/11196366/227744291-dc32ff18-d3f1-4623-a9bf-09dd168571c6.png)


Primary Technologies:

* Django
* Bootstrap5
* Jquery
* **Installation requirements:
  * **Required linux packages
    * libpq-dev
    * python3-dev
  * Install requirements.txt file for the necessary python packages
    * pip3 install -r requirements.txt


AppOverview

* accounts - intended to handle authentication (currently not implemented)
* courses - lists the courses and their tee characteristics
* golf_trip - Core application that is responsible for the trip
* GolfRound - Handles process gross and net scores for a round
* teams - not in use

Custom and Points of Interest

* golf_trip
* GolfRound
  * round_processing
    * Whenever a round score is submitted, this file is used to ingest the player's scores, the tee/course characteristics, the gametype, and team information. If anything is going wrong with processing, it's here.
  * templatetags/index.py
    * Custom django template filter. This was required because theres a lot of nested lists, and this makes it much easier to display the data in django  templates
    



Current pages:

* Course List
![image](https://user-images.githubusercontent.com/11196366/227752211-11a85f69-da64-43f5-a51f-888079209187.png)


* Scoreboard
![image](https://user-images.githubusercontent.com/11196366/227752138-fe7e815b-ec9e-4720-830d-3285aa751849.png)


* Players list 
![image](https://user-images.githubusercontent.com/11196366/227752146-d8a017b5-2df6-4fda-8a8a-53b9f7002a64.png)

* Trip Schedule
![image](https://user-images.githubusercontent.com/11196366/227752158-26a299a5-0938-45e5-aa8f-03d9b669bdb5.png)


* Tee Time Schedule
![image](https://user-images.githubusercontent.com/11196366/227752165-9ac4706e-34d3-45f0-83af-669531f29ce4.png)

* Completed Round View:
![image](https://user-images.githubusercontent.com/11196366/227752180-bcac27a0-ecc0-4463-9da2-6ea48965c44d.png)
