import json
import os
import re

# 1. Map GUI Component Types to HTML Tags
# We use regex to match types like "BidButton (Button)" -> <button>
TAG_MAPPING = {
    "Button": "button",
    "InputField": "input",
    "Label": "h3",
    "Image": "img",
    "ViewContainer": "div",
    "Menu": "nav",
    "Screen": "div"
}

def get_block_type_and_class(full_type_str):
    """
    Parses 'BidButton (Button)' into ('BidButton', 'Button')
    """
    match = re.search(r'(\w+)\s*\((\w+)\)', full_type_str)
    if match:
        return match.group(1), match.group(2)
    return full_type_str, "div" # Default

def generate_html_from_gui(gui_file='gui_model.json'):
    
    # Load GUI Model
    with open(gui_file, 'r') as f:
        data = json.load(f)

    # Navigate to the Main Module in the JSON tree
    # Path: blocks -> block[0] -> inputs -> MODULE -> block -> inputs
    try:
        main_block = data['blocks']['blocks'][0]
        module_block = main_block['inputs']['MODULE (MODULE)']['block']
        screens = module_block['inputs']
    except KeyError as e:
        print(f"Error parsing JSON structure: {e}")
        return

    # Ensure templates directory exists
    if not os.path.exists('templates'):
        os.makedirs('templates')

    # Iterate through every Screen found in gui_model.json
    for screen_key, screen_data in screens.items():
        
        screen_block = screen_data['block']
        screen_name, _ = get_block_type_and_class(screen_block['type'])
        print(screen_name)
        screen_id = screen_block['id']
        
        # Create filename (e.g., ListingDetailsScreen -> listing_details_screen.html)
        file_name = re.sub(r'(?<!^)(?=[A-Z])', '_', screen_name).lower() + ".html"
        file_name = file_name.replace('_screen', '')  # Clean double underscores if any
        
        print(f"Generating {file_name} from {screen_name}...")

        # Start building HTML content
        html_content = '{% extends "base.html" %}\n\n{% block content %}\n'
        html_content += f'<div id="{screen_name}" class="screen">\n'
        html_content += f'    \n'

        # Get components inside the screen
        components = screen_block.get('inputs', {})
        
        for comp_key, comp_data in components.items():
            comp_block = comp_data['block']
            comp_full_type = comp_block['type']
            comp_id = comp_block['id'] # The unique ID from GUI model
            
            # Parse type (e.g., "BidInput (InputField)")
            specific_name, base_class = get_block_type_and_class(comp_full_type)
            
            # Determine HTML Tag
            tag = TAG_MAPPING.get(base_class, "div")
            
            # Generate HTML Element based on type
            html_content += f'\n    '
            
            if tag == "input":
                html_content += f'\n    <input type="text" id="{specific_name.upper()}" class="{base_class.lower()}" placeholder="{specific_name}..." />'
            
            elif tag == "button":
                html_content += f'\n    <button id="{specific_name.upper()}" class="{base_class.lower()}">{specific_name}</button>'
            
            elif tag == "img":
                html_content += f'\n    <div id="{specific_name.upper()}" class="{base_class.lower()}">'
                html_content += f'\n        <img src="placeholder.jpg" alt="{specific_name}" />'
                html_content += '\n    </div>'
                
            elif tag == "h3":
                html_content += f'\n    <h3 id="{specific_name.upper()}" class="{base_class.lower()}">{specific_name}</h3>'
                
            else:
                html_content += f'\n    <div id="{specific_name.upper()}" class="{base_class.lower()}">\n        \n    </div>'
            
            html_content += '\n'

        html_content += '</div>\n{% endblock %}\n'

        # Save the file
        with open(f'templates/{file_name}', 'w') as out_f:
            out_f.write(html_content)

if __name__ == "__main__":
    generate_html_from_gui()