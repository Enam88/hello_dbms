--1. Créez une requête permettant de trouver les noms de pays commençant par la lettre B.
SELECT Country 
FROM world 
WHERE Country like 'B%' 

--2. Créez une requête permettant de trouver les noms de pays commençant par “Al”.
SELECT Country 
FROM world 
WHERE Country like 'Al%' 

--3. Créez une requête permettant de trouver les noms de pays finissant par la lettre y.
SELECT Country
FROM world
WHERE Country LIKE '%y';


--4. Créez une requête permettant de trouver les noms de pays finissant par “land”.
SELECT Country
FROM world
WHERE Country LIKE '%land';

--5. Créez une requête permettant de trouver les noms de pays contenant la lettre w.
SELECT Country 
FROM world 
WHERE Country LIKE '%w%'; 

--6. Créez une requête permettant de trouver les noms de pays contenant “oo” ou “ee”.
SELECT Country 
FROM world 
WHERE Country LIKE '%oo%' OR Country LIKE '%ee%'; 


--7. Créez une requête permettant de trouver les noms de pays contenant au moins trois fois la lettre a.
SELECT Country
FROM world
WHERE LEN(Country) - LEN(REPLACE(Country, 'a', '')) >= 3;


--8. Créez une requête permettant de trouver les noms de pays ayant la lettre 'r' comme seconde lettre.
SELECT Country 
FROM world 
WHERE Country LIKE '_r%'; 