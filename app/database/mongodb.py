import os
from dotenv import load_dotenv
import pymongo
import json
from pathlib import Path

load_dotenv()

_client = None

def connect():
    """Initializes and returns a singleton MongoClient instance."""
    global _client
    if _client is None:
        mongo_uri = os.getenv("MONGO_CONNECTION")
        _client = pymongo.MongoClient(mongo_uri)
    return _client

def get_database(db_name: str = "Shopping_agent"):
    """Returns a database instance."""
    client = connect()
    return client[db_name]

def get_collection(collection_name: str, db_name: str = "Shopping_agent"):
    """Returns a collection instance."""
    db = get_database(db_name)
    return db[collection_name]

def seed_products():
    """Loads products from data/products.json and inserts them into MongoDB."""
    products_col = get_collection("products")
    
    # Path to data/products.json
    base_dir = Path(__file__).resolve().parent.parent.parent
    json_path = base_dir / "data" / "products.json"
    
    with open(json_path, "r", encoding="utf-8") as f:
        products_data = json.load(f)
        
    products_col.delete_many({})  # Clear existing products
    result = products_col.insert_many(products_data)
    print(f"Seeded {len(result.inserted_ids)} products into MongoDB.")

def search_prodouct(product_name):
    """Testing for search product using there id """
    db = _client['Shopping_agent']
    collection = db['products']
    result = collection.find_one(
        {"name": product_name}
    )
    print(result)


if __name__ == "__main__":
    connect()
    search_prodouct('PulseBuds ANC')
    
