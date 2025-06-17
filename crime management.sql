-- Create Schema
CREATE SCHEMA crime;
GO

-- Create tables 
CREATE TABLE Crime ( 
    CrimeID INT  IDENTITY(1,1) PRIMARY KEY NOT NULL, 
    IncidentType VARCHAR(255) NOT NULL, 
    IncidentDate DATE NOT NULL, 
    Location VARCHAR(255) NOT NULL, 
    Description TEXT NOT NULL, 
    Status VARCHAR(20) NOT NULL
); 
 
CREATE TABLE Victim ( 
    VictimID INT IDENTITY(1,1) PRIMARY KEY NOT NULL, 
    CrimeID INT NOT NULL, 
    Name VARCHAR(255) NOT NULL, 
    ContactInfo VARCHAR(255) NOT NULL, 
    Injuries VARCHAR(255) NOT NULL, 
    FOREIGN KEY (CrimeID) REFERENCES Crime(CrimeID) 
    );
 
CREATE TABLE Suspect ( 
    SuspectID INT IDENTITY(1,1) PRIMARY KEY NOT NULL, 
    CrimeID INT  NOT NULL, 
    Name VARCHAR(255)  NOT NULL, 
    Description TEXT  NOT NULL, 
    CriminalHistory TEXT   NULL, 
    FOREIGN KEY (CrimeID) REFERENCES Crime(CrimeID) 
); 

 -- Insert sample data 

INSERT INTO Crime (CrimeID, IncidentType, IncidentDate, Location, Description, Status) 
VALUES 
    (1, 'Robbery', '2023-09-15', '123 Main St, Cityville', 'Armed robbery at a convenience store', 'Open'), 
    (2, 'Homicide', '2023-09-20', '456 Elm St, Townsville', 'Investigation into a murder case', 'Under 
Investigation'), 
    (3, 'Theft', '2023-09-10', '789 Oak St, Villagetown', 'Shoplifting incident at a mall', 'Closed'); 
 
INSERT INTO Crime (CrimeID, IncidentType, IncidentDate, Location, Description, Status) 
VALUES 
    (1, 'Robbery', '2023-09-15', '123 Main St, Cityville', 'Armed robbery at a convenience store', 'Open'), 
    (2, 'Homicide', '2023-09-20', '456 Elm St, Townsville', 'Investigation into a murder case', 'Under Investigation'), 
    (3, 'Theft', '2023-09-10', '789 Oak St, Villagetown', 'Shoplifting incident at a mall', 'Closed');


 SELECT*FROM Crime;

INSERT INTO Victim (VictimID, CrimeID, Name, ContactInfo, Injuries) 
VALUES 
    (1, 1, 'John Doe', 'johndoe@example.com', 'Minor injuries'), 
    (2, 2, 'Jane Smith', 'janesmith@example.com', 'Deceased'), 
(3, 3, 'Alice Johnson', 'alicejohnson@example.com', 'None'); 


    INSERT INTO Victim (CrimeID, Name, ContactInfo, Injuries) 
VALUES 
    (1, 'John Doe', 'johndoe@example.com', 'Minor injuries'), 
    (2, 'Jane Smith', 'janesmith@example.com', 'Deceased'), 
    (3, 'Alice Johnson', 'alicejohnson@example.com', 'None');

SELECT*FROM Victim;


INSERT INTO Suspect (CrimeID, Name, Description, CriminalHistory) 
VALUES 
    (1, 'Robber 1', 'Armed and masked robber', 'Previous robbery convictions'), 
    (2, 'Unknown', 'Investigation ongoing', NULL), 
    (3, 'Suspect 1', 'Shoplifting suspect', 'Prior shoplifting arrests');


SELECT*FROM Suspect;

--1. Select all open incidents. 

SELECT *
FROM Crime
WHERE Status = 'Open';

--2. Find the total number of incidents

SELECT COUNT(*) AS TotalIncidents
FROM Crime;

--3. List all unique incident types

SELECT DISTINCT IncidentType
FROM Crime;

--4. Retrieve incidents between '2023-09-01' and '2023-09-10'

SELECT *
FROM Crime
WHERE IncidentDate BETWEEN '2023-09-01' AND '2023-09-10';

--Age is added to Victim and Suspect tables.
ALTER TABLE Victim ADD Age INT;
ALTER TABLE Suspect ADD Age INT;

--5. List persons involved in incidents in descending order of age

--Age is added to Victim and Suspect tables.

ALTER TABLE Victim ADD Age INT;

ALTER TABLE Suspect ADD Age INT;

SELECT Name, Age, 'Victim' AS Role FROM Victim
UNION ALL
SELECT Name, Age, 'Suspect' FROM Suspect
ORDER BY Age DESC;
--6. Find the average age of persons involved in incidents

SELECT AVG(Age) AS AverageAge
FROM (
    SELECT Age FROM Victim
    UNION ALL
    SELECT Age FROM Suspect
) AS AllPersons;

--7. List incident types and their counts (only for open cases)

SELECT IncidentType, COUNT(*) AS Total
FROM Crime
WHERE Status = 'Open'
GROUP BY IncidentType;

--8. Find persons with names containing 'Doe'

SELECT Name, 'Victim' AS Role FROM Victim WHERE Name LIKE '%Doe%'
UNION
SELECT Name, 'Suspect' FROM Suspect WHERE Name LIKE '%Doe%';

--9. Retrieve names of persons involved in open and closed cases

SELECT DISTINCT v.Name AS PersonName, c.Status
FROM Victim v
JOIN Crime c ON v.CrimeID = c.CrimeID
WHERE c.Status IN ('Open', 'Closed')
UNION
SELECT DISTINCT s.Name, c.Status
FROM Suspect s
JOIN Crime c ON s.CrimeID = c.CrimeID
WHERE c.Status IN ('Open', 'Closed');

--10. Incident types where persons aged 30 or 35 are involved

ALTER TABLE Victim ADD Age INT;

ALTER TABLE Suspect ADD Age INT;

UPDATE Victim SET Age = 30 WHERE Name = 'John Doe';

UPDATE Suspect SET Age = 35 WHERE Name = 'Suspect 1';

SELECT DISTINCT c.IncidentType
FROM Crime c
JOIN Victim v ON c.CrimeID = v.CrimeID
WHERE v.Age IN (30, 35);


--11. Persons involved in incidents of the same type as 'Robbery'

SELECT DISTINCT v.Name AS PersonName, 'Victim' AS Role
FROM Victim v
JOIN Crime c ON v.CrimeID = c.CrimeID
WHERE c.IncidentType = 'Robbery'
UNION
SELECT DISTINCT s.Name, 'Suspect'
FROM Suspect s
JOIN Crime c ON s.CrimeID = c.CrimeID
WHERE c.IncidentType = 'Robbery';


--12. Incident types with more than one open case



SELECT IncidentType 
FROM Crime
WHERE Status = 'Open'
GROUP BY IncidentType
HAVING COUNT(*) > 1;



--13. Incidents with suspects whose names also appear as victims

UPDATE Suspect SET Name = 'John Doe' WHERE SuspectID = 1;

INSERT INTO Suspect (CrimeID, Name, Description, CriminalHistory)
VALUES (3, 'Alice Johnson', 'Same name as victim', 'Test Case');

SELECT DISTINCT c.CrimeID, c.IncidentType, c.IncidentDate, c.Location, c.Status
FROM Crime c
JOIN Suspect s ON c.CrimeID = s.CrimeID
WHERE s.Name IN (
    SELECT Name FROM Victim
);

--14. All incidents with victim and suspect details

SELECT 
    c.CrimeID, c.IncidentType, c.Location, c.Status,
    v.Name AS VictimName, v.Injuries,
    s.Name AS SuspectName, s.Description AS SuspectDesc
FROM Crime c
LEFT JOIN Victim v ON c.CrimeID = v.CrimeID
LEFT JOIN Suspect s ON c.CrimeID = s.CrimeID;

--15. Incidents where the suspect is older than any victim

UPDATE Victim SET Age = 30 WHERE VictimID = 1;
UPDATE Victim SET Age = 25 WHERE VictimID = 2;
UPDATE Victim SET Age = 28 WHERE VictimID = 3;

UPDATE Suspect SET Age = 35 WHERE SuspectID = 1;
UPDATE Suspect SET Age = 40 WHERE SuspectID = 2;
UPDATE Suspect SET Age = 29 WHERE SuspectID = 3;

SELECT DISTINCT 
    c.CrimeID,
    c.IncidentType,
    c.IncidentDate,
    c.Location,
    CAST(c.Description AS VARCHAR(MAX)) AS Description,
    c.Status
FROM Crime c
JOIN Suspect s ON c.CrimeID = s.CrimeID
WHERE s.Age > ALL (
    SELECT v.Age FROM Victim v WHERE v.CrimeID = c.CrimeID
);

--16. Suspects involved in multiple incidents

SELECT * FROM Suspect;


INSERT INTO Suspect (CrimeID, Name, Description, CriminalHistory, Age)
VALUES (2, 'Robber 1', 'Repeat offense', 'Arrested previously', 36);

SELECT Name, COUNT(*) AS IncidentCount
FROM Suspect
GROUP BY Name
HAVING COUNT(*) > 1;


--17. Incidents with no suspects involved

SELECT CrimeID FROM Crime;

INSERT INTO Crime (CrimeID, IncidentType, IncidentDate, Location, Description, Status)
VALUES (5, 'Cyber Crime', '2023-09-25', '99 Tech Park, Digital City', 'Phishing scam reported', 'Open');

SELECT c.*
FROM Crime c
LEFT JOIN Suspect s ON c.CrimeID = s.CrimeID
WHERE s.SuspectID IS NULL;


--18. Cases where at least one incident is 'Homicide' and others are all 'Robbery'

SELECT CrimeID, IncidentType
FROM Crime
WHERE EXISTS (
    SELECT 1 FROM Crime WHERE IncidentType = 'Homicide'
)
AND IncidentType IN ('Homicide', 'Robbery')
GROUP BY CrimeID, IncidentType
HAVING COUNT(*) >= 1;

--19.  list of all incidents and the associated suspects, showing suspects for each incident, or 'No Suspect' if there are none.



SELECT 
    c.CrimeID, c.IncidentType, ISNULL(s.Name, 'No Suspect') AS SuspectName
FROM Crime c
LEFT JOIN Suspect s ON c.CrimeID = s.CrimeID;

--20.  List all suspects who have been involved in incidents with incident types 'Robbery' or 'Assault'


-- Add a new crime of type Assault
INSERT INTO Crime (CrimeID, IncidentType, IncidentDate, Location, Description, Status)
VALUES (6, 'Assault', '2023-09-28', '10 Hill Rd, Cityville', 'Street fight incident', 'Open');

-- Add a suspect linked to that Assault
INSERT INTO Suspect (CrimeID, Name, Description, CriminalHistory, Age)
VALUES (6, 'Assaulter 1', 'Aggressive behavior', 'Previous assault case', 33);


SELECT DISTINCT s.SuspectID, s.CrimeID, s.Name, s.Age
FROM Suspect s
JOIN Crime c ON s.CrimeID = c.CrimeID
WHERE c.IncidentType IN ('Robbery', 'Assault');


















