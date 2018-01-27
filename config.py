#! python3

import argparse,textwrap
from appJar import gui

## Details ##
__author__ = "Rodrigo Lopes - Hele"
__copyright__ = "Copyright 2018, Hele"
#__credits__ = [""]
#__license__ = "Apache 2.0"
__version__ = "0.1"
__maintainer__ = "Rodrigo Lopes"
__email__ = "rodrigof.lops@gmail.com"
__status__ = "Development"
#__url__ = ""

## Help menu ##
parser = argparse.ArgumentParser(prog='Syback',formatter_class=argparse.RawDescriptionHelpFormatter,
	description='A Open-source tool for backup Sybase ASE on Windows.',usage=textwrap.dedent('''syback.py [DIR] [option]
		e.g: syback.py "C:\\Mybkp\dir\location" -F'''),
	epilog='''Author: '''+__author__+
	'''\nEmail contact: '''+__email__+
	'''\nVersion: '''+__version__+
	'''\nSource: https://github.com/rodrigo-apoc/Syback\n'''+__copyright__)
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
		

app = gui(handleArgs=False)

## Layout config ##
app.setTitle("Config Window")
app.setSize("fullscreen")

## Header ##
app.addLabel("header","Settings page of Syback. All informations will be saved on instalation directory.",0,0,3)

## Informations ##
app.addLabelEntry("Username: ")

## GRID VIEW ##
app.setLabelBg("header","red")
app.getLabelWidget("header").config(font="Helvetica 22")
app.setLabelBg("Username: ","blue")

app.go()