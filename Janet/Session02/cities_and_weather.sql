DROP TABLE IF EXISTS cities;
CREATE TABLE cities (name text, state text);

INSERT INTO cities (name, state) VALUES('New York City','NY');
INSERT INTO cities (name, state) VALUES('Boston','MA');
INSERT INTO cities (name, state) VALUES('Chicago','IL');
INSERT INTO cities (name, state) VALUES('Miami','FL');
INSERT INTO cities (name, state) VALUES('Dallas','TX');
INSERT INTO cities (name, state) VALUES('Seattle','WA');
INSERT INTO cities (name, state) VALUES('Portland','OR');
INSERT INTO cities (name, state) VALUES('San Francisco','CA');
INSERT INTO cities (name, state) VALUES('Los Angeles','CA');

DROP TABLE IF EXISTS weather;
CREATE TABLE weather ( city text, year integer, warm_month text, cold_month text, average_high integer);

INSERT INTO weather (city, year, warm_month, cold_month, average_high)  VALUES('New York City',2013,'July','January',62);
INSERT INTO weather (city, year, warm_month, cold_month, average_high)  VALUES('Boston',2013,'July','January',59);
INSERT INTO weather (city, year, warm_month, cold_month, average_high)  VALUES('Chicago',2013,'July','January',59);
INSERT INTO weather (city, year, warm_month, cold_month, average_high)  VALUES('Miami',2013,'August','January',84);
INSERT INTO weather (city, year, warm_month, cold_month, average_high)  VALUES('Dallas',2013,'July','January',77);
INSERT INTO weather (city, year, warm_month, cold_month, average_high)  VALUES('Seattle',2013,'July','January',61);
INSERT INTO weather (city, year, warm_month, cold_month, average_high)  VALUES('Portland',2013,'July','December',63);
INSERT INTO weather (city, year, warm_month, cold_month, average_high)  VALUES('San Francisco',2013,'September','December',64);
INSERT INTO weather (city, year, warm_month, cold_month, average_high)  VALUES('Los Angeles',2013,'September','December',75);
