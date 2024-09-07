/*****PLEASE ENTER YOUR DETAILS BELOW*****/
--T5-mag-select.sql

--Student ID: 33375739
--Student Name: Muhammad Imran Roslan


/* Comments for your marker:




*/


/* (a) */
-- PLEASE PLACE REQUIRED SQL SELECT STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer

SELECT
    LPAD(c.clinic_id, 8) AS CLINICID,
    LPAD(v.vet_id, 5) AS VETID,
    RPAD(vet_givenname || ' ' || vet_familyname, 14) AS VETNAME,
    RPAD(CASE
        WHEN c.vet_id = v.vet_id
            THEN 'HEAD VET'
        ELSE ''
    END, 8) AS ISHEAD,
    RPAD(at.atype_description, 4) AS ANIMALTYPE,
    LPAD(COUNT(vs.visit_id), 11) AS NUMBERAPPTS,
    LPAD(to_char(ROUND(
        COUNT(vs.visit_id) * 100.0 /(
            SELECT
                COUNT(*)
            FROM
                visit v2
                JOIN animal a2
                    ON v2.animal_id = a2.animal_id
                JOIN animal_type at2 
                    ON a2.atype_id = at2.atype_id
            WHERE
                v2.clinic_id = c.clinic_id
                AND upper(at2.atype_description) = upper('dog')
                    OR upper(at2.atype_description) = upper('cat')
        ), 1), '990.0') || '%', 13) AS PERCENTAPPTS
FROM
    clinic c
    JOIN vet v
        ON c.clinic_id = v.clinic_id
    JOIN visit vs
        ON v.vet_id = vs.vet_id
    JOIN animal a 
        ON vs.animal_id = a.animal_id
    JOIN animal_type at
        ON a.atype_id = at.atype_id
WHERE
    upper(at.atype_description) = upper('dog')
        OR upper(at.atype_description) = upper('cat')
GROUP BY
    c.clinic_id,
    v.vet_id,
    v.vet_givenname,
    v.vet_familyname,
    c.vet_id,
    at.atype_description
ORDER BY
    c.clinic_id,
    CASE
        WHEN c.vet_id = v.vet_id THEN 0
        ELSE v.vet_id
    END,
    v.vet_id,
    at.atype_description;


/* (b) */
-- PLEASE PLACE REQUIRED SQL SELECT STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer

SELECT
    vs.service_code,
    s.service_desc,
    v.vet_id,
    v.vet_givenname,
    v.vet_familyname,
    c.clinic_id,
    c.clinic_name,
    vs.visit_id,
    vi.visit_date_time,
    vs.visit_service_linecost
FROM
    visit_service vs
    JOIN service s
        ON vs.service_code = s.service_code
    JOIN visit vi
        ON vs.visit_id = vi.visit_id
    JOIN vet v
        ON vi.vet_id = v.vet_id
    JOIN clinic c
        ON vi.clinic_id = c.clinic_id
WHERE
    vs.visit_service_linecost > (
        SELECT
            AVG(visit_service_linecost)
        FROM
            visit_service
    )
ORDER BY
    vs.service_code,
    v.vet_id,
    vi.visit_date_time;