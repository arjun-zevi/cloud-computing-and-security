"""Thread-based image processing on Azure Blob Storage.
Every image in the container is downloaded, resized to 200x200 and uploaded
back as 'processed_<name>', one thread per image.
Set the connection string in the AZURE_STORAGE_CONNECTION_STRING env variable.
"""
import io
import os
import threading

from azure.storage.blob import BlobServiceClient
from PIL import Image

connection_string = os.environ.get("AZURE_STORAGE_CONNECTION_STRING", "YOUR_CONNECTION_STRING")
container_name = "images"
PREFIX = "processed_"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)


def process_image(blob_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    # Download image
    data = blob_client.download_blob().readall()
    stream = io.BytesIO(data)

    # Open and process image
    img = Image.open(stream).convert("RGB")   # RGB so PNGs can be saved as JPEG
    img = img.resize((200, 200))              # Resize

    # Save processed image
    output = io.BytesIO()
    img.save(output, format="JPEG")
    output.seek(0)

    # Upload processed image
    new_name = PREFIX + blob_name
    blob_service_client.get_blob_client(container=container_name, blob=new_name).upload_blob(output, overwrite=True)
    print(f"[{threading.current_thread().name}] processed {blob_name} -> {new_name}")


def main():
    container_client = blob_service_client.get_container_client(container_name)
    # list() first, and skip already-processed files, so the loop does not
    # pick up the files that this script uploads
    names = [b.name for b in container_client.list_blobs() if not b.name.startswith(PREFIX)]

    threads = []
    # Create threads
    for name in names:
        t = threading.Thread(target=process_image, args=(name,))
        threads.append(t)
        t.start()

    # Wait for completion
    for t in threads:
        t.join()

    print("All images processed successfully")


if __name__ == "__main__":
    main()
