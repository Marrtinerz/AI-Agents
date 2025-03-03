import uuid
import io
import re
import os




def sanitize_filename(filename):
    """Sanitizes a filename by removing or replacing unsafe characters."""
    name, ext = os.path.splitext(filename)  # Split into name and extension
    name = re.sub(r'[^a-zA-Z0-9_.-]', '_', name)  # Replace unsafe characters with underscores
    filename = f"{name}{ext}"  # Recombine name and extension
    return filename

def generate_unique_filename(filename):
    """Generates a unique filename using a UUID."""
    name, ext = os.path.splitext(filename)
    unique_id = str(uuid.uuid4())
    return f"{unique_id}{ext}"  # Use UUID as the filename