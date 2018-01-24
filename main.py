#! python3

import os
import time
import os.path
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(description='Backup software open-source to Sybase ASE.',usage='%(prog)s /backup/dir [option]')
#parser.add_argument('integers', metavar='N', type=int, nargs='+',
 #                   help='an integer for the accumulator')
#parser.add_argument('--sum', dest='accumulate', action='store_const',
 #                   const=sum, default=max,
  #                  help='sum the integers (default: find the max)')

args = parser.parse_args()



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
