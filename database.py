import os
import gzip
import config as settings
from backupconfig import BackupConfig
from command import MysqlCmd


def create_db_list_from_command(dblistcmd):
    os.system(dblistcmd % (settings.RDB_USER, settings.RDB_PASSWORD,
                           settings.RDB_HOST, settings.RDB_LIST_SOURCE_FILE))


def get_db_list_from_file(sourcefile):
    dblist = []
    with open(sourcefile, 'rb') as listfile:
        if sourcefile.endswith(".gz"):
            listfile = gzip.open(sourcefile)
        dblist = [line.rstrip() for line in listfile]
    return dblist


def backup_database():
    backup = BackupConfig()
    todaybackuppath = backup.getDestination(settings.RDB_DESTINATION_DIRECTORY)
    backup.createPath(todaybackuppath)

    rdblistfile = settings.RDB_LIST_SOURCE_FILE
    if settings.ZIP_STATUS:
        rdblistfile = settings.RDB_LIST_SOURCE_FILE + ".gz"

    if backup.isMultiBackup(rdblistfile, settings.RDB_DEFAULT_DB):
        dblist = get_db_list_from_file(rdblistfile)
        for database in dblist:
            if database in settings.RDB_IGNORE:
                continue
            else:
                dumpcmd = MysqlCmd.getDump(settings.ZIP_STATUS) % \
                          (settings.RDB_USER, settings.RDB_PASSWORD, settings.RDB_HOST, database, todaybackuppath, database)
                os.system(dumpcmd)
                dumpcmd = MysqlCmd.getDBStrcture(settings.ZIP_STATUS) % \
                          (settings.RDB_USER, settings.RDB_PASSWORD, settings.RDB_HOST, database, todaybackuppath, database)
                os.system(dumpcmd)
    else:
        database = settings.RDB_DEFAULT_DB
        dumpcmd = MysqlCmd.getDump(settings.ZIP_STATUS) % (settings.RDB_USER, settings.RDB_PASSWORD, settings.RDB_HOST, database, todaybackuppath, database)
        os.system(dumpcmd)
    print "Your backups has been created in '" + todaybackuppath + "' directory"


db_list_created = False
if settings.RDB_LIST_LOAD_FROM_DB:
    print "Creating database list from command and storing in file."
    create_db_list_from_command(MysqlCmd.getDatabaseList(settings.ZIP_STATUS))
    db_list_created = True
else:
    # load from file or from default database from configurations
    ## NOTE: check configurations file for file path
    pass

print "Database backup started"
backup_database()

if db_list_created:
    print "Deleting database list file"
    if settings.ZIP_STATUS:
        os.remove(settings.RDB_LIST_SOURCE_FILE + ".gz")
    else:
        os.remove(settings.RDB_LIST_SOURCE_FILE)
print "Backup script completed"