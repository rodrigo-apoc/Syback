#! python3

import argparse,textwrap
import subprocess,sys
from Syback import *

## Creating class instance ##
full = Fullmode()

## Cleaning terminal ##
subprocess.call('clear', shell=True)

## Help menu ##
parser = argparse.ArgumentParser(prog='Syback',formatter_class=argparse.RawDescriptionHelpFormatter,
	description='A Open-source tool to backup Sybase ASE on Windows.',usage=textwrap.dedent('''syback.py [DIR] [option]
e.g: syback.py "C:\\Mybkp\dir\location" -F -U myuserDB -P password -DB MyDBName'''),
	epilog=textwrap.dedent('''Email contact: rodrigof.lops@gmail.com
Source: https://github.com/rodrigo-apoc/Syback
Thank you!'''))
parser.add_argument('DIR',help='Specify the backup directory with double quotes.')
parser.add_argument('-F','--FULL',dest='full_opt',action='store_true',help='Backup Full mode ON.')
parser.add_argument('-T','--TLOG',dest='tlog_opt',action='store_true',help='Backup TLog mode ON.')
parser.add_argument('-U','--USER',dest='user_arg',required=True,help='Specify a user to connect on Sybase ASE. The user must have SA role. e.g: -U sapsa')
parser.add_argument('-P','--PASS',dest='pass_arg',required=True,help='Specify the password of the user.')
parser.add_argument('-DB',dest='db_arg',required=True,help='Specify the Database name to connect.')
parser.add_argument('-S',dest='srv_arg',required=True,help='Specify the Server name (..SYBASE_HOME\sql.ini) to connect.')
parser.add_argument('-R',dest='retb_arg',type=int,help='Specify retention policy in days. Write 0 to no retention policy. This option will delete oldest files BEFORE the backup. To apply retention policy after backup please choose -r instead of -R.')
parser.add_argument('-r',dest='reta_arg',type=int,help='Specify retention policy in days. Write 0 to no retention policy. This option will delete oldest files AFTER the backup. To apply retention policy before the backup please choose -R instead of -r.')

args = parser.parse_args()


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
