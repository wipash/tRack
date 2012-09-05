#!/bin/bash
rm -rf /home/seanmcg/dev/tRack/track/db/track.db
touch /home/seanmcg/dev/tRack/track/db/track.db
python manage.py syncdb 
