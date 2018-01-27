#! python3


import subprocess,sys
from Syback import *
from config import *


## Creating class instance ##
full = Fullmode()
hh = Help()

print(hh.menu())

## Cleaning terminal ##
subprocess.call('clear', shell=True)


## Function to check if dir is a UNC path ##
def checkdir(dir):
	if str(args.DIR[0]) == "\\":
		Ndir = "\\"+"\\"+args.DIR[1:len(args.DIR)]
		return str(Ndir)
	else:
		return str(dir)


## Checking if user choosed a backup mode FULL or TLOG ##
if args.full_opt == False and args.tlog_opt == False:
	print("You need specify a backup mode [option] on command-line. See syback.py -h for further details.")
	sys.exit()
## Executing backup FULL ##
elif args.full_opt == True:
	## Applying retention policy before to execute backup ##
	if str(args.retb_arg) != "None":
		print(full.retention(checkdir(args.DIR),args.retb_arg))
		full.make(checkdir(args.DIR),args.user_arg,args.pass_arg,args.db_arg,args.srv_arg)
		print(full.size(checkdir(args.DIR),args.db_arg))
		print(full.bkpdate(checkdir(args.DIR),args.db_arg))
		sys.exit()
	## Applying retention policy after execute backup ##
	elif str(args.reta_arg) != "None":
		full.make(checkdir(args.DIR),args.user_arg,args.pass_arg,args.db_arg,args.srv_arg)
		print(full.size(checkdir(args.DIR),args.db_arg))
		print(full.bkpdate(checkdir(args.DIR),args.db_arg))
		print(full.retention(checkdir(args.DIR),args.reta_arg))
		sys.exit()
	## Backup without retention policy ##
	else:
		full.make(checkdir(args.DIR),args.user_arg,args.pass_arg,args.db_arg,args.srv_arg)
		print(full.size(checkdir(args.DIR),args.db_arg))
		print(full.bkpdate(checkdir(args.DIR),args.db_arg))
		sys.exit()
## Executing backup TLOG ##
else:
	print("Tlog")

#os.system('powershell.exe -command "Start-Sleep -s 100"')
