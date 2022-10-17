from sensor.configuration.mongo_db_connection import MongoDBClient

if __name__ == "__main__":
    print("Starting...")
    print("Connecting to MongoDB...")
    mongo_client = MongoDBClient()
    print("Collection name: ",mongo_client.database.list_collection_names())
    print("Connected to MongoDB!")