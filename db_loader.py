import pandas as pd
import sqlite3

def insert_to_table(source_data, data):
    """
    Fungsi untuk mengimport daftar suatu transaksi ke database sqlite

    args:
        - source_data (str): nama database sqlite
        - data (dataframe): dataframe transaksi

    return: 
        None
    """
    # create a connection to database
    try:
        conn = sqlite3.connect(source_data)
    except sqlite3.Error as error:
        print('Gagal terkoneksi dengan database:', error)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions 
                    (no_id INT, 
                    nama_item TEXT, 
                    jumlah_item INT, 
                    harga INT, 
                    total_harga INT, 
                    Diskon INT, 
                    harga_Diskon INT
                    )''')
    
    # GET no_id -> no_id terakhir di database + 1
    cursor.execute('SELECT MAX(no_id) FROM transactions')
    no_id = cursor.fetchone()[0] + 1

    # ASSIGN kolom no_id
    data = pd.concat([pd.Series(no_id, index=data.index, name='no_id'), data], axis=1)
    # print(data) <-- for debugging
    data.to_sql('transactions', con=conn, if_exists='append', index=False)

    conn.commit()  
    conn.close()