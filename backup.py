#! python3

import os,time
from datetime import datetime


class Fullmode:

    now = time.time()

    ## Function to make backup FULL ##
    def make(self,dirbkp,user,passw,dbname,server):
        self.dir = dirbkp
        self.user = user
        self.passw = passw
        self.db = dbname
        self.server = server

        return os.system('echo isql -U%s -P%s -S%s -D%s -X -i\"%s\" -o\"%s\log_bkp_full.log\"' % (self.user,self.passw,self.server,self.db,self.dir,self.dir))


    ## Function to delete oldest files of retention policy ##
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
                        return "Deleted: %s" % file ## ONLY FOR TESTS
                        ## os.remove(file)
                else:
                        pass
        return


    ## Function to colect size of backup ##
    def size(self,dir,dbname):
        self.dir = dir
        self.db = dbname

        for file in os.listdir(self.dir):
            os.chdir(self.dir)
            ## Reading size of the {DBNAME} bkp file ##
            if str(self.db) in file:
                ## Size in MB ##
                size = os.stat(file).st_size/1024/1024

                return 'Size: %.0f Mb' % size
        return


    ## Function to colect Datetime of the last backup ##
    def bkpdate(self,dir,dbname):
        self.dir = dir
        self.db = dbname

        for file in os.listdir(self.dir):
            os.chdir(self.dir)
            ## Reading creation date of the {DBNAME} bkp file ##
            if str(self.db) in file:
                cdate = time.ctime(os.stat(file).st_ctime)
                return datetime.strptime(cdate, '%a %b %d %H:%M:%S %Y').strftime('%d/%m/%Y')
        return

