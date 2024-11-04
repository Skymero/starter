# Testing git push

import subprocess
import sys
import os
from appwrite.client import Client
from appwrite.services.storage import Storage
from appwrite.exception import AppwriteException
from PIL import Image
import io
import tensorflow as tf
import matplotlib.pyplot as plt



def main(context):
    # Set up Appwrite client
    
    """
    Entry point for the Appwrite Cloud Function.

    This function is triggered by an Appwrite Storage file upload event.
    It fetches the uploaded image, shallow clones a repository containing image processing code,
    executes the code, and uploads the processed image to Appwrite Storage.

    The function expects the following environment variables:

    - `APPWRITE_API_KEY`: The Appwrite API key to use for authentication.
    - `REPO_URL`: The URL of the repository containing the image processing code.

    The function assumes the following:

    - The image processing code is in a module named `image_processor.py` with a function `process_image`.
    - The `process_image` function takes a PIL.Image object as input and returns a processed PIL.Image object.
    - The `process_image` function is idempotent and can be called multiple times with the same input.

    The function returns a JSON response with a single key-value pair: `processed_image_id`.
    The value is the ID of the processed image stored in Appwrite Storage.

    If any errors occur during the execution, the function returns an error response with a 500 status code.
    """
    client = Client()
    client.set_endpoint('https://cloud.appwrite.io/v1')
    client.set_project('670820a600112ca60a46')
    client.set_key('standard_facf1cac9eae9d31d3a8aaed5c96fa5c1e3ce463d69af4675d01653387ba5174c066df71d697753f1f948873faa7137a9a4ad0db9e7a66a3d66ac1aca95231962eba74fd6609e5ef2a0eb13ac9485e1d5c2234021685679c0d91f54669b2ea707b9be6e0b04f4ee847279636655880fd9d21fa47251cdc3a331dcac891b28506')  # Store this key as an environment variable

    storage = Storage(client)

    # Get the repository URL and other details from environment variables or context
    repo_url = os.environ.get('REPO_URL', 'https://github.com/Skymero/WoundSize.git')
    clone_dir = '/tmp/cloned_repo/WoundSize/WoundSize'  # A temporary location to clone the repo

    # Step 1: Shallow Clone the Repository
    try:
        if not os.path.exists(clone_dir):
            subprocess.run(["git", "clone", "--depth", "1", repo_url, clone_dir], check=True)
    except subprocess.CalledProcessError as e:
        context.error(f"Failed to clone repository: {repr(e)}")
        return context.res.text("Repository cloning failed", 500)

    # Step 2: Add the cloned repository to the Python path
    sys.path.insert(0, clone_dir)

    # Step 3: Fetch the file from Appwrite Storage
    file_id = context['req']['payload'].get('fileId')
    try:
        file_response = storage.get_file_download('670825a2000361d39c6e', file_id)
        image = Image.open(io.BytesIO(file_response))
        plt.imshow(image)
    except AppwriteException as err:
        context.error(f"Failed to fetch image from storage: {repr(err)}")
        return context.res.text("Failed to fetch image", 500)

    # Step 4: Execute Image Processing Code from the Cloned Repository
    try:
        # Assuming your cloned repo has a module named `image_processor.py` with a function `process_image`
        import wound_analysis as image_processor  # Dynamically importing the cloned module

        # Example: Call the image processing function from the cloned repo
        processed_image = image_processor.main(image)  # Replace with your actual function and logic

        # Save the processed image to an in-memory buffer
        buffer = io.BytesIO()
        processed_image.save(buffer, format="PNG")
        buffer.seek(0)

        # Upload the processed image to Appwrite Storage
        processed_file_response = storage.create_file(
            '670825a2000361d39c6e', 
            'unique()', 
            buffer, 
            content_type="image/PNG"
        )

        return context.res.json({
            "processed_image_id": processed_file_response['$id']
        })
    
    except Exception as err:
        context.error(f"Image processing failed: {repr(err)}")
        return context.res.text("Image processing failed", 500)
    
    finally:
        # Clean up the cloned repository directory if needed
        if os.path.exists(clone_dir):
            subprocess.run(["rm", "-rf", clone_dir])

