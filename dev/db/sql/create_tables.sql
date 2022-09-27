-- Creation of product table
CREATE TABLE IF NOT EXISTS tb_client_id (
  ID  SERIAL PRIMARY KEY,
  first_name varchar(250) NOT NULL,
  last_name varchar(450) NOT NULL,
  email varchar(250) NOT NULL,
  pass varchar(250) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_users_id (
  ID Serial PRIMARY KEY,
  first_name varchar(50) NOT NULL,
  last_name varchar(50) NOT NULL,
  email varchar(100) NOT NULL,
  pass varchar(300) NOT NULL
);
