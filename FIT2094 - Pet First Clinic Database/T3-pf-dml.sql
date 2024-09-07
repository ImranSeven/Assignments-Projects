/*****PLEASE ENTER YOUR DETAILS BELOW*****/
--T3-pf-dml.sql

--Student ID: 33375739
--Student Name: Muhammad Imran Roslan

/* Comments for your marker:

 Assumption 1: The follow up visit is the same length as the original visit
 Assumption 2: Give Oreo the weight of 7kg



*/

/*(a)*/

DROP SEQUENCE visit_seq;
CREATE SEQUENCE visit_seq START WITH 100 INCREMENT BY 10;

/*(b)*/

-- Insert the visit details into the VISIT table
INSERT INTO VISIT VALUES(
    visit_seq.NEXTVAL,
    TO_DATE('19-May-2024 14:00:00', 'DD-Mon-YYYY HH24:MI:SS'),
    30,
    'General consultation',
    NULL,
    NULL,
    (
        SELECT
            animal_id
        FROM
            animal
        WHERE
            upper(animal_name) = upper('Oreo')
            AND animal_born = TO_DATE('01-Jun-2018', 'DD-Mon-YYYY')
    ),
    (
        SELECT
            vet_id
        FROM
            vet
        WHERE
            upper(VET_GIVENNAME) = upper('Anna')
            AND upper(VET_FAMILYNAME) = upper('Kowalski')
    ),
    3,
    NULL
);

-- Insert the visit service details into the VISIT_SERVICE table
INSERT INTO VISIT_SERVICE VALUES (
    visit_seq.CURRVAL,
    'S001',
    NULL
);

commit;

/*(c)*/

-- Record the treatment given to Oreo during the visit
INSERT INTO VISIT_DRUG VALUES (
    (
        SELECT 
        visit_id 
    FROM 
        VISIT 
    WHERE 
        visit_date_time = TO_DATE('19-May-2024 14:00:00', 'DD-Mon-YYYY HH24:MI:SS')
    ),
    (
        SELECT 
            drug_id 
        FROM 
            DRUG 
        WHERE 
            upper(drug_name) = upper('Clotrimazole')
    ),
    '1 bottle',
    'As prescribed',
    1,
    (
        SELECT
            DRUG_STD_COST
        FROM
            DRUG
        WHERE
            upper(drug_name) = upper('Clotrimazole')
    )
);  

-- Schedule a follow-up visit for Oreo
INSERT INTO VISIT VALUES(
    visit_seq.NEXTVAL,
    TO_DATE('26-May-2024 14:00:00', 'DD-Mon-YYYY HH24:MI:SS'),
    30,
    'Follow-up from previous visit',
    NULL,
    NULL,
    (
        SELECT
            animal_id
        FROM
            animal
        WHERE
            upper(animal_name) = upper('Oreo')
            AND animal_born = TO_DATE('01-Jun-2018', 'DD-Mon-YYYY')
    ),
    (
        SELECT
            vet_id
        FROM
            vet
        WHERE
            upper(VET_GIVENNAME) = upper('Anna')
            AND upper(VET_FAMILYNAME) = upper('Kowalski')
    ),
    3,
    (
        SELECT
            VISIT_ID
        FROM
            visit
        WHERE
            VISIT_DATE_TIME = to_date('19-May-2024 14:00:00', 'DD-Mon-YYYY HH24:MI:SS')
    )
);

commit;

-- Update visit service code for original visit
UPDATE VISIT_SERVICE
    SET
        service_code = (
            SELECT
                SERVICE_CODE
            FROM
                SERVICE
            WHERE
                upper(service_desc) = upper('ear infection treatment')
        )
    WHERE
        visit_id = (
            SELECT
                VISIT_ID
            FROM
                visit
            WHERE
                VISIT_DATE_TIME = to_date('19-May-2024 14:00:00', 'DD-Mon-YYYY HH24:MI:SS')
    );

commit;

-- Update visit service linecost for original visit
UPDATE VISIT_SERVICE
    SET
        visit_service_linecost = (
            SELECT
                service_std_cost
            FROM
                SERVICE
            WHERE
                upper(service_desc) = upper('ear infection treatment')
        )
    WHERE
        visit_id = (
            SELECT
                VISIT_ID
            FROM
                visit
            WHERE
                VISIT_DATE_TIME = to_date('19-May-2024 14:00:00', 'DD-Mon-YYYY HH24:MI:SS')
    );

commit;

-- Update Oreo's weight
UPDATE VISIT
    SET
        VISIT_WEIGHT = 7.0
    WHERE
        visit_id = (
            SELECT
                VISIT_ID
            FROM
                visit
            WHERE
                VISIT_DATE_TIME = to_date('19-May-2024 14:00:00', 'DD-Mon-YYYY HH24:MI:SS')
    );

commit;

-- Update original visit's visit note
UPDATE VISIT
    SET
        visit_notes = 'Ear infection treatment'
    WHERE
        visit_id = (
            SELECT
                VISIT_ID
            FROM
                visit
            WHERE
                VISIT_DATE_TIME = to_date('19-May-2024 14:00:00', 'DD-Mon-YYYY HH24:MI:SS')
    );

commit;

-- Update total visit cost for original visit
UPDATE VISIT
    SET
        VISIT_TOTAL_COST = (
            SELECT 
                NVL(SUM(visit_service_linecost), 0) + NVL(SUM(visit_drug_linecost), 0)
            FROM 
                VISIT_SERVICE vs
                JOIN VISIT_DRUG vd
                    ON vs.visit_id = vd.visit_id
            WHERE 
                vs.visit_id = (
                    SELECT 
                        visit_id
                    FROM 
                        VISIT
                    WHERE 
                        visit_date_time = TO_DATE('19-May-2024 14:00:00', 'DD-Mon-YYYY HH24:MI:SS')
                AND animal_id = (
                    SELECT 
                        animal_id
                    FROM 
                        ANIMAL
                    WHERE 
                        upper(animal_name) = upper('Oreo')
                )
            )
        )
    WHERE
        visit_id = (
            SELECT
                VISIT_ID
            FROM
                visit
            WHERE
                VISIT_DATE_TIME = to_date('19-May-2024 14:00:00', 'DD-Mon-YYYY HH24:MI:SS')
    );

commit;

/*(d)*/

-- Find and delete the follow-up visit for Oreo scheduled on 26-May-2024
DELETE FROM VISIT
WHERE 
    visit_date_time = to_date('26-May-2024 14:00:00', 'DD-Mon-YYYY HH24:MI:SS')
    AND animal_id = (
        SELECT 
            animal_id
        FROM 
            animal
        WHERE 
            upper(animal_name) = upper('Oreo')
    )
    AND vet_id = (
        SELECT 
            vet_id
        FROM 
            vet
        WHERE 
            upper(VET_GIVENNAME) = upper('Anna')
            AND upper(VET_FAMILYNAME) = upper('Kowalski')
);

COMMIT;