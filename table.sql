-- Create tables
CREATE TABLE ApplicationServerData (
    DateColumn DATETIME,
    CPURate FLOAT,
    ServerName NVARCHAR(255)
);

CREATE TABLE DatabaseServerData (
    DateColumn DATETIME,
    CPURate FLOAT,
    ServerName NVARCHAR(255)
);

CREATE TABLE FileServerData (
    DateColumn DATETIME,
    CPURate FLOAT,
    ServerName NVARCHAR(255)
);

-- Insert data (Replace 'YourFilePath' with the actual file path)
BULK INSERT ApplicationServerData
FROM 'YourFilePath\ApplicationServerData.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

BULK INSERT DatabaseServerData
FROM 'YourFilePath\DatabaseServerData.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

BULK INSERT FileServerData
FROM 'YourFilePath\FileServerData.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

-- Query average and maximum CPU rates for April
SELECT
    'Application Server' AS ServerType,
    AVG(CPURate) AS AvgCPURate,
    MAX(CPURate) AS MaxCPURate
FROM
    ApplicationServerData
WHERE
    MONTH(DateColumn) = 4;

UNION ALL

SELECT
    'Database Server' AS ServerType,
    AVG(CPURate) AS AvgCPURate,
    MAX(CPURate) AS MaxCPURate
FROM
    DatabaseServerData
WHERE
    MONTH(DateColumn) = 4;

UNION ALL

SELECT
    'File Server' AS ServerType,
    AVG(CPURate) AS AvgCPURate,
    MAX(CPURate) AS MaxCPURate
FROM
    FileServerData
WHERE
    MONTH(DateColumn) = 4;
