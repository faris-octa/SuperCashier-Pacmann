import sqlite3

# create a connection to database
conn = sqlite3.connect('nama_database.db')

# create a cursor object
cursor = conn.cursor()

# execute SQL command to create a table
cursor.execute('''CREATE TABLE nama_tabel
                  (kolom_1 tipe_data_1, kolom_2 tipe_data_2, kolom_3 tipe_data_3)''')

# commit the changes to database
conn.commit()

# close the connection to database
conn.close()