
# Task 1
BEGIN;
INSERT INTO booking(facility_id,
    member_id,
    start_time,
    slots) VALUES

    (
        (SELECT id FROM facility WHERE name = 'Squash Court'),
        (SELECT id FROM member WHERE name = 'Noah Wilson'),
        CURRENT_TIMESTAMP,
        2
     );

UPDATE member
SET balance = balance - 2 * (
    SELECT membercost FROM facility
    WHERE name = 'Squash Court'
)
WHERE name = 'Noah Wilson';

COMMIT;

SELECT balance FROM member
WHERE name = 'Noah Wilson';


# Task 2

BEGIN;
INSERT INTO booking(
	facility_id,
    member_id,
    start_time,
    slots) VALUES

    (
        (SELECT id FROM facility WHERE name = 'Tennis Court'),
        (SELECT id FROM member WHERE name = 'Mia Ali'),
        CURRENT_TIMESTAMP,
        3
     );

UPDATE member
SET balance = balance - 3 * (
    SELECT membercost FROM facility
    WHERE name = 'Tennis Court'
)
WHERE name = 'Mia Ali';

COMMIT;


# Task 3

BEGIN;

UPDATE member
SET balance = balance - 3 * (
    SELECT membercost FROM facility
    WHERE name = 'Tennis Court 1'
)
WHERE name = 'Noah Wilson';

INSERT INTO booking(
	facility_id,
    member_id,
    start_time,
    slots) VALUES

    (
        (SELECT id FROM facility WHERE name = 'Tennis Court 1'),
        (SELECT id FROM member WHERE name = 'Alice Peters'),
        CURRENT_TIMESTAMP,
        3
     );

COMMIT;


# Task 4

BEGIN;

UPDATE member
SET balance = balance - 3 * (
    SELECT membercost FROM facility
    WHERE name = 'Tennis Court 1'
)
WHERE name = 'Noah Wilson';


INSERT INTO booking(
	facility_id,
    member_id,
    start_time,
    slots) VALUES

    (
        (SELECT id FROM facility WHERE name = 'Tennis Court 1'),
        (SELECT id FROM member WHERE name = 'Noah Wilson'),
        CURRENT_TIMESTAMP,
        3
     );


ROLLBACK;



# Task 5

BEGIN;

UPDATE member
SET balance = balance - 1 * (
    SELECT membercost FROM facility
    WHERE name = 'Massage Room 1'
)
WHERE name = 'Ella Lee';


INSERT INTO booking(
	facility_id,
    member_id,
    start_time,
    slots) VALUES

    (
        (SELECT id FROM facility WHERE name = 'Massage Room 1'),
        (SELECT id FROM member WHERE name = 'Ella Lee'),
        CURRENT_TIMESTAMP,
        1
     );
    

SAVEPOINT reward_recommendation;

UPDATE member
SET balance = balance + 0.50
WHERE name = 'Olivia Muller';

ROLLBACK TO reward_recommendation;

COMMIT;




SELECT balance FROM member
WHERE name = 'Olivia Muller';


# Task 6

BEGIN;

UPDATE member
SET balance = balance - 3 * (
    SELECT membercost FROM facility
    WHERE name = 'Tennis Court 1'
)
WHERE name = 'Noah Wilson';


SELECT pg_sleep(10);


INSERT INTO booking(
	facility_id,
    member_id,
    start_time,
    slots) VALUES

    (
        (SELECT id FROM facility WHERE name = 'Tennis Court 1'),
        (SELECT id FROM member WHERE name = 'Noah Wilson'),
        CURRENT_TIMESTAMP,
        3
     );


COMMIT;

# Task 7

BEGIN;

LOCK TABLE member;

UPDATE member
SET balance = balance - 3 * (
    SELECT membercost FROM facility
    WHERE name = 'Tennis Court 1'
)
WHERE name = 'Noah Wilson';


SELECT pg_sleep(15);


INSERT INTO booking(
	facility_id,
    member_id,
    start_time,
    slots) VALUES

    (
        (SELECT id FROM facility WHERE name = 'Tennis Court 1'),
        (SELECT id FROM member WHERE name = 'Noah Wilson'),
        CURRENT_TIMESTAMP,
        3
     );


COMMIT;




--SELECT balance FROM member
--WHERE name = 'Noah Wilson';



# Task 8

BEGIN;

UPDATE member
SET balance = balance - 3 * (
    SELECT membercost FROM facility
    WHERE name = 'Tennis Court 1'
)
WHERE name = 'Noah Wilson';


SELECT pg_sleep(15);


INSERT INTO booking(
	facility_id,
    member_id,
    start_time,
    slots) VALUES

    (
        (SELECT id FROM facility WHERE name = 'Tennis Court 1'),
        (SELECT id FROM member WHERE name = 'Noah Wilson'),
        CURRENT_TIMESTAMP,
        3
     );


COMMIT;

ALTER TABLE member ADD COLUMN city TEXT;

