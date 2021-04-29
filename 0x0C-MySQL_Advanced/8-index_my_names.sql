-- This creates an index on a huge table
-- The table is yuge, I tells ya!

CREATE INDEX idx_name_first ON names(name(1));