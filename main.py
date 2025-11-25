import webbrowser
import time
import os
from core.selector import AreaSelector
from core.scroller import Scroller
from core.pdf_maker import save_to_pdf

def get_pdf_folder():
    folder_path = os.path.join(os.getcwd(), "pdfs")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def main():
    print("--- Scrolling Screenshot to PDF Maker ---")
    
    # 1. Get URL
    url = input("Enter the website URL: ").strip()
    if not url:
        print("Invalid URL. Exiting.")
        return

    if not url.startswith('http'):
        url = 'https://' + url

    # 2. Open Browser
    print(f"Opening {url}...")
    webbrowser.open(url)
    
    print("\nPlease wait for the page to load completely.")
    print("Prepare the page (close popups, etc.).")
    input("Press Enter when you are ready to select the area...")

    # 3. Select Area
    print("Launching selection tool...")
    print("Click and drag to select the area you want to capture.")
    print("Press ESC to cancel.")
    
    # Small delay to ensure browser is focused but selector comes on top
    time.sleep(1)
    
    selector = AreaSelector()
    region = selector.get_selection()
    
    if not region:
        print("No area selected. Exiting.")
        return
        
    print(f"Selected region: {region}")
    
    # 4. Start Scrolling and Capturing
    # SCROLL_AMOUNT: Negative scrolls down, Positive scrolls up.
    # -300 is a safer, smaller step to avoid skipping content.
    SCROLL_AMOUNT = -3000 
    
    scroller = Scroller(region, scroll_amount=SCROLL_AMOUNT, delay=1.0)
    images = scroller.start_scrolling()
    
    print(f"Captured {len(images)} screenshots.")
    
    # 5. Generate PDF
    if images:
        output_folder = get_pdf_folder()
        pdf_path = save_to_pdf(images, output_folder)
        
        if pdf_path:
            print(f"Done! PDF saved to: {pdf_path}")
            # Open the folder
            os.startfile(output_folder)
    else:
        print("No images captured.")

if __name__ == "__main__":
    main()
