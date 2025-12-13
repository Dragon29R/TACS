import json
import os
from jinja2 import Environment, FileSystemLoader

def generate_all_pages():
    # 1. Load DSML Data
    try:
        with open('../../DSML_model.json', 'r', encoding='utf-8') as f:
            dsml_data = json.load(f)
    except FileNotFoundError:
        print("Error: DSML_model.json not found.")
        return

    # 2. Define list of templates to render
    pages = [
        'login.html',
        'home.html',
        'profile.html',
        'auction.html',
        'listing_details.html',
        'create_listing.html',
        'chat.html',
        'menus.html'
    ]

    # 3. Setup Jinja2
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)

    # 4. Loop and Render
    for page_name in pages:
        try:
            template = env.get_template(f"{page_name}")
            output = template.render(dsml=dsml_data)
            
            # Save output (e.g., render login.html -> output_login.html)
            output_filename = f"../out/{page_name}"
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(output)
            
            print(f"Generated: {output_filename}")
            
        except Exception as e:
            print(f"Failed to generate {page_name}: {e}")

if __name__ == "__main__":
    generate_all_pages()