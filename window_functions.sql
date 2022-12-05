SELECT
	LAG(price, 1) OVER(ORDER BY timestamp) AS "previous price",
	AVG(price) OVER(ORDER BY timestamp
					ROWS BETWEEN 2 PRECEDING
					AND 0 FOLLOWING)  -- AND CURRENT ROW
					AS "3-day rolling average",
	MAX(price) OVER(PARTITION BY month)
					AS "peak price of the month",
	RANK() OVER(PARTITION BY month
				ORDER BY timestamp)
				AS "price rank of the month"
FROM stock_price;



/*----------------------------------------------------------------*/



SELECT
	SUM(quantity) OVER(PARTITION BY customer_id) AS "total quantity per customer",
	row_number() OVER(PARTITION BY customer_id
					  ORDER BY timestamp)
					  AS "order number per customer"
FROM orders;
