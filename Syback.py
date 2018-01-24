#! python3

import os
import time
from datetime import datetime

class BkpFull:

    now = time.time()

    def del_file(self,dirbkp,retencao):
        self.dir = dirbkp
        self.ret = retencao
        
        for file in os.listdir(dir):
                os.chdir(dir)
                last_write = (now - (os.stat(file).st_mtime))/60/60
                ## Condicao para NAO apagar o arquivo de Log ##
                if "log_bkp_full.log" in file:
                        pass 
                elif last_write > (ret * 24):
                        print("Seria apagado: %s" % file) ## apagar ao fim dos testes
                        ## os.remove(file)
                else:
                        pass