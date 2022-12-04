
SELECT

CASE cat
  WHEN 'A' THEN 1
  WHEN 'B' THEN 2
  ELSE 3
ENS AS type,

CASE
  WHEN cat IN ('A', 'B') THEN "high"
  WHEN price > 100 AND cat = 'C' THEN "med"
  ELSE "low"
END AS type,

SUM(CASE cat WHEN 'A' THEN amount END),

COUN(CASE WHEN amount > 10 THEN 1 END)

FROM t;
