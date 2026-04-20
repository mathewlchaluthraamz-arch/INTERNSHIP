import pandas as pd

data = [
    [2001, "C101", "2023-08-01 18:00", "2023-08-01 18:45", 500, "upi", "Dominos", 4],
    [2002, "C102", "2023-08-01 19:00", "2023-08-01 18:50", 700, "Credit card", "KFC", 5],
    [2003, "C103", "2023-08-02 20:00", None, None, "Debit Card", "McDonalds", 3],
    [2004, "C104", "invalid", "2023-08-03 21:00", 800, "UPI", "Dominos", 6],
    [2005, "C105", "2023-08-04 18:30", "2023-08-04 19:00", -200, "Cash", "KFC", 2],
    [2005, "C105", "2023-08-04 18:30", "2023-08-04 19:00", -200, "Cash", "KFC", 2],
    [2006, "C106", "2023-08-05 17:00", "2023-08-05 17:40", 1200, None, "Pizza Hut", 4]
]

columns = ["order_id", "customer_id", "order_time", "delivery_time",
           "order_value", "payment_method", "restaurant", "rating"]

df = pd.DataFrame(data, columns=columns)
df.to_csv("orders.csv", index=False)