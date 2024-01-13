SELECT matchid, player FROM goal WHERE teamid = 'GER';

SELECT id, stadium, team1, team2 FROM game WHERE id = 1012;

SELECT player, teamid, stadium, mdate FROM game JOIN goal ON id = matchid WHERE teamid = 'GER';

SELECT team1, team2, player FROM game JOIN goal ON id = matchid WHERE player LIKE '%Mario%';

SELECT teamname, player, gtime FROM eteam JOIN goal ON id = teamid;

SELECT player, teamid, coach, gtime FROM goal JOIN eteam ON teamid = id WHERE gtime <= 10;

SELECT mdate, teamname FROM game JOIN eteam ON team1 = id WHERE coach = 'Fernando Santos';

SELECT player FROM game JOIN goal ON id = matchid WHERE stadium = 'National Stadium, Warsaw';

SELECT teamid, COUNT(*) FROM goal GROUP BY teamid;

SELECT stadium, COUNT(*) FROM game JOIN goal ON id = matchid GROUP BY stadium;

SELECT matchid, mdate, COUNT(*) FROM game JOIN goal ON id = matchid WHERE teamid = 'FRA' GROUP BY matchid;