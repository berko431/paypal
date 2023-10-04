from flask import Flask, jsonify
import requests
from isbntools.app import meta, to_isbn13, cover

app = Flask(__name__)

SERVER_NAME = "Server A" 

@app.route('/')
def home():
    return f"Greetings! You are currently processed on {SERVER_NAME}"

@app.route('/book/<string:isbn>')
def book_metadata(isbn):
    try:
        isbn13 = to_isbn13(isbn) 
        if not isbn13:
            raise ValueError("Invalid ISBN provided.") # Raise exception of invalid ISBN
        
        info = meta(isbn13) 
        
        if not info:
            raise ValueError("No metadata found for this ISBN.") # Raise exception of valid ISBN with no metadata
            
        return jsonify(info)
    except Exception as e: # Any other exception
        return jsonify({"error": str(e)})

@app.route('/cover_image/<string:isbn>')
def get_cover(isbn):
    try:
        cover_data = cover(isbn)
        
        # Extract the URL for the thumbnail
        url = cover_data.get('thumbnail') if cover_data else None # URL of the thumbnail
        
        if not url:
            return "Cover image not found", 404
        
        response = requests.get(url, stream=True)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
        
        content_type = response.headers.get('content-type', 'application/octet-stream')
        
        return response.content, 200, {'Content-Type': content_type}

    except requests.RequestException as e: # Any other exception
        return f"Error fetching cover image: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=8000)


