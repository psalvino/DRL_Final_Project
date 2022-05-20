import datajoint as dj 
import sys


__author__ = "Peter Salvino"
__email__ = "petersalvino2026@u.northwestern.edu"

# DataJoint version details: 
print('DataJoint version:')
print(dj.__version__)

# LogIn configuration:
dj.config['database.host'] = 'vfsmphysiomdb01.fsm.northwestern.edu'
dj.config['database.user'] = 'ward5243user'
dj.config['database.password'] = 'mouseVR&Ca2+'

# Should say: DataJoint connection (connected)... If not, check the LogIn configuration 
print(dj.conn()) 

# Define virtual modules to work with existing schemas
subject = dj.create_virtual_module('subject', 'pintolab_subject') 
behavior = dj.create_virtual_module('behavior', 'pintolab_behavior') 
session = dj.create_virtual_module('session', 'pintolab_session') 

vm = ['subject','behavior','session']
print('List of virutal modules:')
print(vm)