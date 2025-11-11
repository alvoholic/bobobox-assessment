===========================================
DATABASE DESIGN: Bobobox Asset Management
===========================================

-- Locations
-- Menyimpan daftar lokasi Bobobox (Hotel/Cabin)
CREATE TABLE Locations (
    Location_ID VARCHAR(10) PRIMARY KEY,
    Location_Name VARCHAR(100) NOT NULL,
    City VARCHAR(50),
    Type VARCHAR(20) CHECK (Type IN ('Hotel', 'Cabin'))
);

-- Units
-- Setiap unit berada di satu lokasi tertentu
CREATE TABLE Units (
    Unit_ID VARCHAR(10) PRIMARY KEY,
    Location_ID VARCHAR(10) NOT NULL,
    Unit_Name VARCHAR(50) NOT NULL,
    Floor_Number INT,
    Status VARCHAR(20) DEFAULT 'Active',
    FOREIGN KEY (Location_ID) REFERENCES Locations(Location_ID)
);

-- Sensors
-- Menyimpan data setiap sensor IoT
CREATE TABLE Sensors (
    Sensor_ID VARCHAR(10) PRIMARY KEY,
    Sensor_Type VARCHAR(30) CHECK (Sensor_Type IN ('Temperature', 'Humidity', 'Occupancy')),
    Model VARCHAR(50),
    Install_Date DATE,
    Current_Status VARCHAR(20) CHECK (Current_Status IN ('Active', 'Inactive', 'Faulty'))
);

-- Sensor_Placement
-- Menunjukkan di unit mana sensor dipasang
CREATE TABLE Sensor_Placement (
    Placement_ID SERIAL PRIMARY KEY,
    Sensor_ID VARCHAR(10) NOT NULL,
    Unit_ID VARCHAR(10) NOT NULL,
    Placement_Date DATE NOT NULL,
    Removed_Date DATE,
    FOREIGN KEY (Sensor_ID) REFERENCES Sensors(Sensor_ID),
    FOREIGN KEY (Unit_ID) REFERENCES Units(Unit_ID)
);

-- Engineers
-- Data engineer yang melakukan maintenance sensor
CREATE TABLE Engineers (
    Engineer_ID VARCHAR(10) PRIMARY KEY,
    Engineer_Name VARCHAR(100) NOT NULL,
    Contact_Info VARCHAR(100),
    Specialty VARCHAR(50)
);

-- Maintenance_Records
-- Catatan riwayat perawatan untuk setiap sensor
CREATE TABLE Maintenance_Records (
    Maintenance_ID SERIAL PRIMARY KEY,
    Sensor_ID VARCHAR(10) NOT NULL,
    Engineer_ID VARCHAR(10) NOT NULL,
    Maintenance_Date DATE NOT NULL,
    Description TEXT,
    Result VARCHAR(50) CHECK (Result IN ('Fixed', 'Replaced', 'Checked', 'Failed')),
    FOREIGN KEY (Sensor_ID) REFERENCES Sensors(Sensor_ID),
    FOREIGN KEY (Engineer_ID) REFERENCES Engineers(Engineer_ID)
);

