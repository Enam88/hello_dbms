CREATE DATABASE IF NOT EXISTS somecompany

CREATE TABLE employees(
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    birthdate DATE,
    position VARCHAR(255),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE departments(
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(255),
    department_head INT,
    location VARCHAR(255),
    FOREIGN KEY (department_head) REFERENCES employees(employee_id)
);

INSERT INTO employees (first_name, last_name, birthdate, position, department_id)
VALUES 
("John", "Doe", "1990-05-15", "Software Engineer", 1 ),
("Jane", "Smith", "1985-08-20", "Project
Manager", 2),
("Mike", "Johnson", "1992-03-10", "Data Analyst", 1),
("Emily", "Brown", "1988-12-03", "UX Designer", 1),
("Alex", "Williams", "1995-06-28", "Software
Developer", 1),
("Sarah", "Miller", "1987-09-18", "HR Specialist", 3),
("Ethan", "Clark", "1991-02-14", "Database
Administrator", 1),
("Olivia", "Garcia", "1984-07-22", "Marketing
Manager", 2),
("Emilia", "Clark", "1986-01-12", "HR Manager", 3),
("Daniel", "Taylor", "1993-11-05", "Systems
Analyst", 1),
("William", "Lee", "1994-08-15", "Software
Engineer", 1),
("Sophia", "Baker", "1990-06-25", "IT Manager", 2);

SELECT first_name, last_name, position FROM employees;

UPDATE employees SET position = "Software Engineer" WHERE employee_id = 1;

DELETE FROM employees WHERE employee_id = 1;

SELECT first_name, last_name, department_name, location FROM employees INNER JOIN departments ON employees.department_id = departments.department_id;

SELECT first_name, last_name, department_name, location FROM employees INNER JOIN departments ON employees.department_id = departments.department_id WHERE department_name = "IT";

SELECT first_name, last_name, department_name, location FROM employees INNER JOIN departments ON employees.department_id = departments.department_id WHERE department_name = "Project Management";

SELECT first_name, last_name, department_name, location FROM employees INNER JOIN departments ON employees.department_id = departments.department_id WHERE department_name = "Human Resources";

SELECT department_name, first_name, last_name FROM departments INNER JOIN employees ON departments.department_head = employees.employee_id ORDER BY department_name;

INSERT INTO departments (department_name, department_head, location) VALUES ("Marketing", 8, "Paris");

CREATE TABLE Projects(
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255),
    start_date DATE,
    end_date DATE,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

INSERT INTO Projects (project_name, start_date, end_date, department_id) VALUES ("Project 1", "2020-01-01", "2020-02-01", 1),
("Project 2", "2020-02-01", "2020-03-01", 1),
("Project 3", "2020-03-01", "2020-04-01", 1),
("Project 4", "2020-04-01", "2020-05-01", 1),
("Project 5", "2020-05-01", "2020-06-01", 1),
("Project 6", "2020-06-01", "2020-07-01", 1),
("Project 7", "2020-07-01", "2020-08-01", 1),
("Project 8", "2020-08-01", "2020-09-01", 1),
("Project 9", "2020-09-01", "2020-10-01", 1),
("Project 10", "2020-10-01", "2020-11-01", 1),
("Project 11", "2020-11-01", "2020-12-01", 1),
("Project 12", "2020-12-01", "2021-01-01", 1),
("Project 13", "2021-01-01", "2021-02-01", 1),
("Project 14", "2021-02-01", "2021-03-01", 1),
("Project 15", "2021-03-01", "2021-04-01", 1),
("Project 16", "2021-04-01", "2021-05-01", 1),
("Project 17", "2021-05-01", "2021-06-01", 1),
("Project 18", "2021-06-01", "2021-07-01", 1),
("Project 19", "2021-07-01", "2021-08-01", 1);
