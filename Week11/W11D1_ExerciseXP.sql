-- Exercise 1
-- Task1


-- SELECT
--  m.medal_name, AVG(g.age) AS average_age
-- FROM olympics.games_competitor g
-- JOIN olympics.competitor_event c
--   ON g.id = c.competitor_id
-- JOIN olympics.medal m
--   ON c.medal_id = m.id
-- WHERE c.medal_id IN (1, 2, 3)
-- GROUP BY m.medal_name;

-- Task2

-- SELECT
--   noc.region_name
--  ,COUNT(DISTINCT c.competitor_id) AS competitor_count
-- FROM olympics.noc_region noc
-- JOIN olympics.person_region p
--   ON noc.id = p.region_id
-- JOIN olympics.person per
--   ON p.person_id = per.id
-- JOIN olympics.games_competitor g
--   ON per.id = g.person_id
-- JOIN olympics.competitor_event c
--   ON g.id = c.competitor_id
-- WHERE c.event_id > 3
-- GROUP BY noc.region_name
-- ORDER BY competitor_count DESC
-- LIMIT 5;

-- Task3

-- CREATE TEMP TABLE TempMedals AS
-- SELECT
--   gc.person_id
--  ,p.full_name
--  ,COUNT(ce.medal_id) AS total_medals
-- FROM olympics.games_competitor gc
-- JOIN olympics.person p
--   ON gc.person_id = p.id
-- JOIN olympics.competitor_event ce
--   ON gc.id = ce.competitor_id
-- GROUP BY gc.person_id
--         ,p.full_name;
-- SELECT * FROM TempMedals;
-- WHERE total_medals > 2;

-- Task4

-- CREATE TEMP TABLE CompetitorAnalysis AS
-- SELECT
--     gc.person_id,
--     p.full_name,
--     gc.games_id,
--     ce.event_id,
--     ce.medal_id
-- FROM
--     olympics.games_competitor gc
-- JOIN
--     olympics.person p ON gc.person_id = p.id
-- JOIN
--     olympics.competitor_event ce ON gc.id = ce.competitor_id;

-- DELETE FROM CompetitorAnalysis
-- WHERE person_id IN (
--     SELECT person_id
--     FROM CompetitorAnalysis
--     GROUP BY person_id
--     HAVING COUNT(CASE WHEN medal_id IN (1, 2, 3) THEN 1 END) = 0
-- );

-- Exercise 2
-- Task1

-- CREATE TEMP TABLE RegionAverageHeight AS
-- SELECT
--     pr.region_id,
--     AVG(p.height) AS avg_height
-- FROM
--     olympics.person p
-- JOIN
--     olympics.person_region pr ON p.id = pr.person_id
-- GROUP BY
--     pr.region_id;

-- SELECT * FROM RegionAverageHeight

-- WITH AvgHeightCTE AS (
--     SELECT
--         p.id AS person_id,
--         rah.avg_height
--     FROM
--         olympics.person p
--     JOIN
--         olympics.person_region pr ON p.id = pr.person_id
--     JOIN
--         RegionAverageHeight rah ON pr.region_id = rah.region_id
--     WHERE
--         p.height = 0
-- )
-- UPDATE olympics.person
-- SET height = AvgHeightCTE.avg_height
-- FROM AvgHeightCTE
-- WHERE olympics.person.id = AvgHeightCTE.person_id;

-- Task2

-- CREATE TEMP TABLE MultipleParticipation AS
-- SELECT
--     p.full_name,
--     COUNT(c.event_id) AS  total_events
-- FROM
--     olympics.person p
-- JOIN
--     olympics.competitor_event c ON p.id = c.competitor_id
-- GROUP BY
--     p.full_name, c.event_id;

-- SELECT * FROM MultipleParticipation
-- WHERE total_events > 1

-- Task3

-- CREATE TEMP TABLE CompetitorMedals AS
-- SELECT
--     competitor_id,
--     COUNT(*) AS total_medals
-- FROM
--     olympics.competitor_event
-- WHERE
--     medal_id IN (1, 2, 3)
-- GROUP BY
--     competitor_id;

-- CREATE TEMP TABLE RegionAverageMedals AS
-- SELECT
--     pr.region_id,
--     AVG(cm.total_medals) AS avg_medals_per_competitor
-- FROM
--     CompetitorMedals cm
-- JOIN
--     olympics.person_region pr ON cm.competitor_id = pr.person_id
-- GROUP BY
--     pr.region_id;

-- SELECT
--     AVG(total_medals) AS overall_avg_medals_per_competitor
-- INTO TEMP TABLE OverallAverageMedals
-- FROM
--     CompetitorMedals;

-- SELECT
--     nr.region_name,
--     ram.avg_medals_per_competitor
-- FROM
--     RegionAverageMedals ram
-- JOIN
--     olympics.noc_region nr ON ram.region_id = nr.id
-- WHERE
--     ram.avg_medals_per_competitor > (SELECT overall_avg_medals_per_competitor FROM OverallAverageMedals);

-- Task4

-- CREATE TEMP TABLE CompetitorSeasons AS
-- SELECT
--     gc.person_id,
--     g.season
-- FROM
--     olympics.games_competitor gc
-- JOIN
--     olympics.games g ON gc.games_id = g.id
-- GROUP BY
--     gc.person_id, g.season;

-- CREATE TEMP TABLE BothSeasonsCompetitors AS
-- SELECT
--     cs.person_id
-- FROM
--     CompetitorSeasons cs
-- GROUP BY
--     cs.person_id
-- HAVING
--     COUNT(DISTINCT cs.season) = 2;

-- SELECT
--     p.full_name,
--     p.id
-- FROM
--     olympics.person p
-- JOIN
--     BothSeasonsCompetitors bsc ON p.id = bsc.person_id;
