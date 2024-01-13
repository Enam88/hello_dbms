--1. Requête pour afficher les prix Nobel de 1986 :
SELECT *
FROM nobel
WHERE yr = 1986;


--2. Requête pour afficher les prix Nobel de littérature de 1967 :
SELECT *
FROM nobel
WHERE yr = 1967 AND subject = 'Literature';

--3. Requête pour afficher l'année et le sujet du prix Nobel d'Albert Einstein :
SELECT yr, subject
FROM nobel
WHERE winner = 'Albert Einstein';

--4. Requête pour afficher les détails (année, sujet, lauréat) des lauréats du prix de Littérature de 1980 à 1989 inclus :
SELECT *
FROM nobel
WHERE subject = 'Literature' AND yr BETWEEN 1980 AND 1989;

--5. Requête pour afficher les détails des lauréats du prix de Mathématiques. Combien y en a-t-il ?
SELECT *
FROM nobel
WHERE subject = 'Mathematics';
