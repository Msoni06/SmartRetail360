CREATE VIEW retail.v_sales_summary AS
SELECT
    d.year,
    d.month,
    SUM(f.payment_value) AS revenue,
    COUNT(DISTINCT f.order_id) AS orders
FROM retail.fact_sales f
JOIN retail.dim_date d
ON f.date_key = d.date_key
GROUP BY d.year, d.month;