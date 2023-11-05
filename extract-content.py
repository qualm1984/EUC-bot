import os
import requests
import time
from urllib.parse import urlparse, unquote

def fetch_html_from_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

def get_filename_from_url(url):
    path = unquote(urlparse(url).path)
    filename = os.path.basename(path)
    
    # If the filename is empty (e.g., URL ends with a slash), default to 'index'
    if not filename or filename == "/":
        filename = 'index'
    
    return filename + '.html'

def save_html_to_file(html_content, filename, folder_path):
    with open(os.path.join(folder_path, filename), 'w', encoding='utf-8') as file:
        file.write(html_content)

def main():
    urls_file_path = os.path.join('urls', 'controlup-docs.txt')  # Adapted path
    output_folder_path = 'data'  # Adapted path

    # Ensure output folder exists or create it
    os.makedirs(output_folder_path, exist_ok=True)

    # Read the URLs from the file
    with open(urls_file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines()]

    # Fetch and save HTML for each URL
    for url in urls:
        html_content = fetch_html_from_url(url)
        if html_content:
            filename = get_filename_from_url(url)
            save_html_to_file(html_content, filename, output_folder_path)
            print(f"Saved content from {url} to {filename}")
        else:
            print(f"Failed to fetch content from {url}")
        
        # Delay for 1 seconds before the next request
        time.sleep(1)

if __name__ == "__main__":
    main()
