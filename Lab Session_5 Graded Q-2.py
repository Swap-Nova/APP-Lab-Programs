-- creating a table

CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone_number INTEGER NOT NULL,
    hiring_date date,
    job_id INTEGER NOT NULL,
    salary INTEGER NOT NULL,
    comission INTEGER NOT NULL,
    manager_id INTEGER NOT NULL,
    department_id NOT NULL
);

-- inserting the values

INSERT INTO employees VALUES (001, 'Jim', 'Halpert','jimbo42@gmail.com','8823156789','22-01-2014','4565','10456','25000',100,'01');
INSERT INTO employees VALUES (006, 'Micheal', 'Scott','mgs24@gmail.com','9054128690','01-12-2015','4542','12000','28000',600,'02');
INSERT INTO employees VALUES (010, 'Dwight', 'Schrute','dks56@gmail.com','9678345678','14-04-2015','4778','14000','30000','010','03');

-- fetching the values

SELECT * FROM employees;
SELECT first_name,last_name FROM employees WHERE salary >'25000';
