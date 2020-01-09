CREATE TABLE crime
(
incident_no	integer,
high_offense_description	varchar(256),
high_offense_code	integer,
fam_violence	varchar(5),
occurred_date_time	date,
occurred_date	date,
occurred_time	integer,
report_date_time	date,
report_date	date,
report_time	integer,
location_type	varchar(256),
address	varchar(256),
zip	integer,
district	varchar(5),
apd_sector	varchar(5),
apd_district	varchar(5),
pra	integer,
census_tract	numeric(10, 2),
clearance_status	varchar(5),
clearance_date	date,
ucr_category	varchar(40),
category_description	varchar(100),
x_coord	integer,
y_coord	integer,
lat	numeric(11, 10),
lng	numeric(11, 10),
location	varchar(100)
);



CREATE TABLE bars
(
id	varchar(80),
alias	varchar(256),
name	varchar(256),
review_count	integer,
rating	numeric(2, 2),
latitude	numeric(10,7),
longitude	numeric(10,7),
price	varchar(5),
address1	varchar(80),
address2	varchar(80),
address3	varchar(80),
city	varchar(20),
zip	varchar(10),
country	varchar(5),
state	varchar(5)
);
