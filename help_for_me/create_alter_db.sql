DROP TABLE lesson_student;

ALTER TABLE type_status_student_in_lesson
RENAME TO student_visit;

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

CREATE TYPE lesson_status AS ENUM ('plane', 'statement');

ALTER TABLE lesson
DROP COLUMN status_id,
ADD COLUMN status_id lesson_status;

DROP TABLE status_lesson;

ALTER TABLE type_lesson
RENAME TO lesson_type;
