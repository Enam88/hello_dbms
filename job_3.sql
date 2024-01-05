-- 1. Requête pour afficher toutes les colonnes de la table students :


SELECT *
FROM students;

-- 2. Requête pour afficher les élèves âgés de strictement plus de 20 ans :


SELECT *
FROM students
WHERE age > 20;

-- 3. Requête pour classer les élèves selon leur note dans un ordre croissant, puis dans un ordre décroissant :


-- Ordre croissant
SELECT *
FROM students
ORDER BY grade ASC;

-- Ordre décroissant
SELECT *
FROM students
ORDER BY grade DESC;


