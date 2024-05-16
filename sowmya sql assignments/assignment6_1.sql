show databases;

use temp5;

show tables from temp5;

select * from books;

desc books;

insert into books 
values (1, 'life', 'me', '2024', 'motivation', '123ABC');

SHOW GRANTS FOR 'sowmya2'@'localhost';

insert into books 
values (2, 'zindagi', 'me', '2024', 'motivation', '456ABC');

select * from books;

update books
set author='sowmya' where title='zindagi';

update books
set author='gowri' where title='zindagi';

