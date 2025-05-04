import os
import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Download function
def download_file(url):
    try:
        local_filename = os.path.join(DOWNLOAD_FOLDER, url.split("/")[-1])
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        return f"Downloaded: {url}"
    except Exception as e:
        return f"Failed: {url} -> {e}"

# sequential download
def download_sequential(urls):
    print("\nStarting sequential download...")
    start = time.time()
    for url in urls:
        print(download_file(url))
    print(f"Sequential download time: {time.time() - start:.2f} seconds")

def download_concurrent(urls, max_workers=5):
    print("\nStarting concurrent download with ThreadPoolExecutor...")
    start = time.time()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(download_file, url): url for url in urls}
        for future in as_completed(futures):
            print(future.result())
    print(f"Concurrent download time: {time.time() - start:.2f} seconds")

# Main
def main():

    url1 = input("Enter space-separated URLs:\n").strip().split()
    url2 = input("Enter space-separated URLs:\n").strip().split()

    download_sequential(url1)
    download_sequential(url2)
    download_concurrent(url1)
    download_concurrent(url2)

if __name__ == "__main__":
    main()
