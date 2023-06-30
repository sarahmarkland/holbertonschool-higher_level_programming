-- lists all the cities of California that can be found in the database hbtn_0e_4_usa
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
WHERE states.name = 'California';