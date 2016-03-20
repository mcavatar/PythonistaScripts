# Ago.py
#!/usr/bin/env python

from datetime import datetime
from dateutil.parser import parse
import sys

# The date is given on the command line in American format.
then = parse(sys.argv[1], dayfirst=False, yearfirst=False)
now = datetime.today()

ago = now - then

if sys.argv[0].split('/')[-1] == 'til':
  print -ago.days
else:
  print ago.days