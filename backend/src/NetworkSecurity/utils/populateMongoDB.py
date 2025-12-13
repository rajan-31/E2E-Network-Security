import pandas as pd
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

# Configuration variables - set your values here
DB_NAME = "PhishingData"
COLLECTION_NAME = "NetworkData"  # Set your collection name here

csv_file_path = "datafromDB.csv"  # Path to the CSV file to be pushed

def get_mongo_connection():
    """Establish connection to MongoDB"""
    client = MongoClient(MONGO_DB_URL)
    db = client[DB_NAME]
    return client, db

def push_csv_to_mongodb(csv_path: str, collection_name: str = COLLECTION_NAME):
    """
    Read CSV file and push data to MongoDB collection
    
    Args:
        csv_path: Path to the CSV file
        collection_name: Name of the MongoDB collection
    """
    # Read CSV file
    df = pd.read_csv(csv_path)
    
    # Convert DataFrame to list of dictionaries
    records = df.to_dict(orient='records')
    
    # Connect to MongoDB
    client, db = get_mongo_connection()
    
    try:
        collection = db[collection_name]
        
        # Clear existing data (optional - remove if you want to append)
        collection.delete_many({})
        
        # Insert records
        if records:
            result = collection.insert_many(records)
            print(f"Successfully inserted {len(result.inserted_ids)} records into '{collection_name}' collection")
        else:
            print("No records found in CSV file")
            
    except Exception as e:
        print(f"Error inserting data: {e}")
        raise
    finally:
        client.close()

def get_collection_names():
    """Get all collection names from the database"""
    client, db = get_mongo_connection()
    try:
        collections = db.list_collection_names()
        return collections
    finally:
        client.close()

def main():    
    if not os.path.exists(csv_file_path):
        print(f"Error: {csv_file_path} not found")
        return
    
    push_csv_to_mongodb(csv_file_path)
    print("Data migration completed successfully!")

if __name__ == "__main__":
    main()