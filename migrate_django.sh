

python golf_coordinator/manage.py makemigrations GolfRound
python golf_coordinator/manage.py makemigrations accounts
python golf_coordinator/manage.py makemigrations Courses
python golf_coordinator/manage.py makemigrations golf_trip
python golf_coordinator/manage.py makemigrations bookie

python golf_coordinator/manage.py makemigrations
python golf_coordinator/manage.py migrate

python golf_coordinator/manage.py loaddata dump_files/accounts_dump.yaml
python golf_coordinator/manage.py loaddata dump_files/courses_dump.yaml
python golf_coordinator/manage.py loaddata dump_files/golf_trip_dump.yaml
python golf_coordinator/manage.py loaddata dump_files/golfround_dump.yaml

python golf_coordinator/manage.py createsuperuser


