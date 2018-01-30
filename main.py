#! python3


import subprocess,sys
from Syback import *
from config import *


## Creating class instance ##
full = Fullmode()
helpmenu = Helpmenu()
conf = Settings()

## Cleaning terminal ##
subprocess.call('clear', shell=True)

## Calling help menu ##
help = helpmenu.menu()

## Function to check if dir is a UNC path ##
#def checkdir(dir):
#	if str(args.DIR[0]) == "\\":
#		Ndir = "\\"+"\\"+args.DIR[1:len(args.DIR)]
#		return str(Ndir)
#	else:
#		return str(dir)


## Calling settings window ##
if help.conf_arg == True:
	print("user: %s" % conf.window()) ## ONLY FOR TESTS

## Executing backup FULL ##
#if help.full_opt == True:
	## Applying retention policy before to execute backup ##
#	if str(args.retb_arg) != "None":
#		print(full.retention(checkdir(args.DIR),args.retb_arg))
#		full.make(checkdir(args.DIR),args.user_arg,args.pass_arg,args.db_arg,args.srv_arg)
#		print(full.size(checkdir(args.DIR),args.db_arg))
#		print(full.bkpdate(checkdir(args.DIR),args.db_arg))
#		sys.exit()
#	## Applying retention policy after execute backup ##
#	elif str(args.reta_arg) != "None":
#		full.make(checkdir(args.DIR),args.user_arg,args.pass_arg,args.db_arg,args.srv_arg)
#		print(full.size(checkdir(args.DIR),args.db_arg))
#		print(full.bkpdate(checkdir(args.DIR),args.db_arg))
#		print(full.retention(checkdir(args.DIR),args.reta_arg))
#		sys.exit()
#	## Backup without retention policy ##
#	else:
#		full.make(checkdir(args.DIR),args.user_arg,args.pass_arg,args.db_arg,args.srv_arg)
#		print(full.size(checkdir(args.DIR),args.db_arg))
#		print(full.bkpdate(checkdir(args.DIR),args.db_arg))
#		sys.exit()
### Executing backup TLOG ##
#else:
#	print("Tlog")


#if args.full_opt == False and args.tlog_opt == False:
#	print("You need specify a backup mode [option] on command-line. See syback.py -h for further details.")
#	sys.exit()
#os.system('powershell.exe -command "Start-Sleep -s 100"')