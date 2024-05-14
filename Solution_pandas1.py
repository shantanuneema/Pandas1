import pandas as pd

# Solution to Problem 1
def list_of_list_to_pandas(lst: list, col_names=['list1', 'list2']) -> pd.DataFrame:
    df = pd.DataFrame(lst, columns=col_names)
    return df

# Solution to Problem 2
def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = (world["population"] >= 25000000) | (world["area"]>=3000000)
    return world[df][["name", "population", "area"]]

# Solution to Problem 3
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    df = df[['product_id']]
    return df

# Solution to Problem 4
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers[~customers['id'].isin(orders['customerId'])]
    df = df[['name']].rename(columns ={'name': 'Customers'})
    return df
