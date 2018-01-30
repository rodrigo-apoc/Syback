DECLARE back_full CURSOR FOR SELECT name FROM master..sysdatabases
GO

DECLARE @date1 datetime
DECLARE @fnamefull varchar(80)
DECLARE @fnamefull2 varchar(80)
DECLARE @fnamefull3 varchar(80)
DECLARE @fdate varchar(20)
DECLARE @fpath varchar(40)
DECLARE @name nvarchar(100)
DECLARE @msg nvarchar (100)
OPEN back_full
        
FETCH NEXT FROM back_full INTO @name

WHILE (@@FETCH_STATUS= 0)
if @name = 'PER'
    BEGIN
        select @fpath = "T:\SYB_BKP\DATA\"
        select @date1 = getdate()
        select @fdate =
            convert(varchar(4),datepart(YY,@date1)) +
            convert(varchar(2),datepart(MM,@date1)) +
            convert(varchar(2),datepart(DD,@date1)) +
            convert(varchar(2),datepart(HH,@date1)) +
            convert(varchar(2),datepart(MI,@date1)) +
            convert(varchar(2),datepart(SS,@date1))

        select @fnamefull = @fpath + 'Full_'+ @name + '_' + @fdate + '.dmp'
        select @fnamefull2 = @fpath + 'Full_'+ @name + '_' + @fdate + '2.dmp'
        select @fnamefull3 = @fpath + 'Full_'+ @name + '_' + @fdate + '3.dmp'
        select @msg = '*** [Globalsys] Iniciando Backup full - Banco '+@name+' ***'
        print @msg
        print dump database @name to @fnamefull stripe on @fnamefull2 stripe on @fnamefull3 with verify=header,compression=2,init
        select @msg = '*** [Globalsys] Finalizando Backup full - Banco '+@name+' ***'
        print @msg

        FETCH NEXT FROM back_full INTO @name
        END
else
    BEGIN
        select @fpath = "T:\SYB_BKP\DATA\"
        select @date1 = getdate()
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
        print dump database @name to @fnamefull with verify=header,compression=2,init
        select @msg = '*** [Globalsys] Finalizando Backup full - Banco '+@name+' ***'
        print @msg

        FETCH NEXT FROM back_full INTO @name
        END

CLOSE back_full
DEALLOCATE CURSOR back_full
GO