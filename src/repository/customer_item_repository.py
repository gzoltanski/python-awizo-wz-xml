from db.database import Database
from src.model.customer_item import CustomerItem
from src.repository import *

def query_customer_item(db: Database, customer_name, buyer_item_code) -> CustomerItem:
    SQL_CUSTOMER_ITEM = f"""
        SELECT 
            pc.[name]
           ,ci.[item_no]
           ,ci.[buyer_item_code]
           ,ci.[drobimex_increment]
           ,ci.[customer_increment]
           ,ci.[customer_uom]
        FROM [ecoddb_tst].[dbo].[customer_item] as ci JOIN [ecoddb_tst].[dbo].[parent_customer] as pc 
        ON ci.[parent_customer_id] = pc.[id] 
        WHERE pc.[name] = {customer_name} and ci.[buyer_item_code] = {buyer_item_code}
    """

    customer_item_sql = SqlQuery(db, SQL_CUSTOMER_ITEM).execute()
    customer_item_list = []
    for customer_item in customer_item_sql:
        customer_item_list.append(CustomerItem(*customer_item))

    return customer_item_list