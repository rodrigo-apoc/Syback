#! python3

import argparse,textwrap
from appJar import gui

class Helpmenu:

	def menu(self):
		## Details ##
		__author__ = "Rodrigo Lopes"
		__copyright__ = "Copyright 2018, Rodrigo Lopes"
		#__credits__ = [""]
		#__license__ = "Apache 2.0"
		__version__ = "0.1"
		__maintainer__ = "Rodrigo Lopes"
		__email__ = "rodrigof.lops@gmail.com"
		__status__ = "Development"
		#__url__ = ""
		
		
		## Help menu ##
		parser = argparse.ArgumentParser(prog='Syback',formatter_class=argparse.RawDescriptionHelpFormatter,
			description='A Open-source tool for backup Sybase ASE on Windows.',usage=textwrap.dedent('''syback.py [DIR] [option] e.g: syback.py "C:\\Mybkp\dir\location" -F'''),
			epilog='''Author: '''+__author__+
			'''\nEmail contact: '''+__email__+
			'''\nVersion: '''+__version__+
			'''\nSource: https://github.com/rodrigo-apoc/Syback\n'''+__copyright__)
		parser.add_argument('-F','--FULL',dest='full_opt',action='store_true',help='Backup Full mode ON.')
		parser.add_argument('-T','--TLOG',dest='tlog_opt',action='store_true',help='Backup TLog mode ON.')
		parser.add_argument('--conf',dest='conf_arg',required=True,action='store_true',help='Open settings window to configure backup.')

		#parser.add_argument('DIR',help='Specify the backup directory with double quotes.')
		#parser.add_argument('-F','--FULL',dest='full_opt',action='store_true',help='Backup Full mode ON.')
		#parser.add_argument('-T','--TLOG',dest='tlog_opt',action='store_true',help='Backup TLog mode ON.')
		#parser.add_argument('-U','--USER',dest='user_arg',help='Specify a user to connect on Sybase ASE. The user must have SA role. e.g: -U sapsa')
		#parser.add_argument('-P','--PASS',dest='pass_arg',help='Specify the password of the user.')
		#parser.add_argument('-DB',dest='db_arg',help='Specify the Database name to connect.')
		#parser.add_argument('-S',dest='srv_arg',help='Specify the Server name (..SYBASE_HOME\sql.ini) to connect.')
		#parser.add_argument('-R',dest='retb_arg',type=int,help='Specify retention policy in days. Write 0 to no retention policy. This option will delete oldest files BEFORE the backup. To apply retention policy after backup please choose -r instead of -R.')
		#parser.add_argument('-r',dest='reta_arg',type=int,help='Specify retention policy in days. Write 0 to no retention policy. This option will delete oldest files AFTER the backup. To apply retention policy before the backup please choose -R instead of -r.')
		#parser.add_argument('--conf',dest='conf_arg',required=True,action='store_true',help='Open settings window to configure backup.')
		
		args = parser.parse_args()

		return args


class Settings:

	def window(self):

		def retention(btn):
			app.addLabelOptionBox("Delete", ["After", "Before"], 5, 5)
			app.addLabel("txt1Lab", "backup.", 5, 6)
			app.addEntry("daysEntry", 5, 7, 0, 0)
			app.addLabel("txt2Lab", "day(s).", 5, 8)

		## GUI ##
		app = gui(handleArgs=False,title="Settings Window")#,size="fullscreen")
		app.setBg("lightBlue")

		## Header ##
		#app.addLabel("header","Settings page of Syback. All informations will be saved on instalation directory.",0,0,3)

		## First Block ##
		app.addLabel("title1Lab", "Connection", 0, 0, 9)
		app.addHorizontalSeparator(1,0,9)
		app.addLabel("userLab", "Username:", 2, 0)
		app.addEntry("userEntry", 2, 1)
		app.addLabel("passLab", "Password:", 2, 2)
		app.addSecretEntry("passEntry", 2, 3)
		app.addLabel("dbLab", "DBName:", 2, 4)
		app.addEntry("dbEntry", 2, 5)
		app.addLabel("srvLab", "Server:", 2, 6)
		app.addEntry("srvEntry", 2, 7)
		app.addCheckBox("Encryption", 2, 8)

		## Second BLock ##
		app.addLabel("title2Lab", "Backup and Retention", 3, 0, 9)
		app.addHorizontalSeparator(4,0,9)
		app.addLabel("dirLab", "Backup Directory:", 5, 0)
		app.addEntry("dirEntry", 5, 1, 3)
		app.addButton("Enable retention policy", retention, 5, 4)

		## Adjustments ##
		app.setFocus("userEntry")
		app.getLabelWidget("title1Lab").config(font="Helvetica 18")
		app.getLabelWidget("title2Lab").config(font="Helvetica 18")

		## GRID VIEW ##
		#app.setLabelBg("header","red")
		#app.getLabelWidget("header").config(font="Helvetica 22")

		app.go()

