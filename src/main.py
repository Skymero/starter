import subprocess
import sys
import os
from appwrite.client import Client
from appwrite.services.storage import Storage
from appwrite.exception import AppwriteException
from PIL import Image
import io

def main(context):
    # Set up Appwrite client
    client = Client()
    client.set_endpoint(os.environ['https://cloud.appwrite.io/v1'])
    client.set_project(os.environ['670820a600112ca60a46'])
    client.set_key(os.environ['APPWRITE_API_KEY'])  # Store this key as an environment variable

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
    file_id = context.req['payload'].get('fileId')
    try:
        file_response = storage.get_file_download('bucket-id', file_id)
        image = Image.open(io.BytesIO(file_response))
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

