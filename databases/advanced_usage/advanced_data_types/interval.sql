SELECT ts_1 - INTERVAL '4 years 1 day 4 hours'
FROM demo_stamp;

SELECT now() - INTERVAL '3 months 10 days 5 hours';

SELECT now() - INTERVAL 'P5Y4M10DT5H12M14S';

SELECT now() - INTERVAL 'P0005-04-10T05:12:14';