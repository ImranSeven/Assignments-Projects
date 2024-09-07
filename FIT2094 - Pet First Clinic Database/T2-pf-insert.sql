/*****PLEASE ENTER YOUR DETAILS BELOW*****/
--T2-pf-insert.sql

--Student ID: 33375739
--Student Name: Muhammad Imran Roslan

/* Comments for your marker:




*/

--------------------------------------
--INSERT INTO visit
--------------------------------------
INSERT INTO VISIT VALUES (
    1,
    to_date('01-Apr-2024 10:00:00','dd-Mon-yyyy HH:MI:SS'),
    60,
    'Routine check-up',
    12.5,
    100.00,
    1,
    1001,
    1,
    NULL
);

INSERT INTO VISIT VALUES (
    2,
    to_date('02-Apr-2024 11:00:00','dd-Mon-yyyy HH24:MI:SS'),
    45,
    'Vaccination',
    15.0,
    75.00,
    2,
    1001,
    2,
    NULL
);

INSERT INTO VISIT VALUES (
    3,
    to_date('03-Apr-2024 09:00:00','dd-Mon-yyyy HH24:MI:SS'),
    30,
    'Follow-up visit',
    12.8,
    50.00,
    1,
    1002,
    1,
    1
);

INSERT INTO VISIT VALUES (
    4,
    to_date('04-Apr-2024 14:00:00','dd-Mon-yyyy HH24:MI:SS'),
    90,
    'Surgery',
    18.2,
    300.00,
    3,
    1002,
    3,
    NULL
);

INSERT INTO VISIT VALUES (
    5,
    to_date('05-Apr-2024 10:30:00','dd-Mon-yyyy HH24:MI:SS'),
    60,
    'Dental Cleaning',
    14.5,
    120.00,
    4,
    1003,
    2,
    NULL
);

INSERT INTO VISIT VALUES (
    6,
    to_date('06-Apr-2024 12:00:00','dd-Mon-yyyy HH24:MI:SS'),
    30,
    'Routine check-up',
    11.3,
    100.00,
    5,
    1003,
    1,
    NULL
);

INSERT INTO VISIT VALUES (
    7,
    to_date('01-May-2024 10:00:00','dd-Mon-yyyy HH24:MI:SS'),
    60,
    'Vaccination',
    16.7,
    85.00,
    1,
    1001,
    2,
    3
);

INSERT INTO VISIT VALUES (
    8,
    to_date('02-May-2024 13:00:00','dd-Mon-yyyy HH24:MI:SS'),
    45,
    'Follow-up visit',
    18.0,
    75.00,
    2,
    1002,
    3,
    2
);

INSERT INTO VISIT VALUES (
    9,
    to_date('01-Jun-2024 12:00:00','dd-Mon-yyyy HH24:MI:SS'),
    30,
    'Routine check-up',
    14.2,
    50.00,
    3,
    1001,
    1,
    NULL
);

INSERT INTO VISIT VALUES (
    10,
    to_date('15-Jun-2024 12:00:00','dd-Mon-yyyy HH24:MI:SS'),
    45,
    'Vaccination',
    12.5,
    75.00,
    5,
    1003,
    2,
    NULL
);

INSERT INTO VISIT VALUES (
    11,
    to_date('20-Jun-2024 12:00:00','dd-Mon-yyyy HH24:MI:SS'),
    45,
    'Check-up',
    13.0,
    70.00,
    1,
    1001,
    1,
    NULL
);

INSERT INTO VISIT VALUES (
    12,
    to_date('21-Jun-2024 12:00:00','dd-Mon-yyyy HH24:MI:SS'),
    45,
    'Follow-up after surgery',
    19.0,
    60.00,
    3,
    1002,
    3,
    4
);

INSERT INTO VISIT VALUES (
    13,
    to_date('22-Jun-2024 12:00:00','dd-Mon-yyyy HH24:MI:SS'),
    60,
    'Dental follow-up',
    15.0,
    90.00,
    4,
    1003,
    2,
    5
);

INSERT INTO VISIT VALUES (
    14,
    to_date('23-Jun-2024 12:00:00','dd-Mon-yyyy HH24:MI:SS'),
    60,
    'Vaccination',
    16.0,
    80.00,
    2,
    1001,
    1,
    NULL
);

INSERT INTO VISIT VALUES (
    15,
    to_date('24-Jun-2024 12:00:00','dd-Mon-yyyy HH24:MI:SS'),
    45,
    'Check-up',
    17.0,
    70.00,
    5,
    1002,
    3,
    NULL
);

--------------------------------------
--INSERT INTO visit_service
--------------------------------------
INSERT INTO VISIT_SERVICE VALUES (
    1, 
    'S001', 
    50.00
);

INSERT INTO VISIT_SERVICE VALUES (
    1, 
    'S002', 
    50.00
);

INSERT INTO VISIT_SERVICE VALUES (
    2, 
    'S003', 
    75.00
);

INSERT INTO VISIT_SERVICE VALUES (
    3, 
    'S001', 
    50.00
);

INSERT INTO VISIT_SERVICE VALUES (
    3, 
    'S004', 
    25.00
);

INSERT INTO VISIT_SERVICE VALUES (
    4, 
    'S005', 
    300.00
);

INSERT INTO VISIT_SERVICE VALUES (
    5, 
    'S006', 
    120.00
);

INSERT INTO VISIT_SERVICE VALUES (
    6, 
    'S001', 
    50.00
);

INSERT INTO VISIT_SERVICE VALUES (
    7, 
    'S003', 
    85.00
);

INSERT INTO VISIT_SERVICE VALUES (
    8, 
    'S002', 
    75.00
);

INSERT INTO VISIT_SERVICE VALUES (
    9, 
    'S001', 
    50.00
);

INSERT INTO VISIT_SERVICE VALUES (
    9, 
    'S007', 
    25.00
);

INSERT INTO VISIT_SERVICE VALUES (
    10, 
    'S003', 
    75.00
);

INSERT INTO VISIT_SERVICE VALUES (
    10, 
    'S008', 
    50.00
);

INSERT INTO VISIT_SERVICE VALUES (
    10, 
    'S009', 
    25.00
);

INSERT INTO VISIT_SERVICE VALUES (
    11, 
    'S001', 
    70.00
);

INSERT INTO VISIT_SERVICE VALUES (
    12, 
    'S005', 
    60.00
);

INSERT INTO VISIT_SERVICE VALUES (
    13, 
    'S006', 
    90.00
);

INSERT INTO VISIT_SERVICE VALUES (
    14, 
    'S003', 
    80.00
);

INSERT INTO VISIT_SERVICE VALUES (
    15, 
    'S002', 
    70.00
);

INSERT INTO VISIT_SERVICE VALUES (
    15, 
    'S004', 
    30.00
);

INSERT INTO VISIT_SERVICE VALUES (
    5, 
    'S003', 
    60.00
);

INSERT INTO VISIT_SERVICE VALUES (
    6, 
    'S005', 
    70.00
);

INSERT INTO VISIT_SERVICE VALUES (
    11, 
    'S002', 
    40.00
);

INSERT INTO VISIT_SERVICE VALUES (
    7, 
    'S006', 
    90.00
);

INSERT INTO VISIT_SERVICE VALUES (
    8, 
    'S007', 
    55.00
);

--------------------------------------
--INSERT INTO visit_drug
--------------------------------------
INSERT INTO VISIT_DRUG VALUES (
    1, 
    101, 
    1, 
    'Once daily', 
    30, 
    25.00
);

INSERT INTO VISIT_DRUG VALUES (
    2, 
    102, 
    2, 
    'Twice daily', 
    60, 
    50.00
);

INSERT INTO VISIT_DRUG VALUES (
    3, 
    101, 
    1, 
    'Once daily', 
    30, 
    25.00
);

INSERT INTO VISIT_DRUG VALUES (
    4, 
    103, 
    3, 
    'Three times daily', 
    90, 
    100.00
);

INSERT INTO VISIT_DRUG VALUES (
    5, 
    102, 
    2, 
    'Once daily', 
    30, 
    50.00
);

INSERT INTO VISIT_DRUG VALUES (
    6, 
    101, 
    1, 
    'Once daily', 
    30, 
    25.00
);

INSERT INTO VISIT_DRUG VALUES (
    7, 
    102, 
    2, 
    'Twice Daily', 
    60, 
    50.00
);

INSERT INTO VISIT_DRUG VALUES (
    8, 
    103, 
    3, 
    'Three times daily', 
    90, 
    100.00
);

INSERT INTO VISIT_DRUG VALUES (
    9, 
    101, 
    1, 
    'Once daily', 
    30, 
    25.00
);

INSERT INTO VISIT_DRUG VALUES (
    10, 
    102, 
    2, 
    'Twice daily', 
    60, 
    50.00
);

INSERT INTO VISIT_DRUG VALUES (
    11, 
    103, 
    2, 
    'Once daily', 
    30, 
    25.00
);

INSERT INTO VISIT_DRUG VALUES (
    12, 
    101, 
    2, 
    'Twice daily', 
    60, 
    50.00
);

INSERT INTO VISIT_DRUG VALUES (
    13, 
    102, 
    1, 
    'Once Daily', 
    30, 
    25.00
);

INSERT INTO VISIT_DRUG VALUES (
    14, 
    103, 
    3, 
    'Once daily', 
    90, 
    100.00
);

INSERT INTO VISIT_DRUG VALUES (
    15, 
    101, 
    2, 
    'Twice daily', 
    60, 
    50.00
);

INSERT INTO VISIT_DRUG VALUES (
    4, 
    102, 
    2, 
    'Once daily', 
    30, 
    25.00
);

INSERT INTO VISIT_DRUG VALUES (
    5, 
    101, 
    1, 
    'Twice daily', 
    60, 
    50.00
);

INSERT INTO VISIT_DRUG VALUES (
    6, 
    103, 
    2, 
    'Three times daily', 
    90, 
    100.00
);

INSERT INTO VISIT_DRUG VALUES (
    7, 
    104, 
    2, 
    'Once Daily', 
    30, 
    25.00
);

INSERT INTO VISIT_DRUG VALUES (
    8, 
    101, 
    3, 
    'Twice daily', 
    60, 
    50.00
);

commit;