#! python3

import argparse,textwrap,platform,sys,subprocess,os,time,pyodbc
import xml.etree.cElementTree as ET

## Configurando ambiente ##
if platform.system() != "Windows":
	print("Este programa não suporta o sistema *%s*." % platform.system())
	sys.exit()
else:
	pass

path = "C:\Program Files\syback"
config = False

while config == False:
	if "syback.exe" in os.listdir(path):
		if "infologin.xml" in os.listdir(path):
			os.chdir(path)
			tree = ET.parse('infologin.xml')
			root = tree.getroot()
			config = True
		else:
			print("## Informações de Login ##")
			host = input("IP do servidor: ")
			port = input("Porta: ")
			user = input("User (sa, sapsa ou outro que tenha permissão para executar backup): ")
			passwd = input("Password: ")
			db = input("Base para logar (default: saptools): ")
			encrypt = input("Criptografar password (0 para não, 1 para sim): ")

			root = ET.Element("login")
			dados = ET.SubElement(root, "dados")

			ET.SubElement(dados, "host").text = host
			ET.SubElement(dados, "port").text = port
			ET.SubElement(dados, "user").text = user
			ET.SubElement(dados, "passwd").text = passwd
			ET.SubElement(dados, "db").text = db
			ET.SubElement(dados, "encrypt").text = encrypt

			tree = ET.ElementTree(root)
			os.chdir(path)
			tree.write("infologin.xml")
			os.system("attrib +H infologin.xml")
			os.system('setx PATH "%sPATH%s;%s"' % ("%","%",path))
	else:
		path = input("Digite o diretório de instalação do programa: ")
		os.chdir(path)

subprocess.call('cls', shell=True)

## Help menu ##
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
	description='Ferramenta para backup Sybase.',
	usage=textwrap.dedent('''syback [DIR] [option]
e.g: sb "C:\\Mybkp\dir\location" -F -r 1'''),)
parser.add_argument('DIR',help='Diretório do backup. Com aspas duplas')
parser.add_argument('-F', '--FULL', dest='full_arg', action='store_true', help='Realizar backup Full.')
parser.add_argument('-T', '--TLOG', dest='tlog_arg', action='store_true', help='Realizar backup TLOG.')
parser.add_argument('-r', dest='antes_arg', type=int, help='Aplicar retenção ANTES de fazer o backup.')
parser.add_argument('-R', dest='depois_arg', type=int, help='Aplicar retenção DEPOIS de fazer o backup.')

args = parser.parse_args()

now = time.time()

def checkdir(dir):
	if str(dir[0]) == "\\":
		Ndir = "\\"+dir[1:len(dir)]
		return str(Ndir)
	else:
		return str(dir)

def retention(dirbkp,retention):
	for file in os.listdir(dirbkp):
		os.chdir(dirbkp)
		last_write = (now - (os.stat(file).st_mtime))/60/60
		if "log_bkp_full.log" in file:
			pass
		elif last_write > (retention * 24):
			print("Deletado: %s" % file)
			## os.remove(file)
		else:
			pass

def makeFull(host,user,passwd,port,db,encrypt,dirbkp):
	cnxn = pyodbc.connect('Provider=ASEOLEDB;Driver=Adaptive Server Enterprise;Server=%s;uid=%s;pwd=%s;Port=%s;Catalog=%s;EncryptPassword=%s;' % (host,user,passwd,port,db,encrypt))
	cnxn.setencoding(encoding='utf-8')
	cursor = cnxn.cursor()
	query = textwrap.dedent("""
		DECLARE back_full CURSOR FOR SELECT name FROM master..sysdatabases

		DECLARE @date1 datetime
		DECLARE @fnamefull varchar(80)
		DECLARE @fdate varchar(20)
		DECLARE @fpath varchar(40)
		DECLARE @name nvarchar(100)
		DECLARE @msg nvarchar (100)
		DECLARE @db nvarchar (50)
		OPEN back_full

		FETCH NEXT FROM back_full INTO @name

		WHILE (@@FETCH_STATUS= 0)
		BEGIN
			select @fpath = ?
			select @date1 = getdate()
			select @db = db_name()
			select @fdate =
				convert(varchar(4),datepart(YY,@date1)) +
				convert(varchar(2),datepart(MM,@date1)) +
				convert(varchar(2),datepart(DD,@date1)) +
				convert(varchar(2),datepart(HH,@date1)) +
				convert(varchar(2),datepart(MI,@date1)) +
				convert(varchar(2),datepart(SS,@date1))
		select @fnamefull = @fpath + 'Full_'+ @name + '_' + @fdate + '.dmp'
		select @msg = '*** [Globalsys] Iniciando Backup full - Banco '+@name+' ***'
		print @msg
		print dump database @name to @fnamefull with verify=header,compression=101,init
		select @msg = '*** [Globalsys] Finalizando Backup full - Banco '+@name+' ***'
		print @msg
		FETCH NEXT FROM back_full INTO @name
		END

		CLOSE back_full
		DEALLOCATE CURSOR back_full
		GO
	""")
	os.chdir(dirbkp)
	if "log_bkp_full.log" in os.listdir():
		with open("log_bkp_full.log",'w') as logfile:
			for line in cursor.execute(query, dirbkp).fetchall():
				logfile.write(str(line))
			logfile.close()
	else:
		open("log_bkp_full.log",'w').close()
		with open("log_bkp_full.log",'w') as logfile:
			for line in cursor.execute(query, dirbkp).fetchall():
				logfile.write(str(line))
			logfile.close()


if args.full_arg == False and args.tlog_arg == False:
	print("Você precisa especificar um modo de backup [option] na linha de comando. Veja syback -h para mais detalhes.")
	sys.exit()
elif args.full_arg == True:
	if args.antes_arg != None:
		print(retention(checkdir(args.DIR),args.antes_arg))
		makeFull(root[0][0].text,root[0][2].text,root[0][3].text,root[0][1].text,root[0][4].text,root[0][5].text,checkdir(args.DIR))
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