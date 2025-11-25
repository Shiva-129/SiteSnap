# Scrolling Screenshot to PDF Maker

Hi there! 

This is a Python application designed to help you capture **long, scrollable content** (like articles, chat logs, or documentation) and save it as a clean, continuous PDF.

##  What does it do?

1.  **Opens a website** for you.
2.  Lets you **select exactly what you want to capture** using a simple drag-and-drop box.
3.  **Automatically scrolls** down the page, taking screenshots along the way.
4.  **Stitches everything together** into a high-quality PDF.
5.  **Saves it** right to a `pdfs` folder in this directory.

It even handles **super long pages** by intelligently splitting them so the PDF doesn't crash!

##  Getting Started

### Prerequisites
You'll need Python installed on your computer.

### Installation
1.  Open your terminal/command prompt in this folder.
2.  Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## How to Use

1.  Run the app:
    ```bash
    python main.py
    ```
2.  **Paste the URL** of the website you want to capture.
3.  Wait for the page to load, then press **Enter** in the terminal.
4.  **Draw a box** around the content you want to read.
5.  Sit back and watch it scroll! 
6.  It will stop automatically when it reaches the bottom.

> **Tip:** You can press `q` at any time to stop it manually.

## Customization

If it's scrolling too fast or too slow, you can tweak the `SCROLL_AMOUNT` in `main.py`:
- **`-300`**: Default. Good balance.
- **`-500`**: Faster scrolling.
- **`-200`**: Slower, more precise.

## Where are my PDFs?
Check the `pdfs` folder right here in the project directory.

