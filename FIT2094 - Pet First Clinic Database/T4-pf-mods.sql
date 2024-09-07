/*****PLEASE ENTER YOUR DETAILS BELOW*****/
--T4-pf-mods.sql

--Student ID: 33375739
--Student Name: Muhammad Imran Roslan


/* Comments for your marker:




*/

/*(a)*/

ALTER TABLE service DROP COLUMN service_nonstd_cost_count;

DESC service;

SELECT
    *
FROM
    service;
    
-- Add the new attribute to the SERVICE table

ALTER TABLE SERVICE ADD (
    service_nonstd_cost_count Numeric (5)
        DEFAULT 0 NOT NULL);

UPDATE SERVICE
    SET
	    service_nonstd_cost_count = (
            SELECT
                COUNT(*)
            FROM
                VISIT_SERVICE vs
                JOIN service s
                    ON vs.SERVICE_CODE = s.SERVICE_CODE
            WHERE
                vs.VISIT_SERVICE_LINECOST != s.SERVICE_STD_COST
                AND SERVICE.SERVICE_CODE = s.SERVICE_CODE
        );

commit;

DESC service;

SELECT
    *
FROM
    service;

/*(b)*/

--Create the VISIT_PAYMENT_METHOD table
DROP TABLE VISIT_PAYMENT_METHOD CASCADE CONSTRAINTS;

CREATE TABLE VISIT_PAYMENT_METHOD (
    payment_method_id    Numeric(5) NOT NULL,
    payment_method_name  Varchar(50) NOT NULL
);

COMMENT ON COLUMN VISIT_PAYMENT_METHOD.payment_method_id IS
    'Identifier for payment method';

COMMENT ON COLUMN VISIT_PAYMENT_METHOD.payment_method_name IS
    'Payment method name';

ALTER TABLE VISIT_PAYMENT_METHOD ADD CONSTRAINT VISIT_PAYMENT_METHOD_pk PRIMARY KEY (payment_method_id);

ALTER TABLE VISIT_PAYMENT_METHOD ADD CONSTRAINT uq_VISIT_PAYMENT_METHOD UNIQUE (payment_method_name);

--Create the VISIT_PAYMENT table
DROP TABLE VISIT_PAYMENT CASCADE CONSTRAINTS;

CREATE TABLE VISIT_PAYMENT (
    payment_id              Numeric(5) NOT NULL,
    visit_id                Numeric(5) NOT NULL,
    payment_method_id       Numeric(5) NOT NULL,
    visit_payment_date      Date NOT NULL,
    visit_payment_amount    Numeric(5,2) NOT NULL
);

COMMENT ON COLUMN VISIT_PAYMENT.payment_id IS
    'Identifier for payment';

COMMENT ON COLUMN VISIT_PAYMENT.visit_id IS
    'Identifier for visit';

COMMENT ON COLUMN VISIT_PAYMENT.payment_method_id IS
    'Identifier for payment method';

COMMENT ON COLUMN VISIT_PAYMENT.visit_payment_date IS
    'Payment date';

COMMENT ON COLUMN VISIT_PAYMENT.visit_payment_amount IS
    'Payment amount';

ALTER TABLE VISIT_PAYMENT ADD CONSTRAINT visit_payment_pk PRIMARY KEY (payment_id);

ALTER TABLE VISIT_PAYMENT
    ADD CONSTRAINT visit_visit_payment_fk FOREIGN KEY (visit_id)
        REFERENCES visit (visit_id);

ALTER TABLE VISIT_PAYMENT
    ADD CONSTRAINT visit_payment_method_visit_payment_fk FOREIGN KEY (payment_method_id)
        REFERENCES visit_payment_method (payment_method_id);

-- Create a sequence for payment_method_id
DROP SEQUENCE payment_method_seq;
CREATE SEQUENCE payment_method_seq START WITH 4 INCREMENT BY 1;

-- Create a sequence for payment_id
DROP SEQUENCE payment_seq;
CREATE SEQUENCE payment_seq START WITH 1 INCREMENT BY 1;

-- Insert payment methods
INSERT INTO VISIT_PAYMENT_METHOD VALUES (
    1,
    'Card'
);

INSERT INTO VISIT_PAYMENT_METHOD VALUES (
    2,
    'Cash'
);

INSERT INTO VISIT_PAYMENT_METHOD VALUES (
    3,
    'Historical'
);

-- Insert payment record for completed visits
INSERT INTO VISIT_PAYMENT (
    SELECT
        payment_seq.NEXTVAL,
        visit_id,
        3,
        visit_date_time,
        visit_total_cost
    FROM
        visit
    WHERE
        VISIT_TOTAL_COST IS NOT NULL
);

commit;

DESC VISIT_PAYMENT_METHOD;
DESC VISIT_PAYMENT;

SELECT 
    * 
FROM 
    VISIT_PAYMENT_METHOD;

SELECT 
    * 
FROM 
    VISIT_PAYMENT;