--les pays dont la population est supérieure à celle de la Russie.

SELECT Country
FROM world
WHERE Population > (SELECT Population FROM world WHERE Country = 'Russia');

--les pays d'Europe dont le PIB par habitant est supérieur à celui d’ "Italy".
SELECT Country
FROM world
WHERE region IN ('WESTERN EUROPE', 'EASTERN EUROPE')
    AND gdp_per_capita > (SELECT gdp_per_capita FROM world WHERE country = 'Italy');


-- les pays dont la population est supérieure à celle du Royaume-Uni mais inférieure à celle de l'Allemagne.
SELECT country
FROM world
WHERE population > (SELECT population FROM world WHERE country = 'United Kingdom')
    AND population < (SELECT population FROM world WHERE country = 'Germany');

--le nom et la population de chaque pays d'Europe, en pourcentage de la population de l'Allemagne.
SELECT country, CONCAT(ROUND(population / (SELECT population FROM world WHERE country = 'Germany') * 100, 2), '%') AS 'population'
FROM world
WHERE region IN ('WESTERN EUROPE', 'EASTERN EUROPE');

--le plus grand pays de chaque continent, en indiquant son continent, son nom et sa superficie.
SELECT Region, Country, Area_sq_mi 
FROM world 
WHERE Area_sq_mi IN (SELECT MAX(Area_sq_mi) FROM world GROUP BY Region);

--les continents qui ont une population inférieure ou égale à 25 000 000.

SELECT DISTINCT Region AS Continent
FROM world
WHERE NOT EXISTS (
    SELECT *
    FROM world AS c2
    WHERE c2.Region = world.Region
      AND c2.Population > 25000000
);

--les pays qui ont une population inférieure ou égale à 25 000 000.
SELECT *
FROM countries
WHERE Population <= 25000000;

