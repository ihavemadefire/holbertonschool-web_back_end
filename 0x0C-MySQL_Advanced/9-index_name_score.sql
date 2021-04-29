-- Creates index on name and score
-- More indexing for fun and profit
CREATE INDEX idx_name_first_score ON names(name(1), score);
