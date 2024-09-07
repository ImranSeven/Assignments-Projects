--*****PLEASE ENTER YOUR DETAILS BELOW*****
--T1-pf-schema.sql

--Student ID: 33375739
--Student Name: Muhammad Imran Roslan


/* Comments for your marker:




*/

-- Task 1 Add Create table statements for the Missing TABLES below.
-- Ensure all column comments, and constraints (other than FK's)are included. 
-- FK constraints are to be added at the end of this script

-- VISIT
CREATE TABLE VISIT (
    visit_id            Numeric(5) NOT NULL,
    visit_date_time     DATE NOT NULL,
    visit_length        Numeric(2) NOT NULL,
    visit_notes         VARCHAR(200) NOT NULL,
    visit_weight        Numeric(4,1),
    visit_total_cost    Numeric(6,2),
    animal_id           Numeric(5) NOT NULL,
    vet_id              Numeric(4) NOT NULL,
    clinic_id           Numeric(2) NOT NULL,
    from_visit_id       Numeric(5)
);

COMMENT ON COLUMN VISIT.visit_id IS
    'Identifier for visit (added surrogate key)';

COMMENT ON COLUMN VISIT.visit_date_time IS
    'Date and time of visit';

COMMENT ON COLUMN VISIT.visit_length IS
    'Visit length in minutes 
        (must be between 30 - 90 minutes, inclusive)';

COMMENT ON COLUMN VISIT.visit_notes IS
    'Vet notes from visit';

COMMENT ON COLUMN VISIT.visit_weight IS
    'Weight in Kgs';

COMMENT ON COLUMN VISIT.visit_total_cost IS
    'Total cost for this visit';

COMMENT ON COLUMN VISIT.animal_id IS
    'Animal identifier';

COMMENT ON COLUMN VISIT.vet_id IS
    'Identifier for the vet';

COMMENT ON COLUMN VISIT.clinic_id IS
    'Identifier for the clinic';

COMMENT ON COLUMN VISIT.from_visit_id IS
    'The previous visit’s identifier 
        (for follow-up visit only)';

ALTER TABLE VISIT ADD CONSTRAINT visit_pk PRIMARY KEY (visit_id);

ALTER TABLE VISIT ADD CONSTRAINT uq_visit UNIQUE (visit_date_time, animal_id);

ALTER TABLE VISIT ADD CONSTRAINT chk_visit_length CHECK (
    visit_length >= 30 AND visit_length <= 90);

-- VISIT_DRUG
CREATE TABLE VISIT_DRUG(
    visit_id                NUMERIC(5) NOT NULL,
    drug_id                 NUMERIC(4) NOT NULL,
    visit_drug_dose         VARCHAR(20) NOT NULL,
    visit_drug_frequency    VARCHAR(20) NOT NULL,
    visit_drug_qtysupplied  NUMERIC(2) NOT NULL,
    visit_drug_linecost     NUMERIC(5,2) NOT NULL
);

COMMENT ON COLUMN VISIT_DRUG.visit_id IS
    'Identifier for visit (added surrogate key)';

COMMENT ON COLUMN VISIT_DRUG.drug_id IS
    'Drug identifier';

COMMENT ON COLUMN VISIT_DRUG.visit_drug_dose IS
    'Dose prescribed in this visit';

COMMENT ON COLUMN VISIT_DRUG.visit_drug_frequency IS
    'Frequency prescribed for this drug for this visit';

COMMENT ON COLUMN VISIT_DRUG.visit_drug_qtysupplied IS
    'Quantity of drug supplied';

COMMENT ON COLUMN VISIT_DRUG.visit_drug_linecost IS
    'Cost charged for drug in this visit';

ALTER TABLE VISIT_DRUG ADD CONSTRAINT VISIT_DRUG_pk PRIMARY KEY (visit_id, drug_id);

-- VISIT_SERVICE
CREATE TABLE VISIT_SERVICE(
    visit_id                NUMERIC(5) NOT NULL,
    service_code            CHAR(5) NOT NULL,
    visit_service_linecost  Numeric(6,2)
);

COMMENT ON COLUMN VISIT_SERVICE.visit_id IS
    'Identifier for visit (added surrogate key)';

COMMENT ON COLUMN VISIT_SERVICE.service_code IS
    'Service identifier';

COMMENT ON COLUMN VISIT_SERVICE.visit_service_linecost IS
    'Cost charged for this service in this visit';

ALTER TABLE VISIT_SERVICE ADD CONSTRAINT VISIT_SERVICE_pk PRIMARY KEY (visit_id, service_code);

-- Add all missing FK Constraints below here

ALTER TABLE VISIT
    ADD CONSTRAINT animal_visit_fk FOREIGN KEY (animal_id)
        REFERENCES animal (animal_id);

ALTER TABLE VISIT
    ADD CONSTRAINT vet_visit_fk FOREIGN KEY (vet_id)
        REFERENCES vet (vet_id);

ALTER TABLE VISIT
    ADD CONSTRAINT clinic_visit_fk FOREIGN KEY (clinic_id)
        REFERENCES clinic (clinic_id);

ALTER TABLE VISIT
    ADD CONSTRAINT visit_visit_fk FOREIGN KEY (visit_id)
        REFERENCES visit (visit_id);

ALTER TABLE VISIT_DRUG
    ADD CONSTRAINT visit_visit_drug_fk FOREIGN KEY (visit_id)
        REFERENCES visit (visit_id);

ALTER TABLE VISIT_DRUG
    ADD CONSTRAINT drug_visit_drug_fk FOREIGN KEY (drug_id)
        REFERENCES drug (drug_id);

ALTER TABLE VISIT_SERVICE
    ADD CONSTRAINT visit_visit_service_fk FOREIGN KEY (visit_id)
        REFERENCES visit (visit_id);

ALTER TABLE VISIT_SERVICE
    ADD CONSTRAINT service_visit_service_fk FOREIGN KEY (service_code)
        REFERENCES service (service_code);

commit;