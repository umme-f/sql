i have 3 csv files. one is application server cpu data, one is database server cpu data and the last one is file server cpu data. each csv file contains 3 columns-date-time column,cpu using rate and server name. how do i show each day of  aprils avg and max cpu using rate in a table using sql management server. also show the dates from date time column in the first column in the combied table
ChatGPT
Certainly! If you want to display each day of April's average and maximum CPU usage for each server type in a combined table, you can modify the script as follows:

sql
Copy code
-- Create a combined table
CREATE TABLE CombinedServerData (
    ServerType NVARCHAR(255),
    DateColumn DATETIME,
    AvgCPURate FLOAT,
    MaxCPURate FLOAT
);

-- Insert data from Application Server
INSERT INTO CombinedServerData (ServerType, DateColumn, AvgCPURate, MaxCPURate)
SELECT 
    'Application Server' AS ServerType, 
    DateColumn, 
    AVG(CPURate) AS AvgCPURate, 
    MAX(CPURate) AS MaxCPURate
FROM 
    ApplicationServerData
WHERE 
    MONTH(DateColumn) = 4
GROUP BY 
    DateColumn;

-- Insert data from Database Server
INSERT INTO CombinedServerData (ServerType, DateColumn, AvgCPURate, MaxCPURate)
SELECT 
    'Database Server' AS ServerType, 
    DateColumn, 
    AVG(CPURate) AS AvgCPURate, 
    MAX(CPURate) AS MaxCPURate
FROM 
    DatabaseServerData
WHERE 
    MONTH(DateColumn) = 4
GROUP BY 
    DateColumn;

-- Insert data from File Server
INSERT INTO CombinedServerData (ServerType, DateColumn, AvgCPURate, MaxCPURate)
SELECT 
    'File Server' AS ServerType, 
    DateColumn, 
    AVG(CPURate) AS AvgCPURate, 
    MAX(CPURate) AS MaxCPURate
FROM 
    FileServerData
WHERE 
    MONTH(DateColumn) = 4
GROUP BY 
    DateColumn;

-- Query the combined table
SELECT 
    ServerType,
    DateColumn,
    AvgCPURate,
    MaxCPURate
FROM 
    CombinedServerData
ORDER BY 
    ServerType, DateColumn;
This script creates a new table named CombinedServerData and inserts the relevant data from each server table for each day in April. The final query retrieves the average and maximum CPU rates for each server type on each day in April.

Make sure to adjust the column and table names as needed based on your actual database structure and CSV file contents.


--------------------------------------------------------------------------
SELECT DATE(timestamp_column) AS date_only
FROM your_table
WHERE timestamp_column >= '2024-02-01' AND timestamp_column < '2024-03-01';


...............Replace timestamp_column with the actual name of your timestamp column, and your_table with the name of your table.

In this example, the DATE(timestamp_column) function extracts the date part from the timestamp. The WHERE clause filters the data for the month of February 2024. Adjust the date range in the WHERE clause based on your requirements.









