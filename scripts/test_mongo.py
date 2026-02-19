from pymongo import MongoClient 

uri = "mongodb+srv://indinaazizah_db_user:bigdata.project@bigdata.iwksw4h.mongodb.net/?appName=bigdata" 

try: 
    # Kode di bawah ini harus menjorok ke dalam (1x Tab)
    client = MongoClient(uri) 
    print("Koneksi berhasil!") 
    print(client.list_database_names()) 
except Exception as e: 
    # Kode di bawah ini juga harus menjorok ke dalam
    print("Koneksi gagal:", e)