# password-manager
create random strong passwords, store, and retrieve them .......

use the master_pass.py to generate your master-hash and place the hash in code.py in line 11

you'll need to first install mysql in your computer and create a database called passwords and a table called passwords in the passwords database with Domain, Username, Password fields.
you also must enter your mysql access credentials in the code.py in line 27

syntax to create the database:

create database passwords;
use passwords;
create table passwords(domain varchar(20),username varchar(20),password varchar(20));
