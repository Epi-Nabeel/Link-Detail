import requests
from urllib.parse import urljoin

def display_title():
    """
    Display the title screen with ASCII art and tool information.
    """
    title = """
L      III   N   N   K  K         DDD    EEEE   TTTTTT    AA    III   L    
L       I    NN  N   K K          D  D   E        TT     A  A    I    L    
L       I    N N N   KK     ===   D  D   EEE      TT     AAAA    I    L    
L       I    N  NN   K K          D  D   E        TT     A  A    I    L    
LLLL   III   N   N   K  K         DDD    EEEE     TT     A  A   III   LLLL 
                                                                  
    """
    details = """
Version: 1.0
Created by: Epi-Nabeel
https://github.com/Epi-Nabeel
"""
    print(title)
    print(details)


def trace_redirects(url):
    """
    Traces the redirect chain of a URL and prints the details.
    Args:
        url (str): The initial URL to trace.
    """
    try:
        print(f"\nTracing redirects for: {url}\n")
        response = requests.get(url, allow_redirects=True)
        if not response.history:
            print(f"No redirects. Final URL: {response.url}")
            return
        
        # Display the redirect chain
        for i, resp in enumerate(response.history, start=1):
            print(f"Redirect {i}:")
            print(f"  Status Code: {resp.status_code}")
            print(f"  From: {resp.url}")
            print(f"  To: {urljoin(resp.url, resp.headers['Location'])}\n")
        
        # Display the final destination
        print(f"Final URL (Status Code {response.status_code}): {response.url}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Display the title screen first
    display_title()
    
    # Prompt the user to input a URL
    url = input("Enter the URL to trace (e.g., http://example.com): ").strip()
    
    if url:
        trace_redirects(url)
    else:
        print("No URL entered. Please run the script again and provide a valid URL.")
