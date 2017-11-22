#!/usr/bin/env python3
import subprocess
import re
 
ACPI = subprocess.run(["acpi"], stdout=subprocess.PIPE)

# If dis found in string.
if re.search('Dis', str(ACPI.stdout), re.I) == None:
    DISCHARGING = False
else: 
    DISCHARGING = True

PERCENT = int(re.search(r'\d+(?=%)', str(ACPI.stdout))[0])

# Set battery icon.
if    PERCENT == 100: BATT_ICON = ''
elif  PERCENT  >  65: BATT_ICON = ''
elif  PERCENT  >  40: BATT_ICON = ''
elif  PERCENT  >  15: BATT_ICON = ''
else:                 BATT_ICON = '';

# Set charging icon.

if DISCHARGING: PWR_ICON = '⚡'
else: PWR_ICON = ''

#print('{}{}% {}\n'.format(PWR_ICON, PERCENT, BATT_ICON))
print('{}  {}%  {}\n'.format(BATT_ICON, PERCENT, PWR_ICON))

