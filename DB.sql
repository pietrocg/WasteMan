CREATE DATABASE Wasteman;

CREATE TABLE Users (
user_id BIGINT UNIQUE AUTO_INCREMENT,
email VARCHAR(100) UNIQUE NOT NULL,
password VARCHAR(100) NOT NULL,
user_type TEXT NOT NULL,
user_address_latitude DECIMAL(19,17),
user_address_longitude DECIMAL(19,17),
PRIMARY KEY (user_id),
);



CREATE TABLE Reports (
report_id BIGINT NOT NULL AUTO_INCREMENT,
user_id BIGINT NOT NULL,
report_time TIMESTAMP NOT NULL CURRENT_TIMESTAMP,
report_latitude DECIMAL(19,17) NOT NULL,
report_longitude DECIMAL(19,17) NOT NULL,
report_photo VARBINARY(60000) NOT NULL,
report_description TEXT,
collected BOOL,
PRIMARY KEY (report_id),
FOREIGN KEY (user_id)
);