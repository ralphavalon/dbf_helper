__author__ = 'Raphael Amoedo' #a.k.a. Ralph Avalon

import os
from dbfpy import dbf

columns = ''
table_name = 'TABLE_NAME'
create_table = 'CREATE TABLE ' + table_name + ' ('
drop_table = 'DROP TABLE ' + table_name + ';'
sql_list = []
dbf_files_path = './'

for _file in os.listdir(dbf_files_path):
    if _file.endswith(".dbf"):
        print _file
        db = dbf.Dbf(dbf_files_path + '/' + _file)        

        #Get Columns
        if not columns:
            for rec in db.fieldNames:
                create_table += rec + ' VARCHAR(255),'
                columns += rec + ','
                
            columns = columns[:-1]
            create_table = create_table[:-1] + ');'

        #Get Inserts
        for rec in db:
            values = []
            sql = 'INSERT INTO ' + table_name + '(' + columns + ') VALUES ('
            for value in rec:
                values.append("'" + str(value) + "'")
            sql += ','.join(values)
            sql += ');'
            sql_list.append(sql)

        #print '-----------------'
        #print '--CREATE TABLE---'
        #print '-----------------'
        #print create_table

        #print '-----------------'
        #print '--INSERT INTO----'
        #print '-----------------'
        #print sql_list

i = 0
f = None
for index in range(len(sql_list)):
    if (index % 35000) == 0:
        i += 1
        if f:
        #    f.write('GO\n')  # SQL Server
            f.close() # you can omit in most cases as the destructor will call it
        f = open(table_name.lower() +'-' + str(i) + '.sql','w')
        if i == 1:
            #f.write(drop_table + '\n') # Drop line if needed
            f.write(create_table + '\n')
    f.write(sql_list[index] + '\n') # python will convert \n to os.linesep
    #if index > 0 and (index % 1000) ==0:
        #f.write('GO\n')  # SQL Server

#f.write('GO\n')  # SQL Server
f.close()
print 'Done.'