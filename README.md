# Syback
*Syback* is a backup tool for SAP Sybase ASE, to help you on backup rountine.
It is a open-source Python tool, feel free to contribute with the project.
At first, Syback only runs on Windows OS. Perhaps, in future will be implement to others platforms too.

##Usage
You can see this help menu typing `syback -h` or `syback --help`.
```
usage: syback [DIR] [option]
e.g: syback "C:\Mybkp\dir\location" -F -U myuserDB -P password -DB MyDBName

A Open-source tool to backup Sybase ASE on Windows.

positional arguments:
  DIR                   Specify the backup directory with double quotes.

optional arguments:
  -h, --help            show this help message and exit
  -F, --FULL            Backup Full mode ON.
  -T, --TLOG            Backup TLog mode ON.
  -U USER_ARG, --USER USER_ARG
                        Specify a user to connect on Sybase ASE. The user must
                        have SA role. e.g: -U sapsa
  -P PASS_ARG, --PASS PASS_ARG
                        Specify the password of the user.
  -DB DB_ARG            Specify the Database name to connect.
  -R RETB_ARG           Specify retention policy in days. Write 0 to no
                        retention policy. This option will delete oldest files
                        BEFORE the backup. To apply retention policy after
                        backup please choose -r instead of -R.
  -r RETA_ARG           Specify retention policy in days. Write 0 to no
                        retention policy. This option will delete oldest files
                        AFTER the backup. To apply retention policy before the
                        backup please choose -R instead of -r.
```

You can run Syback through:
1. CMD (prompt command)
	- syback "C:\Mybkp\dir\location" -F -U myuserDB -P password -DB MyDBName