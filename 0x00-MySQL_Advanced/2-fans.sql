-- script that ranks country origins of bands
-- ordered by the number of (non-unique) fans

-- CREATE TEMPORARY TABLE IF NOT EXISTS temp AS
-- SELECT origin, SUM(fans) AS total_fans
-- FROM metal_bands
-- GROUP BY origin;

-- SELECT origin, total_fans AS nb_fans
-- FROM temp
-- ORDER BY total_fans DESC;

SELECT
    origin,
    SUM(fans) AS nb_fans
FROM
    metal_bands
GROUP BY
    origin
ORDER BY
    nb_fans DESC;
