-- This task want me to rank glam bands based on longevity
-- This query selects the feilds band name split and formed then calculates life span of glam bands
SELECT band_name AS band_name, ifnull(split, 2020)-formed AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
