# Golf_Project

Track golf outing events.

This is a Django webapp that tries to provide a easy way to manage golf trips. Typically managing a golf trip can get confusing and complicated. This application will provide a easy way to see who is on the trip, what courses are on the trip, the tee times involved, tracking team competition, and gambling.

The current intent for this proejct is to be used for the golf trip 2023 to understand practical applications, and then will take feedback to build a customer focused product, allowing for customization and a lot more forms for the user to create database objects. The initial version is intended for admin use only.

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
