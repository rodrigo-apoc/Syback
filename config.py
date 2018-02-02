#! python3

import argparse,textwrap
from appJar import gui
from backup import odbc

class Helpmenu:

	def menu(self):
		## Details ##
		__author__ = "Rodrigo Lopes"
		__copyright__ = "Copyright 2018, Rodrigo Lopes | https://github.com/rodrigo-apoc/Syback"
		#__license__ = "Apache 2.0"
		__version__ = "0.1"
		__maintainer__ = "Rodrigo Lopes"
		__email__ = "rodrigof.lops@gmail.com"
		__status__ = "Development"
		#__url__ = ""
		
		## Help menu ##
		parser = argparse.ArgumentParser(prog='Syback',formatter_class=argparse.RawDescriptionHelpFormatter,
			description='A Open-source tool for backup Sybase ASE on Windows.',usage=textwrap.dedent('''syback.py [option] e.g: syback.py --conf "C:\\Myconf\dir\location"'''),
			epilog='''Email contact: '''+__email__+'''\n'''+__copyright__)
		parser.add_argument('--conf',dest='conf_arg',help='Specify config file location to read backup settings before executing.')
		parser.add_argument('--version', action='version', version='%(prog)s 0.1')
		
		args = parser.parse_args()

		return args


class Settings:

	def window(self):

		def retention(self):
			app.addLabelOptionBox("Delete", ["Choose","After", "Before"], 6, 5)
			app.addLabel("txt1Lab", "backup.", 6, 6)
			app.addNumericEntry("daysEntry", 6, 7, 0, 0)
			app.addLabel("txt2Lab", "day(s).", 6, 8)

		def stripe(self):
			app.addNumericEntry("stripeEntry", 7, 5)
			app.addLabel("stripeLb", "Files", 7, 6)

		def compress(self):
			app.addNumericEntry("compressEntry", 8, 1)

		def dbname(self):
			conn = odbc()

			host = app.getEntry("hostEntry")
			user = app.getEntry("userEntry")
			passwd = app.getEntry("passEntry")
			port = app.getEntry("portEntry")
			db = app.getEntry("dbEntry")

			if app.getCheckBox("Encryption") == True:
				encrypt = str(1)
			else:
				encrypt = str(0)

			list = conn.connect(host,user,passwd,port,db,encrypt)
			app.addTickOptionBox("N", list, 8, 5)

		def save(self):
			app.stop()

		def cancel(self):
			app.clearAllEntries(callFunction=False)
			app.clearAllOptionBoxes()
			app.stop()

		def clear(self):
			app.clearAllEntries(callFunction=False)
			app.clearAllOptionBoxes()
		
		## GUI ##
		app = gui(handleArgs=False,title="Settings Window",size="fullscreen")
		app.setBg("lightBlue")

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
		app.addLabel("hostLab", "Host:", 3, 0)
		app.addEntry("hostEntry", 3, 1)
		app.addLabel("portLab", "Port:", 3, 2)
		app.addEntry("portEntry", 3, 3)
		app.addCheckBox("Encryption", 3, 4)

		## Second BLock ##
		app.addLabel("title2Lab", "Backup and Retention", 4, 0, 9)
		app.addHorizontalSeparator(5,0,9)
		app.addLabel("dir1Lab", "Backup FULL Directory:", 6, 0)
		app.addEntry("dir1Entry", 6, 1, 3)
		app.addButton("Retention policy", retention, 6, 4)
		app.addButton("Stripe backup", stripe, 7, 4)
		app.addLabel("dir2Lab", "Backup TLOG Directory:", 7, 0)
		app.addEntry("dir2Entry", 7, 1, 3)
		app.addButton("Compression backup", compress, 8, 0)
		app.addLabel("dbnameLab", "Select Databases to backup:", 8, 2)
		app.addButton("Choose", dbname, 8, 3)

		## Third Block ##
		app.addLabel("title3Lab", "Monitoring", 9, 0, 9)
		app.addHorizontalSeparator(10,0,9)

		## Button ##
		app.addButton("Save", save, 12, 1)
		app.addButton("Cancel", cancel, 12, 2)
		app.addButton("Clear", clear, 12, 3)

		## Adjustments ##
		app.setFocus("userEntry")
		app.getLabelWidget("title1Lab").config(font="Helvetica 18")
		app.getLabelWidget("title2Lab").config(font="Helvetica 18")
		app.getLabelWidget("title3Lab").config(font="Helvetica 18")
		app.addLabel("blank1", "", 11, 0, 9)
		app.setButtonTooltip("Retention policy", "Click here to configure retention policy in Days and choose delete oldest files After or Before backup.")
		app.setButtonTooltip("Stripe backup", "The Backup Server splits the database into approximately equal portions (Max 32), and sends each portion to a different device. Dumps are made concurrently on all devices, reducing the time required to make a dump, and requiring fewer volume changes during the dump.")
		app.setButtonTooltip("Compression backup", "Is a number between 0 and 9, 100, or 101. For single-digit compression levels, 0 indicates no compression, and 9 provides the highest level of compression. Compression levels of 100 and 101 provide a faster, more efficient compression mode, with 100 providing faster compression and 101 providing better compression. RECOMENDED = 2")
		
		## GRID VIEW ##
		#app.setLabelBg("header","red")
		#app.getLabelWidget("header").config(font="Helvetica 22")
		
		app.go()
		
		return app
