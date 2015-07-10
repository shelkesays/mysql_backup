# MySQL / MariaDB Backup Script #

### Backup script helps in taking backup of mysql / mariadb database. ###

* Quick summary

It takes backup of all the databases present on the host server.

If <pre><code>RDB_LIST_LOAD_FROM_DB = True</code></pre> will first create a list of databases present on server and write to the file locally

If you wish to provide your own list of databases to take backup instead of all the databases present on server, give <pre><code>RDB_LIST_SOURCE_FILE  = /path/to/list/file</code></pre>
NOTE: make sure in this case the <pre><code>RDB_LIST_LOAD_FROM_DB = False</code></pre>

If you wish to take backup on only one database, then give default db to <pre><code>RDB_DEFAULT_DB = "default_db"</code></pre>.
NOTE: make sure in this case the <pre><code>RDB_LIST_LOAD_FROM_DB = False</code></pre>

<pre><code>RDB_DESTINATION_DIRECTORY = /path/to/backup/destination/directory</code></pre>

To compress all the backup files,
<pre><code>ZIP_STATUS = True</code></pre>


NOTE: To keep list of all the databases that needs to be ignored while taking backup
<pre><code>RDB_IGNORE = ["mysql", "information_schema", "performance_schema"]</code></pre>


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
