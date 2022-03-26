import os
from dotenv import load_dotenv

load_dotenv()

azure_subscription_key = os.getenv('azure_subscription_key')
azure_blob_connection_string = DefaultEndpointsProtocol = os.getenv('azure_blob_connection_string')
face_api_url = os.getenv('face_api_url')