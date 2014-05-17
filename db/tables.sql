SET NAMES 'utf8';
SET CHARACTER SET utf8;

drop table if exists books;
create table books (
book_id INT not null AUTO_INCREMENT,
filename VARCHAR(256),
path VARCHAR(1024),
filesize INT not null DEFAULT 0,
format VARCHAR(8),
cat_id INT not null,
cat_type INT not null DEFAULT 0,
registerdate TIMESTAMP not null DEFAULT CURRENT_TIMESTAMP,
docdate VARCHAR(20),
favorite INT not null DEFAULT 0,
lang  VARCHAR(16),
title VARCHAR(256),
annotation VARCHAR(10000),
cover VARCHAR(32),
cover_type VARCHAR(32),
doublicat INT not null DEFAULT 0,
avail INT not null DEFAULT 0,
PRIMARY KEY(book_id),
KEY(filename),
KEY(title,format,filesize),
INDEX(path),
INDEX(cat_id),
INDEX(avail,doublicat),
INDEX(registerdate));
commit;

drop table if exists catalogs;
create table catalogs (
cat_id INT not null AUTO_INCREMENT,
parent_id INT null,
cat_name VARCHAR(64),
path VARCHAR(1024),
cat_type INT not null DEFAULT 0,
PRIMARY KEY(cat_id),
KEY(cat_name,path));
commit;

drop table if exists authors;
create table authors (
author_id INT not null AUTO_INCREMENT,
first_name VARCHAR(64),
last_name VARCHAR(64),
PRIMARY KEY(author_id),
KEY(last_name,first_name));
commit;

drop table if exists bauthors;
create table bauthors (
author_id INT not NULL,
book_id INT not NULL,
PRIMARY KEY(book_id,author_id),
INDEX(author_id));
commit;

drop table if exists genres;
create table genres(
genre_id INT not null AUTO_INCREMENT,
genre VARCHAR(32),
section VARCHAR(32),
subsection VARCHAR(32),
PRIMARY KEY(genre_id),
KEY(genre));
commit;

drop table if exists bgenres;
create table bgenres(
genre_id INT not NULL,
book_id INT not NULL,
PRIMARY KEY(book_id,genre_id),
INDEX(genre_id));
commit;

drop table if exists series;
create table series(
ser_id INT not null AUTO_INCREMENT,
ser VARCHAR(64),
PRIMARY KEY(ser_id),
KEY(ser));
commit;

drop table if exists bseries;
create table bseries(
ser_id INT not NULL,
book_id INT not NULL,
ser_no TINYINT UNSIGNED NOT NULL DEFAULT 0,
PRIMARY KEY(book_id,ser_id),
INDEX(ser_id));
commit;

drop table if exists bookshelf;
create table bookshelf(
user VARCHAR(32) not NULL,
book_id INT not NULL,
readtime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
INDEX(user,readtime));
commit;

drop table if exists dbver;
create table dbver(
ver varchar(5));
commit;

insert into dbver(ver) values("0.20");
commit;
insert into authors(author_id,last_name,first_name) values(1,"Неизвестный Автор","");
commit;

DROP PROCEDURE IF EXISTS sp_update_dbl;
DROP PROCEDURE IF EXISTS sp_newinfo;
DELIMITER //

CREATE PROCEDURE sp_update_dbl()
BEGIN
  DECLARE done INT DEFAULT 0;
  DECLARE id, dbl INT;
  DECLARE dbl_sav, id_sav INT;
  DECLARE cur CURSOR FOR select book_id, doublicat from books
                         where doublicat!=0 and avail!=0 and doublicat not in
                         (select book_id from books where doublicat=0 and avail=2) order by doublicat, book_id;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

  OPEN cur;

  SET dbl_sav=0;
  SET id_sav=0;
  WHILE done=0 DO
    FETCH cur INTO id, dbl;
    IF dbl_sav!=dbl THEN
       UPDATE books SET doublicat=0 WHERE book_id=id;
       SET dbl_sav=dbl;
       SET id_sav=id;
    ELSE
       UPDATE books SET doublicat=id_sav where book_id=id;
    END IF;
  END WHILE;

  CLOSE cur;
END //

CREATE PROCEDURE sp_newinfo(period INT)
BEGIN
  DECLARE min_book_id INT;

  select MIN(book_id) into min_book_id from books where registerdate>now()-INTERVAL period DAY;
  select 1 s, count(*) from books where book_id>=min_book_id and avail!=0 and doublicat=0
  union all
  select 2 s, count(*) from (select author_id from bauthors where book_id>=min_book_id group by author_id) a
  union all
  select 3 s, count(*) from (select genre_id from bgenres where book_id>=min_book_id group by genre_id) a
  union all
  select 4 s, count(*) from (select ser_id from bseries where book_id>=min_book_id group by ser_id) a
  order by s;

END //


DELIMITER ;
commit;

