# Program 7: Thread-based image processing application in Microsoft Azure


## Aim
To implement a thread-based image processing application using Azure Blob Storage.

## Prerequisites
- Azure account, Python 3.8+
- `pip install -r requirements.txt` (azure-storage-blob, pillow)

## Repository contents
```
07-azure-image-processing/
├── .gitignore
├── README.md
├── code.txt
├── output/output_screenshot.png
├── requirements.txt
├── src/app.py
├── src/local_demo.py
```
`code.txt` contains every program/command used, in one plain-text file.

## Procedure
1. Azure Portal > **Storage accounts > Create** (new resource group, name e.g. `imagestorage123`, nearest region).
2. Open the account > **Containers > + Container**: name `images`, access level *Private*.
3. **Upload** several sample images to the container.
4. **Access keys** > copy the **Connection string**.
5. Install libraries: `pip install -r requirements.txt`
6. Set the connection string and run:
   - Linux/macOS: `export AZURE_STORAGE_CONNECTION_STRING="..."`
   - Windows: `setx AZURE_STORAGE_CONNECTION_STRING "..."`
   - `python src/app.py`
7. Verify in the portal that `processed_<name>.jpg` blobs were created.
8. (No Azure account?) test the logic locally: `python src/local_demo.py`.

## Expected output
Each image is resized to 200x200 by its own thread, then `All images processed successfully` is printed.


## Result
Images were processed concurrently using threads and stored back in Azure Blob Storage.


