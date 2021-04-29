-- This is the bonus round WOOOOOOOAH
-- This proceedure first adds the project if it diesn't exist in the table
-- Then adds the new correction
DELIMITER ??
CREATE PROCEDURE AddBonus (user_id int, project_name varchar(255), score float)
BEGIN
    INSERT INTO projects (name) SELECT project_name FROM DUAL
    WHERE project_name NOT IN (SELECT name FROM projects);

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END??
DELIMITER ;
