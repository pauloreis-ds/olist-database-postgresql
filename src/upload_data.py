import pandas as pd


def upload_csv(db):

    # Python's default None wouldn't work, then I put these 1s
    olist_orders_dataset = pd.read_csv("./data/olist_orders_dataset.csv").fillna("1111-11-11 11:11:11")
    for row in range(len(olist_orders_dataset)):
        order_id = olist_orders_dataset.loc[row].values[0]
        customer_id = olist_orders_dataset.loc[row].values[1]
        order_status = olist_orders_dataset.loc[row].values[2]
        order_purchase_timestamp = olist_orders_dataset.loc[row].values[3]
        order_approved_at = olist_orders_dataset.loc[row].values[4]
        order_delivered_carrier_date = olist_orders_dataset.loc[row].values[5]
        order_delivered_customer_date = olist_orders_dataset.loc[row].values[6]
        order_estimated_delivery_date = olist_orders_dataset.loc[row].values[7]

        insert = f'''INSERT INTO orders (order_id, customer_id, order_status, order_purchase_timestamp,
                     order_approved_at, order_delivered_carrier_date, order_delivered_customer_date,
                     order_estimated_delivery_date)
                    VALUES('{order_id}', '{customer_id}', '{order_status}', '{order_purchase_timestamp}',
                    '{order_approved_at}', '{order_delivered_carrier_date}', '{order_delivered_customer_date}',
                    '{order_estimated_delivery_date}');'''
        db.cursor.execute(insert)
    print(f"orders uploaded.")

    db.cursor.execute(
        """UPDATE orders SET order_estimated_delivery_date = NULL WHERE order_estimated_delivery_date = timestamp '1111-11-11 11:11:11'""")
    db.cursor.execute(
        """UPDATE orders SET order_approved_at = NULL WHERE order_approved_at = timestamp '1111-11-11 11:11:11'""")
    db.cursor.execute(
        """UPDATE orders SET order_delivered_carrier_date = NULL WHERE order_delivered_carrier_date = timestamp '1111-11-11 11:11:11'""")
    db.cursor.execute(
        """UPDATE orders SET order_delivered_customer_date = NULL WHERE order_delivered_customer_date = timestamp '1111-11-11 11:11:11'""")
    db.cursor.execute(
        """UPDATE orders SET order_purchase_timestamp = NULL WHERE order_purchase_timestamp = timestamp '1111-11-11 11:11:11'""")

    olist_order_reviews_dataset = pd.read_csv("./data/olist_order_reviews_dataset.csv")
    for row in range(len(olist_order_reviews_dataset)):
        review_id = olist_order_reviews_dataset.loc[row].values[0]
        order_id = olist_order_reviews_dataset.loc[row].values[1]
        review_score = olist_order_reviews_dataset.loc[row].values[2].item()
        review_comment_title = olist_order_reviews_dataset.loc[row].values[3]
        review_comment_message = olist_order_reviews_dataset.loc[row].values[4]
        review_creation_date = olist_order_reviews_dataset.loc[row].values[5]
        review_answer_timestamp = olist_order_reviews_dataset.loc[row].values[6]

        insert = f'''INSERT INTO order_reviews (review_id, order_id, review_score, review_comment_title,
                     review_comment_message, review_creation_date, review_answer_timestamp)
                    VALUES(%s, %s, %s, %s, %s, %s, %s);'''
        db.cursor.execute(insert, (review_id, order_id, review_score, review_comment_title, review_comment_message,
                                   review_creation_date, review_answer_timestamp))
    print(f"order_reviews uploaded.")

    olist_order_payments_dataset = pd.read_csv("./data/olist_order_payments_dataset.csv")
    for row in range(len(olist_order_payments_dataset)):
        order_id = olist_order_payments_dataset.loc[row].values[0]
        payment_sequential = olist_order_payments_dataset.loc[row].values[1].item()
        payment_type = olist_order_payments_dataset.loc[row].values[2]
        payment_installments = olist_order_payments_dataset.loc[row].values[3].item()
        payment_value = olist_order_payments_dataset.loc[row].values[4].item()

        insert = f'''INSERT INTO order_payments (order_id, payment_sequential, payment_type,
                     payment_installments, payment_value)
                    VALUES(%s, %s, %s, %s, %s);'''
        db.cursor.execute(insert, (order_id, payment_sequential, payment_type,
                                   payment_installments, payment_value))
    print(f"order_payments uploaded.")

    olist_geolocation_dataset = pd.read_csv("./data/olist_geolocation_dataset.csv")
    for row in range(len(olist_geolocation_dataset)):
        geolocation_zip_code_prefix = olist_geolocation_dataset.loc[row].values[0].item()
        geolocation_lat = olist_geolocation_dataset.loc[row].values[1].item()
        geolocation_lng = olist_geolocation_dataset.loc[row].values[2].item()
        geolocation_city = olist_geolocation_dataset.loc[row].values[3]
        geolocation_state = olist_geolocation_dataset.loc[row].values[4]

        insert = f'''INSERT INTO geolocation (geolocation_zip_code_prefix, geolocation_lat, geolocation_lng,
                     geolocation_city, geolocation_state)
                    VALUES(%s, %s, %s, %s, %s);'''
        db.cursor.execute(insert, (geolocation_zip_code_prefix, geolocation_lat, geolocation_lng,
                                   geolocation_city, geolocation_state))
    print(f"geolocation uploaded.")

    olist_customers_dataset = pd.read_csv("./data/olist_customers_dataset.csv")
    for row in range(len(olist_customers_dataset)):
        customer_id = olist_customers_dataset.loc[row].values[0]
        customer_unique_id = olist_customers_dataset.loc[row].values[1]
        customer_zip_code_prefix = olist_customers_dataset.loc[row].values[2].item()
        customer_city = olist_customers_dataset.loc[row].values[3]
        customer_state = olist_customers_dataset.loc[row].values[4]

        insert = f'''INSERT INTO customers (customer_id, customer_unique_id, customer_zip_code_prefix,
                     customer_city, customer_state)
                    VALUES(%s, %s, %s, %s, %s);'''
        db.cursor.execute(insert, (customer_id, customer_unique_id, customer_zip_code_prefix,
                                   customer_city, customer_state))
    print(f"customers uploaded.")

    add_orders_FK = "ALTER TABLE orders ADD CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES customers(customer_id);"
    db.cursor.execute(add_orders_FK)

    olist_products_dataset = pd.read_csv("./data/olist_products_dataset.csv")
    for row in range(len(olist_products_dataset)):
        product_id = olist_products_dataset.loc[row].values[0]
        product_category_name = olist_products_dataset.loc[row].values[1]
        product_name_lenght = olist_products_dataset.loc[row].values[2].item()
        product_description_lenght = olist_products_dataset.loc[row].values[3].item()
        product_photos_qty = olist_products_dataset.loc[row].values[4].item()
        product_weight_g = olist_products_dataset.loc[row].values[5].item()
        product_length_cm = olist_products_dataset.loc[row].values[6].item()
        product_height_cm = olist_products_dataset.loc[row].values[7].item()
        product_width_cm = olist_products_dataset.loc[row].values[8].item()

        insert = f'''INSERT INTO products (product_id, product_category_name, product_name_lenght,
                     product_description_lenght, product_photos_qty, product_weight_g,
                     product_length_cm, product_height_cm, product_width_cm)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);'''
        db.cursor.execute(insert, (product_id, product_category_name, product_name_lenght,
                                   product_description_lenght, product_photos_qty, product_weight_g,
                                   product_length_cm, product_height_cm, product_width_cm))
    print(f"products uploaded.")

    olist_sellers_dataset = pd.read_csv("./data/olist_sellers_dataset.csv")
    for row in range(len(olist_sellers_dataset)):
        seller_id = olist_sellers_dataset.loc[row].values[0]
        seller_zip_code_prefix = olist_sellers_dataset.loc[row].values[1].item()
        seller_city = olist_sellers_dataset.loc[row].values[2]
        seller_state = olist_sellers_dataset.loc[row].values[3]

        insert = f'''INSERT INTO sellers (seller_id, seller_zip_code_prefix, seller_city, seller_state)
                    VALUES(%s, %s, %s, %s);'''
        db.cursor.execute(insert, (seller_id, seller_zip_code_prefix, seller_city, seller_state))
    print(f"sellers uploaded.")

    olist_order_items_dataset = pd.read_csv("./data/olist_order_items_dataset.csv")
    for row in range(len(olist_order_items_dataset)):
        order_id = olist_order_items_dataset.loc[row].values[0]
        order_item_id = olist_order_items_dataset.loc[row].values[1].item()
        product_id = olist_order_items_dataset.loc[row].values[2]
        seller_id = olist_order_items_dataset.loc[row].values[3]
        shipping_limit_date = olist_order_items_dataset.loc[row].values[4]
        price = olist_order_items_dataset.loc[row].values[5].item()
        freight_value = olist_order_items_dataset.loc[row].values[6].item()

        insert = f'''INSERT INTO order_items (order_id, order_item_id, product_id, seller_id, shipping_limit_date,
                    price, freight_value)
                    VALUES(%s, %s, %s, %s, %s, %s, %s);'''
        db.cursor.execute(insert, (order_id, order_item_id, product_id, seller_id, shipping_limit_date,
                                   price, freight_value))
    print(f"order_items uploaded.")
    print("All files were uploaded.")