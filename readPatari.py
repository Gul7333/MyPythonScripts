import json

def process_large_json_file(file_path):
    with open(file_path, 'r') as f:
        chunk_size = 1024 * 1024  # 1MB chunk size (adjust as needed)
        buffer = ""  # Initialize an empty buffer
        in_array = False  # Flag to track whether we are inside the root array
        for chunk in iter(lambda: f.read(chunk_size), ""):  # Read chunks until EOF
            buffer += chunk  # Add the chunk to the buffer
            while True:
                # Find the beginning and end of the next JSON object in the buffer
                start_index = buffer.find('{')
                end_index = buffer.find('}', start_index)
                if start_index != -1 and end_index != -1:  # If both start and end indices are found
                    json_str = buffer[start_index:end_index + 1]  # Extract the JSON object
                    try:
                        data = json.loads(json_str)  # Parse the JSON object
                        print(data)
                        # Process the JSON object here
                    except json.JSONDecodeError:
                        # Handle incomplete JSON object
                        pass
                    buffer = buffer[end_index + 1:]  # Remove the processed JSON object from the buffer
                else:
                    break  # No complete JSON object found in the buffer

# Usage
process_large_json_file('/sdcard/Telegram/patari.json')




















