#! python3

import argparse,textwrap
import subprocess,sys

subprocess.call('clear', shell=True) ## Change to 'cls' berofe tests


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

args = parser.parse_args()
print(args)






## Variaveis para controle ##
retencao = 0 ## Aqui define a retencao em dias
dir_bkp = r"\\storeonce\DB_Sybase\FIORI\DEV\DATA"
bkpfile = "FID" ## Prefixo utilizado no arquivo de bkp


## Funcao para apagar arquivos com X dias (retencao) ##
#def del_file(dir, retencao):
#        for file in os.listdir(dir):
#                os.chdir(dir)
#                last_write = (now - (os.stat(file).st_mtime))/60/60
#                ## Condicao para NAO apagar o arquivo de Log ##
#                if "log_bkp_full.log" in file:
#                        pass 
#                elif last_write > (retencao * 24):
#                        print("Seria apagado: %s" % file) ## apagar ao fim dos testes
#                        ## os.remove(file)
#                else:
#                        pass


## Funcao para coletar tamanho do arquivo de Bkp principal ##
#def size_file(dir):
#        for file in os.listdir(dir):
#                ## Condicao para coletar tamanho apenas do file principal ##
#                if bkpfile in file:
#                        os.chdir(dir)
#                        size = os.stat(file).st_size/1024/1024
#                        cdate = time.ctime(os.stat(file).st_ctime)
#                        print('Tamanho: %.0f Mb' % size) ## apagar ao fim dos 
#                        d = datetime.strptime(cdate, '%a %b %d %H:%M:%S %Y')
#                        print(d.strftime('%d/%m/%Y'))
#                        ## return size
#                else:
#                        pass

#############################
######## RODANDO BKP ########
#############################
#del_file(dir_bkp,retencao) ## Apagando bkps antigos (retencao) ##
#os.chdir('C:\\') ## Bypass do erro de UNC invalido devido ao bkp estar em REDE. Nao e necessario essa linha caso o bkp esteja local ##
#os.system('isql -Usapsa -Ph4tlevS@P -SFID -DFID -X -i\"\\\StoreOnce\DB_Sybase\FIORI\DEV\scripts\BACKUP_FULL.sql\" -o\"\\\StoreOnce\DB_Sybase\FIORI\DEV\DATA\log_bkp_full.log\"')
#size_file(dir_bkp) ## Coletando tamanho do bkp ##

#os.system('powershell.exe -command "Start-Sleep -s 100"')
