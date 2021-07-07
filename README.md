## Usage

You need to install and configure PostgreSQL in your computer. This [tutorial](https://www.youtube.com/watch?v=BLH3s5eTL4Y) may help you.

- Download the [Olist data](https://www.kaggle.com/olistbr/brazilian-ecommerce?select=olist_orders_dataset.csv) from kaggle.
- Pull this repository to your computer.
- Create a file called "data" in the main directory and unzip the Olist file there.

Remember to set the connection according to your own PostgreSQL settings in main.py.

```python
user = User(host="localhost", name="postgres", password="********", database="postgres")
```

Uncomment these and run it. 

```python
# src.database_schema.make_schema(db)
# src.upload_data.upload_csv(db)
```


[<img align="right" width="60" height="60" src="https://github.com/pauloreis-ds/Paulo-Reis-Data-Science/blob/master/Paulo%20Reis/Pauloreis01.png">](https://github.com/pauloreis-ds)

---
