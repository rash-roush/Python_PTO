import tkinter as tk
import customtkinter as ctk
from login import LoginFrame
import sqlite3

conn = sqlite3.connect('pto.db')
cursor = conn.cursor()


# Create the employee table with EmpID as primary key
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user(
    UserID INT PRIMARY KEY,
    FName VARCHAR(20) NOT NULL,
    LName VARCHAR(20) NOT NULL,
    DOB TEXT,
    Address VARCHAR(255),
    Email VARCHAR(30),
    Phone INT)''')

# Check if there's any data in the table
cursor.execute('SELECT COUNT(*) FROM user')
if cursor.fetchone()[0] == 0:  # If the table is empty, then insert data
    user_data = [
        (1, 'John', 'Doe', '1980-05-15', '123 Main St, Cityville, State, Zip', 'john.doe@email.com', 1234567890),
        (2, 'Jane', 'Smith', '1985-10-20', '456 Elm St, Townsville, State, Zip', 'jane.smith@email.com', 9876543210),
        (3, 'Michael', 'Johnson', '1976-03-08', '789 Oak St, Villageton, State, Zip', 'michael.johnson@email.com', 5551234567),
        (4, 'Emily', 'Brown', '1990-12-25', '101 Pine St, Hamletville, State, Zip', 'emily.brown@email.com', 4447890123),
        (5, 'David', 'Lee', '1988-07-14', '222 Maple St, Burgville, State, Zip', 'david.lee@email.com', 3335678901)
    ]
    cursor.executemany('''
        INSERT INTO user (UserID, FName, LName, DOB, Address, Email, Phone)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', user_data)
    conn.commit()


#  PTORequest SQL
cursor.execute('''
    CREATE TABLE IF NOT EXISTS PTORequest(
    PTOID INT PRIMARY KEY,
    EmpID INT NOT NULL,
    PTODate TEXT, /*for created date in our form*/
    PTOType INT,
    PTOReason VARCHAR(200),
    PTOStartDate TEXT,
    PTOEndDate TEXT,
    FOREIGN KEY (EmpID) REFERENCES employee(EmpID))''')

# Check if there's any data in the table
cursor.execute('SELECT COUNT(*) FROM PTORequest')
if cursor.fetchone()[0] == 0:  # If the table is empty, then insert data
    ptorequest_data = [
        (1, 10000, '2024-04-14', 1, 'Family vacation', '2024-04-20', '2024-04-25'),
        (2, 11111, '2024-04-14', 2, 'Flu', '2024-04-10', '2024-04-12'),
        (3, 12345, '2024-04-14', 1, 'Attending a family event', '2024-04-18', '2024-04-19'),
        (4, 22222, '2024-04-14', 1, 'Traveling abroad', '2024-05-01', '2024-05-10'),
        (5, 54321, '2024-04-14', 2, 'Food poisoning', '2024-04-14', '2024-04-16')
    ]
    cursor.executemany('''
        INSERT INTO PTORequest (PTOID, EmpID, PTODate, PTOType, PTOReason, PTOStartDate, PTOEndDate)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', ptorequest_data)
    conn.commit()

    # create data for PTO Documentation
cursor.execute('''
    CREATE TABLE IF NOT EXISTS PTODocument(
    PTODOCID INT PRIMARY KEY,
    PTOID INT NOT NULL,
    PDFData BLOB NOT NULL,
    FOREIGN KEY (PTOID) REFERENCES PTORequest(PTOID))''')



app = ctk.CTk()
app.title('PTO')
app.geometry("800x500")
app.configure(bg="#121212")

if __name__ == "__main__":
    login_frame = LoginFrame(app)
    app.mainloop()
