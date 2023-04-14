

python golf_coordinator/manage.py makemigrations GolfRound
python golf_coordinator/manage.py makemigrations accounts
python golf_coordinator/manage.py makemigrations Courses
python golf_coordinator/manage.py makemigrations golf_trip
python golf_coordinator/manage.py makemigrations bookie

python golf_coordinator/manage.py makemigrations
python golf_coordinator/manage.py migrate
python golf_coordinator/manage.py runserver