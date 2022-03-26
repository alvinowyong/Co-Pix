import os, uuid
import emotion
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__, ContentSettings
from load import azure_blob_connection_string

def emotion_recognition():
    connect_str = 'DefaultEndpointsProtocol=https;AccountName=cs460;AccountKey=Be6zSGwaZlK3dORLVr+NIifPl7PEzzoUXiiKlLK/D68Ih1+mF/p1j6FibFaABKfTSgiz3x0LuhBpUJFDrvgcLQ==;EndpointSuffix=core.windows.net'

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create a unique name for the container
    container_name = 'cs460blob'

    # Create a local directory to hold blob data
    local_path = "data/"
    # Create a file in the local data directory to upload and download
    local_file_name = 'image.jpg'

    upload_file_path = os.path.join(local_path, local_file_name)
    # upload_file_path = local_path + local_file_name

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    # Upload the created file
    with open(upload_file_path, "rb") as data:
        my_content_settings = ContentSettings(content_type='image/jpg')
        blob_client.upload_blob(data, overwrite=True, content_settings=my_content_settings)
        url = blob_client.url

    result = emotion.get_emotion(url)

    blob_client.delete_blob()
    
    return result
