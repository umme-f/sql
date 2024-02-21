-- Create a combined table
CREATE TABLE CombinedServerData (
    ServerType NVARCHAR(255),
    DateColumn DATETIME,
    CPURate FLOAT
);

-- Insert data from Application Server
INSERT INTO CombinedServerData (ServerType, DateColumn, CPURate)
SELECT 'Application Server', DateColumn, CPURate
FROM ApplicationServerData
WHERE MONTH(DateColumn) = 4;

-- Insert data from Database Server
INSERT INTO CombinedServerData (ServerType, DateColumn, CPURate)
SELECT 'Database Server', DateColumn, CPURate
FROM DatabaseServerData
WHERE MONTH(DateColumn) = 4;

-- Insert data from File Server
INSERT INTO CombinedServerData (ServerType, DateColumn, CPURate)
SELECT 'File Server', DateColumn, CPURate
FROM FileServerData
WHERE MONTH(DateColumn) = 4;

-- Query the combined table for April's average and maximum CPU rates
SELECT
    ServerType,
    DateColumn,
    AVG(CPURate) AS AvgCPURate,
    MAX(CPURate) AS MaxCPURate
FROM
    CombinedServerData
GROUP BY
    ServerType, DateColumn
ORDER BY
    ServerType, DateColumn;
