-- Creation of product table
CREATE TABLE IF NOT EXISTS tb_client_id (
  ID  SERIAL PRIMARY KEY,
  first_name varchar(250) NOT NULL,
  last_name varchar(450) NOT NULL,
  email varchar(250) NOT NULL,
  pass varchar(250) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_users_id (
  ID SERIAL PRIMARY KEY,
  public_id VARCHAR(40) UNIQUE NOT NULL,
  username VARCHAR(64) NOT NULL,
  email VARCHAR(64) NOT NULL,
  password VARCHAR(288) NOT NULL,
  creation_date DATE NOT NULL,
  last_access TIMESTAMP NOT NULL,
  admin BOOL NOT NULL
);
