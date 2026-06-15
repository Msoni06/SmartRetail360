CREATE TABLE retail.fact_sales (
    sales_key BIGSERIAL PRIMARY KEY,

    order_id VARCHAR(50),

    customer_key INT,
    product_key INT,
    seller_key INT,
    date_key INT,
    region_key INT,

    price NUMERIC(12,2),
    freight_value NUMERIC(12,2),
    payment_value NUMERIC(12,2),

    review_score INT,

    FOREIGN KEY (customer_key)
        REFERENCES retail.dim_customer(customer_key),

    FOREIGN KEY (product_key)
        REFERENCES retail.dim_product(product_key),

    FOREIGN KEY (seller_key)
        REFERENCES retail.dim_seller(seller_key),

    FOREIGN KEY (date_key)
        REFERENCES retail.dim_date(date_key),

    FOREIGN KEY (region_key)
        REFERENCES retail.dim_region(region_key)
);