
--les pays dont la population est supérieure à celle de "Russia".
SELECT *
FROM world
WHERE Population > (SELECT Population FROM world WHERE Country = 'Russia');


SELECT Country
FROM world
WHERE region IN ('WESTERN EUROPE', 'EASTERN EUROPE')
    AND gdp_per_capita > (SELECT gdp_per_capita FROM world WHERE country = 'Italy');


SELECT country
FROM world
WHERE population > (SELECT population FROM world WHERE country = 'United Kingdom')
    AND population < (SELECT population FROM world WHERE country = 'Germany');


SELECT country, CONCAT(ROUND(population / (SELECT population FROM world WHERE country = 'Germany') * 100, 2), '%') AS 'population'
FROM world
WHERE region IN ('WESTERN EUROPE', 'EASTERN EUROPE');

SELECT Region, Country, Area_sq_mi 
FROM world 
WHERE Area_sq_mi IN (SELECT MAX(Area_sq_mi) FROM world GROUP BY Region);


SELECT DISTINCT Region AS Continent
FROM world
WHERE NOT EXISTS (
    SELECT *
    FROM world AS c2
    WHERE c2.Region = world.Region
      AND c2.Population > 25000000
);


