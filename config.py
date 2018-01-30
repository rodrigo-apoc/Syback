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
			'''\nSource: https://github.com/rodrigo-apoc/Syback\n'''+__copyright__)
		parser.add_argument('-F','--FULL',dest='full_opt',action='store_true',help='Backup Full mode ON.')
		parser.add_argument('-T','--TLOG',dest='tlog_opt',action='store_true',help='Backup TLog mode ON.')
		parser.add_argument('--conf',dest='conf_arg',required=True,action='store_true',help='Open settings window to configure backup.')
		parser.add_argument('--version', action='version', version='%(prog)s 0.1')
		
		args = parser.parse_args()

		return args


class Settings:

	def window(self):

		def layout(self):

			def retention(self):
				app.addLabelOptionBox("Delete", ["After", "Before"], 5, 5)
				app.addLabel("txt1Lab", "backup.", 5, 6)
				app.addEntry("daysEntry", 5, 7, 0, 0)
				app.addLabel("txt2Lab", "day(s).", 5, 8)

			def ok(param):
				if param == True:
					username = app.getEntry("userEntry")
					return username
				else:
					app.stop()
					pass

			def cancel(param):
				app.stop()

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
			app.addLabel("dir1Lab", "Backup FULL Directory:", 5, 0)
			app.addEntry("dir1Entry", 5, 1, 3)
			app.addButton("Enable retention policy", retention, 5, 4)
			app.addLabel("dir2Lab", "Backup TLOG Directory:", 6, 0)
			app.addEntry("dir2Entry", 6, 1, 3)

			## Button ##
			app.addButton("OK", ok, 7, 1, 4)
			app.addButton("Cancel", cancel, 7, 5, 4)

			## Adjustments ##
			app.setFocus("userEntry")
			app.getLabelWidget("title1Lab").config(font="Helvetica 18")
			app.getLabelWidget("title2Lab").config(font="Helvetica 18")

			## GRID VIEW ##
			#app.setLabelBg("header","red")
			#app.getLabelWidget("header").config(font="Helvetica 22")

			app.go()

			return ok(True)

		return layout(True)
