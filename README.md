# MySQL / MariaDB Backup Script #

### This Backup Script is to take backup of mysql server. ###

* Quick summary

Backup script helps in taking backup of mysql / mariadb database. 
It takes backup of all the databases present on the host server.

If <pre><code>RDB_LIST_LOAD_FROM_DB = True</code></pre> will first create a list of databases present on server and write to the file locally

If you wish to provide your own list of databases to take backup instead of all the databases present on server, give <pre><code>RDB_LIST_SOURCE_FILE</code></pre> path to list file.
NOTE: make sure in this case the <pre><code>RDB_LIST_LOAD_FROM_DB = False</code></pre>

If you wish to take backup on only one database, then give default db to <pre><code>RDB_DEFAULT_DB</code></pre>.
NOTE: make sure in this case the <pre><code>RDB_LIST_LOAD_FROM_DB = False</code></pre>

Give <pre><code>RDB_DESTINATION_DIRECTORY</code></pre> path to where you would like to store your database backup files.

If <pre><code>ZIP_STATUS = True</code></pre>, then it will compress all the backup files.


NOTE: Keep list of all the databases that needs to be ignored while taking backup in <pre><code>RDB_IGNORE</code></pre>


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


### Who do I talk to? ###

* @srahul07
