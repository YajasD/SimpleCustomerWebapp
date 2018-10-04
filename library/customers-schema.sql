-- sqlite3 customers.db < customers-schema.sql

drop table if exists customers;
create table customers (
  id integer primary key autoincrement,
  Name text not null,
  Email varchar(320) not null
);
