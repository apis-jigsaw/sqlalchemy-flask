drop table if exists bartenders;
drop table if exists customers;
drop table if exists drinks;
drop table if exists orders;
drop table if exists ingredients_drinks;
drop table if exists ingredients;


CREATE TABlE IF NOT EXISTS bartenders (
  id serial PRIMARY KEY,
  name TEXT,
  hometown TEXT,
  birthyear INTEGER
);

  CREATE TABLE IF NOT EXISTS customers (
    id serial PRIMARY KEY,
    name TEXT,
    hometown TEXT,
    birthyear INTEGER
  );



CREATE TABLE IF NOT EXISTS drinks (
    id serial PRIMARY KEY,
    name TEXT,
    calories INTEGER,
    price INTEGER,
    alcoholic INTEGER
  );


CREATE TABLE IF NOT EXISTS orders (
    id serial PRIMARY KEY,
    customer_id INTEGER,
    drink_id INTEGER,
    bartender_id INTEGER
  );


CREATE TABLE IF NOT EXISTS ingredients (
    id serial PRIMARY KEY,
    name TEXT,
    price INTEGER
  );


CREATE TABLE IF NOT EXISTS ingredients_drinks (
  id serial PRIMARY KEY,
  drink_id INTEGER,
  ingredient_id INTEGER
);



