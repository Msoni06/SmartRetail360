CREATE INDEX idx_customer
ON retail.fact_sales(customer_key);

CREATE INDEX idx_product
ON retail.fact_sales(product_key);

CREATE INDEX idx_seller
ON retail.fact_sales(seller_key);

CREATE INDEX idx_date
ON retail.fact_sales(date_key);

CREATE INDEX idx_region
ON retail.fact_sales(region_key);