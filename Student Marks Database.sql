use db;
CREATE TABLE studentmarks(name varchar(10),language int,English int,Maths int,Science int,Social int)
describe studentmarks;
SELECT * from studentmarks
SELECT name,(language + English + Maths + Science + Social) AS total_marks FROM studentmarks;
SELECT name,(language + English + Maths + Science + Social) / 5 AS average_marks FROM studentmarks;
SELECT name, MAX(language) AS max_marks FROM studentmarks GROUP BY name;
SELECT name, MIN(Maths) AS min_marks FROM studentmarks GROUP BY name;
delete from studentmarks where name='Manoj';