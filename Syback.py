#! python3

import os,time
from datetime import datetime

class Fullmode:

    now = time.time()

    ## Function to dele oldest files of retention policy ##
    def retention(self,dirbkp,retention):
        self.dir = dirbkp
        self.ret = retention
        
        for file in os.listdir(self.dir):
                os.chdir(self.dir)
                last_write = (self.__class__.now - (os.stat(file).st_mtime))/60/60
                ## To avoid delete Log file ##
                if "log_bkp_full.log" in file:
                        pass 
                elif last_write > (self.ret * 24):
                        print("Deleted: %s" % file) ## ONLY FOR TESTS
                        ## os.remove(file)
                else:
                        pass
        return


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