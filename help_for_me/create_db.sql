CREATE TABLE IF NOT EXISTS studio (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    is_active BOOLEAN DEFAULT True
);

SELECT * FROM studio;

CREATE TABLE IF NOT EXISTS branch (
    id INTEGER PRIMARY KEY,
    studio_id INTEGER NOT NULL,
    FOREIGN KEY (studio_id) REFERENCES studio(id),
    name VARCHAR(50),
    address TEXT,
    is_active BOOLEAN DEFAULT True
);

SELECT * FROM branch;

CREATE TABLE IF NOT EXISTS room (
    id INTEGER PRIMARY KEY,
    branch_id INTEGER NOT NULL,
    FOREIGN KEY (branch_id) REFERENCES branch(id),
    name VARCHAR(50),
    is_active BOOLEAN DEFAULT True
);

SELECT * FROM room;

CREATE TABLE IF NOT EXISTS role (
    id INTEGER PRIMARY KEY,
    type VARCHAR(50)
);

SELECT * FROM role;

CREATE TYPE gender_user AS ENUM ('male', 'female');

CREATE TABLE IF NOT EXISTS stuff (
    id INTEGER PRIMARY KEY,
    surname VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    gender gender_user,
    phone VARCHAR(12) NOT NULL UNIQUE,
    email VARCHAR(150) UNIQUE,
    role_id INTEGER NOT NULL,
    FOREIGN KEY (role_id) REFERENCES role(id),
    created_at TIMESTAMP,
    changed_at TIMESTAMP,
    is_active BOOLEAN DEFAULT True
);

SELECT * FROM stuff;

CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    surname VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    gender gender_user,
    phone VARCHAR(12) NOT NULL UNIQUE,
    email VARCHAR(150) UNIQUE,
    created_at TIMESTAMP,
    changed_at TIMESTAMP,
    is_active BOOLEAN DEFAULT True
);

SELECT * FROM student;

CREATE TABLE IF NOT EXISTS class (
    id INTEGER PRIMARY KEY,
    branch_id INTEGER NOT NULL,
    FOREIGN KEY (branch_id) REFERENCES branch(id),
    teacher_id INTEGER NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES stuff(id),
    name VARCHAR(100) NOT NULL,
    age_min SMALLINT,
    age_max SMALLINT,
    created_at TIMESTAMP,
    changed_at TIMESTAMP,
    is_active BOOLEAN DEFAULT True
);

SELECT * FROM class;

CREATE TABLE IF NOT EXISTS class_student (
    class_id INTEGER NOT NULL,
    FOREIGN KEY (class_id) REFERENCES class(id),
    student_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES student(id),
    PRIMARY KEY (class_id, student_id),
    added_at TIMESTAMP,
    excluded_at TIMESTAMP,
    is_active BOOLEAN DEFAULT True
);

SELECT * FROM class_student;

CREATE TABLE IF NOT EXISTS lesson_type (
    id INTEGER PRIMARY KEY,
    type VARCHAR(100) NOT NULL
);

SELECT * FROM lesson_type;

CREATE TYPE lesson_status AS ENUM ('plane', 'statement');

CREATE TABLE IF NOT EXISTS lesson (
    id INTEGER PRIMARY KEY,
    type_id INTEGER NOT NULL,
    FOREIGN KEY (type_id) REFERENCES lesson_type(id),
    class_id INTEGER NOT NULL,
    FOREIGN KEY (class_id) REFERENCES class(id),
    room_id INTEGER NOT NULL,
    FOREIGN KEY (room_id) REFERENCES room(id),
    date DATE NOT NULL,
    time_start TIME,
    time_stop TIME,
    created_at TIMESTAMP,
    changed_at TIMESTAMP,
    status_id lesson_status
);

SELECT * FROM lesson;

CREATE TABLE IF NOT EXISTS student_visit (
    id SMALLINT PRIMARY KEY,
    type VARCHAR(50) NOT NULL
);

SELECT * FROM student_visit;

CREATE TABLE IF NOT EXISTS lesson_student (
    lesson_id INTEGER NOT NULL,
    FOREIGN KEY (lesson_id) REFERENCES lesson(id),
    student_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES student(id),
    PRIMARY KEY (lesson_id, student_id),
    visit_id SMALLINT NOT NULL,
    FOREIGN KEY (visit_id) REFERENCES student_visit(id),
    created_at TIMESTAMP,
    changed_at TIMESTAMP
);

SELECT * FROM lesson_student;

\d+ lesson

SELECT t.typname, e.enumlabel 
FROM pg_type t, pg_enum e
WHERE t.oid = e.enumtypid AND typname = 'lesson_status';

ALTER TYPE lesson_status
  ADD VALUE 'finished' AFTER 'statement';

#Просмотр всех возможных значений
select t.typname, e.enumlabel 
 from pg_type t, pg_enum e 
 where t.oid = e.enumtypid and typname = 'e_contact_method';

#Добавление новых значений
ALTER TYPE e_contact_method 
  ADD VALUE 'Facebook' AFTER 'Phone';

#Изменение строки на enum в существующей таблице
ALTER TABLE transactions_enum 
  ALTER COLUMN status 
  TYPE enum_transaction_status 
  USING status::text::enum_transaction_status;