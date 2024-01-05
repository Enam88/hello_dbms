SELECT (Population) FROM world  
WHERE Country = 'Germany' 

SELECT  Country, Population  
FROM world 
WHERE Country IN ('Germany' ,'Norway', 'Denmark') 

SELECT Country, Area_sq_mi 
FROM world 
WHERE Area_sq_mi BETWEEN 200000 AND 300000 