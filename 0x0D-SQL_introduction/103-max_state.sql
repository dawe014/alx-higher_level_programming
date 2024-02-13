-- display max temprature of each state

SELECT state, MAX(value) AS max_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY state
ORDER BY state;