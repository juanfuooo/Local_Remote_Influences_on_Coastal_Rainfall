import os
import time
import subprocess
import pyautogui
import pyperclip

def open_browser_with_url(url, browser_path=None):
    """Open browser with specified URL"""
    if browser_path:
        subprocess.Popen([browser_path, url])
    # else:
    #     # Try to use default browser
    #     import webbrowser
    #     webbrowser.open(url)
    
    # Give browser time to open
    time.sleep(1)

def process_urls_with_manual_automation(url_file_path, wait_time=1, max_urls=None):
    """
    Process URLs using PyAutoGUI for browser control
    
    Parameters:
    - url_file_path: Path to the text file containing URLs (one per line)
    - wait_time: Time to wait between URL visits (in seconds)
    - max_urls: Maximum number of URLs to process (None for all)
    """
    # Check if Edge browser path exists
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if not os.path.exists(edge_path):
        edge_path = None
        print("Edge browser not found at default location. Using default browser.")
    
    # Read URLs from file
    with open(url_file_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]
    
    # Limit number of URLs if specified
    if max_urls is not None:
        urls = urls[:max_urls]
    
    total_urls = len(urls)
    print(f"Starting to process {total_urls} URLs")
    
    # Process each URL
    for i, url in enumerate(urls):
        try:
            print(f"Processing URL {i+1}/{total_urls}")
            
            # Copy URL to clipboard for reliability
            pyperclip.copy(url)
            
            # Open browser with the URL
            open_browser_with_url(url, edge_path)
            
            # If you need to press specific keys or click on specific buttons, add PyAutoGUI
            # commands here. For example:
            
            # Wait for page to load
            time.sleep(wait_time)
            
            # Example: Press Enter to confirm a download
            # pyautogui.press('enter')
            
            # Example: Click on a download button at specific coordinates
            # pyautogui.click(x=800, y=500)
            
            # Wait for download to start
       
            
            # Close browser tab with Ctrl+W
            pyautogui.hotkey('ctrl', 'w')
            
            # Wait a bit before next URL
      
            
        except Exception as e:
            print(f"Error processing URL: {str(e)}")
    
    print("URL processing completed")

if __name__ == "__main__":
    # Configuration
    url_file_path = r"C:\Users\lv299\Downloads\subset_TRMM_3B42_Daily_7_20250311_042429_.txt"  # Path to your text file with URLs
    wait_time = 5  # Time to wait after page load
    max_urls = None  # Set to a number to limit URLs processed, or None for all
    
    # Run the automation
    process_urls_with_manual_automation(url_file_path, wait_time, max_urls)




