# importing required module(mysql.Connector)
import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
)

cursor = conn.cursor()

# Create the Books database if it doesn't exist
# cursor.execute("CREATE DATABASE IF NOT EXISTS Books")
cursor.execute("USE Books")

# Create Authors table
cursor.execute("CREATE TABLE Authors (AuthorID INT PRIMARY KEY, First_Name VARCHAR(50), Last_Name VARCHAR(50))")

# Create Publishers table
cursor.execute("CREATE TABLE Publishers (PublisherID INT PRIMARY KEY, Publisher_Name VARCHAR(50))")

# Create Titles table with a foreign key constraint on PublisherID
cursor.execute("CREATE TABLE Titles (ISBN VARCHAR(20) PRIMARY KEY, Title VARCHAR(50), PublisherID INT, Image_file LONGBLOB, Price INT, FOREIGN KEY (PublisherID) REFERENCES Publishers(PublisherID))")

# Create AuthorISBN table with foreign key constraints on AuthorID and ISBN
cursor.execute("CREATE TABLE AuthorISBN (AuthorID INT, ISBN VARCHAR(20), FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID), FOREIGN KEY (ISBN) REFERENCES Titles(ISBN))")

# Insert data into Publishers table first
cursor.execute("INSERT INTO Publishers (PublisherID, Publisher_Name) VALUES (1902, 'Tech Publications')")
cursor.execute("INSERT INTO Publishers (PublisherID, Publisher_Name) VALUES (0102, 'Multi-Tech Publisher')")

# Insert data into Titles table
cursor.execute("INSERT INTO Titles (ISBN, Title, PublisherID, Image_file, Price) VALUES ('1234567890123', 'My Health', 1902, NULL, 150)")
cursor.execute("INSERT INTO Titles (ISBN, Title, PublisherID, Image_file, Price) VALUES ('9876543210987', 'Healthy Life Style', 102, NULL, 200)")

# Insert data into Authors table
cursor.execute("INSERT INTO Authors (AuthorID, First_Name, Last_Name) VALUES (1, 'Rangdal', 'Pavansai')")
cursor.execute("INSERT INTO Authors (AuthorID, First_Name, Last_Name) VALUES (2, 'Pavan', 'Sai')")

# Insert data into AuthorISBN table
cursor.execute("INSERT INTO AuthorISBN (AuthorID, ISBN) VALUES (1, '1234567890123')")
cursor.execute("INSERT INTO AuthorISBN (AuthorID, ISBN) VALUES (2, '9876543210987')")

# Update data in Authors table
cursor.execute("UPDATE Authors SET First_Name = 'R' WHERE AuthorID = 1")

# Delete data from AuthorISBN table first
cursor.execute("DELETE FROM AuthorISBN WHERE ISBN = '9876543210987'")

# Delete data from Titles table
cursor.execute("DELETE FROM Titles WHERE ISBN = '9876543210987'")

# Commit the changes
conn.commit()

cursor.close()
conn.close()


"""The "Titles" table includes two foreign keys, one for the "Authors" table and one for the "Publishers" table, which establishes the relationships between these tables. The "AuthorID" column in the "Titles" table references the "AuthorID" column in the "Authors" table, and the "PublisherID" column in the "Titles" table references the "PublisherID" column in the "Publishers" table.

This sequence ensures that the necessary tables and relationships are created in the correct order."""