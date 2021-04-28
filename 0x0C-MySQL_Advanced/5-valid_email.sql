-- creates a trigger that updates the valid email bool field
DELIMITER $$

CREATE TRIGGER valid
BEFORE UPDATE
ON users FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
    SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;
