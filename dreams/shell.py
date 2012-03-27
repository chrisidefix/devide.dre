# Start an appropriate shell according to the OS name
import os
if os.name == 'nt':
    os.system('cmd')
    
else:
    old_ps1 = os.environ.get('PS1', '')
    os.environ['PS1'] = '[DRE] \u@\h:\w\$ '
    os.system("bash --norc")
    os.environ['PS1'] = old_ps1
    
