__author__ = 'rahul'


class MysqlCmd(object):

    def __init__(self):
        pass

    @classmethod
    def getDump(self, zipstatus):
        cmd = "mysqldump -u %s -p%s -h %s -e --opt -c %s > %s/%s.sql"
        if zipstatus:
            cmd = "mysqldump -u %s -p%s -h %s -e --opt -c %s | gzip -c > %s/%s.sql.gz"
        return cmd

    @classmethod
    def getDBStrcture(self, zipstatus):
        cmd = "mysqldump -u %s -p%s -h %s -e -d --opt -c %s > %s/%s.sql"
        if zipstatus:
            cmd = "mysqldump -u %s -p%s -h %s -e -d --opt -c %s | gzip -c > %s/%s.sql.gz"
        return cmd

    @classmethod
    def getDatabaseList(self, zipstatus):
        cmd = "mysql -u %s -p%s -h %s --silent -N -e 'show databases' > %s"
        if zipstatus:
            cmd = "mysql -u %s -p%s -h %s --silent -N -e 'show databases' | gzip -c > %s.gz"
        return cmd