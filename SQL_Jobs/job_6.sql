SELECT SUM(population) FROM world;

SELECT continent, SUM(population) FROM world GROUP BY continent;

SELECT continent, SUM(gdp) FROM world GROUP BY continent;

SELECT SUM(gdp) FROM world WHERE continent = 'Africa';

SELECT COUNT(*) FROM world WHERE area >= 1000000;

SELECT SUM(population) FROM world WHERE name IN ('Estonia', 'Latvia', 'Lithuania');

SELECT continent, COUNT(*) FROM world GROUP BY continent;

SELECT continent FROM world GROUP BY continent HAVING SUM(population) >= 100000000;