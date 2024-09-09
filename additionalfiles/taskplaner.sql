drop database if exists taskplaner;
create database taskplaner;
use taskplaner;

-- ********************************************************************************************************
-- Andre Probst
-- 1.7.2024
-- Version 1.0
-- ********************************************************************************************************

-- ********************************************************************************************************
-- ********************************************************************************************************
-- TABELLEN ERSTELLEN
-- ********************************************************************************************************
-- ********************************************************************************************************

-- ********************************************************************************************************
-- Material --> Hier können Materialien eingetragen werden, die wiederkehrend bei Aufgaben benötigt werden
-- Attribut IstAktiv ist ein Boolean über welchen gesteuert werden kann, welche Materialien bei der Erfassung
-- einer neuen Aufgabe zur Auswahl stehen
-- ********************************************************************************************************
CREATE TABLE Material(
	MaterialID int primary key not null auto_increment,
    Material varchar(100) not null,
    IstAktiv boolean not null default true
);

-- ********************************************************************************************************
-- Kategorie --> Domänentabelle für die Kategorie einer Aufgabe
-- Attribut IstAktiv ist ein Boolean über welchen gesteuert werden kann, welche Kategorien bei der Erfassung
-- einer neuen Aufgabe zur Auswahl stehen
-- ********************************************************************************************************
CREATE TABLE Kategorie(
	KategorieID int primary key not null auto_increment,
    Kategorie varchar(100) not null,
    IstAktiv boolean not null default true
);

-- ********************************************************************************************************
-- Priorität --> Domänentabelle für die Priorität einer Aufgabe
-- ********************************************************************************************************
CREATE TABLE Prioritaet(
	PrioritaetID int primary key not null auto_increment,
    Prioritaet varchar(100) not null
);

-- ********************************************************************************************************
-- Fortschritt --> Domänentabelle für den Fortschritt einer Aufgabe
-- Als Werte werden Prozentangaben von 0 bis 100 in Zehnerschritten vorgegeben
-- ********************************************************************************************************
CREATE TABLE Fortschritt(
	FortschrittID int primary key not null auto_increment,
    Fortschritt varchar(100) not null
);

-- ********************************************************************************************************
-- Aufgabe --> Haupttabelle mit den Aufgaben
-- SerieMasterID --> Rekursion, zeigt auf den Haupteintrag, wenn eine Aufgabe "wiederkehrend" erstellt werden soll
-- Beginn --> Datum und Uhrzeit --> Muss erfasst werden
-- Ende --> Datum und Uhrzeit --> Kann leer bleiben wenn unbekannt
-- Ort --> Wenn erwünscht Ort der Erledigung, als Text
-- Koordinaten --> GPS Koordinaten wenn erwünscht --> Könnte ja mittels Google Maps eingebunden werden
-- Notiz --> Memo-Feld für Infos zur Aufgabe
-- ********************************************************************************************************
CREATE TABLE Aufgabe(
	AufgabeID int primary key not null auto_increment,
    SerieMasterID int null,
    Titel varchar(100) not null,
    Beginn datetime not null,
    Ende datetime null,
    Ort varchar(250) null,
    Koordinaten varchar(100) null,
    Notiz TEXT null,
    KategorieID int not null,
    PrioritaetID int not null,
    FortschrittID int not null,
    foreign key (SerieMasterID) references Aufgabe(AufgabeID),
    foreign key (KategorieID) references Kategorie(KategorieID),
    foreign key (PrioritaetID) references Prioritaet(PrioritaetID),
    foreign key (FortschrittID) references Fortschritt(FortschrittID)
);

-- ********************************************************************************************************
-- Datei --> Hier können Datein verlinkt oder binär als BLOB zu einer Aufgabe verknüpft werden
-- ********************************************************************************************************
CREATE TABLE Datei(
	DateiID int primary key not null auto_increment,
    Dateipfad varchar(250),
    AufgabeID int not null,
    foreign key (AufgabeID) references Aufgabe(AufgabeID)
);

-- ********************************************************************************************************
-- AufgabeMaterial --> Mapping von Materialien zu einer Aufgabe
-- ********************************************************************************************************
CREATE TABLE AufgabeMaterial(
	AufgabeID int not null,
    MaterialID int not null,
    Anzahl int null,
    primary key (AufgabeID, MaterialID),
    foreign key (AufgabeID) references Aufgabe(AufgabeID),
    foreign key (MaterialID) references Material(MaterialID)
);


-- ********************************************************************************************************
-- ********************************************************************************************************
-- EINIGE DATEN VORGEBEN
-- ********************************************************************************************************
-- ********************************************************************************************************
INSERT INTO Material (Material) VALUES (('Notebook'));
INSERT INTO Material (Material) VALUES (('Pepier'));
INSERT INTO Material (Material) VALUES (('Schreibzeug'));
INSERT INTO Material (Material) VALUES (('Fachbuch'));

INSERT INTO Kategorie (Kategorie) VALUES (('Hausaufgaben'));
INSERT INTO Kategorie (Kategorie) VALUES (('Prüfungsvorbereitung'));
INSERT INTO Kategorie (Kategorie) VALUES (('Exkurion'));
INSERT INTO Kategorie (Kategorie) VALUES (('Freiwilliges Lernen'));
INSERT INTO Kategorie (Kategorie) VALUES (('Einkaufen'));
INSERT INTO Kategorie (Kategorie) VALUES (('Freizeit'));

INSERT INTO Prioritaet (Prioritaet) VALUES (('Hoch'));
INSERT INTO Prioritaet (Prioritaet) VALUES (('Normal'));
INSERT INTO Prioritaet (Prioritaet) VALUES (('Niedrig'));

INSERT INTO Fortschritt (Fortschritt) VALUES (('0%'));
INSERT INTO Fortschritt (Fortschritt) VALUES (('10%'));
INSERT INTO Fortschritt (Fortschritt) VALUES (('20%'));
INSERT INTO Fortschritt (Fortschritt) VALUES (('30%'));
INSERT INTO Fortschritt (Fortschritt) VALUES (('40%'));
INSERT INTO Fortschritt (Fortschritt) VALUES (('50%'));
INSERT INTO Fortschritt (Fortschritt) VALUES (('60%'));
INSERT INTO Fortschritt (Fortschritt) VALUES (('70%'));
INSERT INTO Fortschritt (Fortschritt) VALUES (('80%'));
INSERT INTO Fortschritt (Fortschritt) VALUES (('90%'));
INSERT INTO Fortschritt (Fortschritt) VALUES (('100%'));

-- ********************************************************************************************************
-- ********************************************************************************************************
-- ENDE
-- ********************************************************************************************************
-- ********************************************************************************************************

