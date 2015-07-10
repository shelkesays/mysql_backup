# MySQL / MariaDB Backup Script #

### This Backup Script is to take backup of mysql server. ###

* Quick summary

Backup script helps in taking backup of mysql / mariadb database. 
It takes backup of all the databases present on the host server.

If "RDB_LIST_LOAD_FROM_DB" is True, this will first create a list of databases present on server and write to the file locally

If you wish to provide your own list of databases to take backup instead of all the databases present on server, give "RDB_LIST_SOURCE_FILE" path to list file.
NOTE: make sure in this case the "RDB_LIST_LOAD_FROM_DB" is False

If you wish to take backup on only one database, then give default db to "RDB_DEFAULT_DB".
NOTE: make sure in this case the "RDB_LIST_LOAD_FROM_DB" is False

Give "RDB_DESTINATION_DIRECTORY" path to where you would like to store your database backup files.

If "ZIP_STATUS" is True, it will compress all the backup files.


NOTE: Keep list of all the databases that needs to be ignored while taking backup in "RDB_IGNORE"


* Version
V0.1

### How do I get set up? ###

* Summary of set up

Need python

* Configuration

Update the details in config.py file

* Dependencies

No dependancies. It completely runs on os.system

* Database configuration

Make sure the database user provided in config.py file has access to all the databases or atleast to the databases whose backup needs to be taken.

* How to run tests

python database.py 

* Deployment instructions

python database.py 


### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* @srahul07
