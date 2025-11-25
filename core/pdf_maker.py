from PIL import Image
import os

def save_to_pdf(images, output_folder, filename="output.pdf"):
    if not images:
        print("No images to save.")
        return None

    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_path = os.path.join(output_folder, filename)
    
    # Convert all images to RGB (PDF doesn't support RGBA)
    rgb_images = []
    for img in images:
        if img.mode == 'RGBA':
            rgb_images.append(img.convert('RGB'))
        else:
            rgb_images.append(img)

    # Stitch images vertically, but respect max height limit
    # Pillow/PDF often has a limit around 65500 pixels. We'll use 60000 to be safe.
    MAX_HEIGHT = 60000
    
    pdf_pages = []
    current_batch = []
    current_height = 0
    
    widths = [i.size[0] for i in rgb_images]
    max_width = max(widths) if widths else 0

    for img in rgb_images:
        img_h = img.size[1]
        
        # If adding this image exceeds max height, process current batch
        if current_height + img_h > MAX_HEIGHT:
            # Create page from current batch
            page_img = Image.new('RGB', (max_width, current_height))
            y_offset = 0
            for batch_img in current_batch:
                page_img.paste(batch_img, (0, y_offset))
                y_offset += batch_img.size[1]
            pdf_pages.append(page_img)
            
            # Reset batch
            current_batch = [img]
            current_height = img_h
        else:
            current_batch.append(img)
            current_height += img_h

    # Process remaining batch
    if current_batch:
        page_img = Image.new('RGB', (max_width, current_height))
        y_offset = 0
        for batch_img in current_batch:
            page_img.paste(batch_img, (0, y_offset))
            y_offset += batch_img.size[1]
        pdf_pages.append(page_img)

    if not pdf_pages:
        return None

    try:
        pdf_pages[0].save(
            output_path,
            "PDF",
            resolution=100.0,
            save_all=True,
            append_images=pdf_pages[1:]
        )
        print(f"PDF saved successfully at: {output_path}")
        return output_path
    except Exception as e:
        print(f"Error saving PDF: {e}")
        return None
