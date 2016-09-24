# dbf_helper

* Currently, it just reads everything to VARCHAR(255)

# Requirements

* Python 2.7+ (I suggest 2.7.12)
* DBFPy: http://dbfpy.sourceforge.net/

# Using

* You need to alter file to set table_name. Ex: table_name = 'MY_TABLE'
* python dbf_helper.py

# How it works

* It searches for files in the 'dbf_files_path', reads them and creates SQL files.