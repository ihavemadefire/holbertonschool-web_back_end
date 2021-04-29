-- Creates index on name and score
-- More indexing
CREATE INDEX idx_name_first ON names(name(1), score);