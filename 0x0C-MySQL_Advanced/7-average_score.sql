-- This calculates the grade average
-- Then adds the average 
DELIMITER ??
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id int)
BEGIN
    UPDATE users 
    SET average_score = (SELECT AVG(score) FROM corrections as bounce WHERE bounce.user_id=user_id)
    WHERE id = user_id;
END??
DELIMITER ;
