import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Zai\Desktop\Database1.accdb;')
    print("Connected to a Database")

except pyodbc.Error as e:
    print("Error in Connection")