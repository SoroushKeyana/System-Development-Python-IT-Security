USE Elevator;

CREATE TABLE City(
	CityId INT PRIMARY KEY,
    CityName CHAR
);

CREATE TABLE Building(
	BuildingId INT PRIMARY KEY,
    CityId INT,
    Floors int,
    FOREIGN KEY (CityId) REFERENCES City(CityId)
);

CREATE TABLE EmployeeStatus(
	EmployeeStatusId INT PRIMARY KEY,
    StatusDescription CHAR
);

CREATE TABLE ServiceStatus(
	ServiceStatusId INT PRIMARY KEY,
    StatusDescription CHAR
);

CREATE TABLE Technican(
	EmployeeId INT PRIMARY KEY,
    FirstName CHAR,
    LastName CHAR,
    EmailAddress CHAR,
    AnnualSalary INT,
    SpecialSkill CHAR,
    EmployeeStatusId INT,
    FOREIGN KEY (EmployeeStatusId) REFERENCES EmployeeStatus(EmployeeStatusId)
);

CREATE TABLE ElevatorType(
	ElevatorTypeId INT PRIMARY KEY,
    TypeName CHAR
);

CREATE TABLE ElevatorModel(
	ElevatorModelId INT PRIMARY KEY,
    ModelName INT,
    Speed INT,
    MaxWeight INT,
    PeopleLimit INT,
    ElevatorTypeId INT,
    FOREIGN KEY (ElevatorTypeId) REFERENCES ElevatorType(ElevatorTypeId)
);

CREATE TABLE Elevator(
	ElevatorId INT PRIMARY KEY,
    ElevatorModelId INT,
    BuildingId INT,
    InstallationDate DATE,
    FOREIGN KEY (ElevatorModelId) REFERENCES ElevatorModel(ElevatorModelId),
    FOREIGN KEY (BuildingId) REFERENCES Building(BuildingId)
);

CREATE TABLE ServiceActivity(
	ServiceActivityId INT PRIMARY KEY,
    EmployeeId INT,
    ElevatorId INT,
    ServiceDateTime DATE,
    ServiceDescription CHAR,
    ServiceStatusId INT,
    FOREIGN KEY (EmployeeId) REFERENCES Technican(EmployeeId),
    FOREIGN KEY (ElevatorId) REFERENCES Elevator(ElevatorId)
);
