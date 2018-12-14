CREATE DATABASE warsztat_2_war_pyt_s_12;

CREATE TABLE Users(
  id SERIAL,
  email VARCHAR(255) UNIQUE,
  username VARCHAR(255),
  hashed_password VARCHAR(80),
  PRIMARY KEY(id)
);