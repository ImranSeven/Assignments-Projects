/*****PLEASE ENTER YOUR DETAILS BELOW*****/
--T6-pf-json.sql

--Student ID: 33375739
--Student Name: Muhammad Imran Roslan


/* Comments for your marker:




*/

-- PLEASE PLACE REQUIRED SQL SELECT STATEMENT TO GENERATE 
-- THE COLLECTION OF JSON DOCUMENTS HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer

SELECT JSON_OBJECT(
    '_id' VALUE c.clinic_id,
    'name' VALUE c.clinic_name,
    'address' VALUE c.clinic_address,
    'phone' VALUE c.clinic_phone,
    'head_vet' VALUE JSON_OBJECT(
        'id' VALUE v.vet_id,
        'name' VALUE v.vet_givenname || ' ' || v.vet_familyname),
    'no_of_vets' VALUE (
        SELECT 
            COUNT(*) 
        FROM 
            vet v2 
        WHERE 
            v2.clinic_id = c.clinic_id),
    'vets' VALUE JSON_ARRAYAGG(
        JSON_OBJECT(
            'id' VALUE v2.vet_id,
            'name' VALUE v2.vet_givenname || ' ' || v2.vet_familyname,
            'specialisation' VALUE NVL(s.spec_description, 'N/A')))
FORMAT JSON) || ','

FROM 
    clinic c
    JOIN vet v 
        ON c.vet_id = v.vet_id
    LEFT JOIN vet v2 
        ON c.clinic_id = v2.clinic_id
    LEFT JOIN specialisation s 
        ON v2.spec_id = s.spec_id
GROUP BY 
    c.clinic_id, 
    c.clinic_name, 
    c.clinic_address, 
    c.clinic_phone, 
    v.vet_id, 
    v.vet_givenname, 
    v.vet_familyname;