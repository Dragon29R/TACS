import json
import os

def create_runtime_config(dsml_input_path, output_json_path):    
    # 1. Load the raw DSML file
    try:
        with open(dsml_input_path, 'r', encoding='utf-8') as f:
            dsml_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find DSML file at {dsml_input_path}")
        return

    # 2. Navigate the complex DSML structure
    # Note: Adjust index [0] if your structure differs
    try:
        main_block = dsml_data['blocks']['blocks'][0]
        inputs = main_block['inputs']
        
        # Helper to safely get field values
        def get_field(block_name, field_name):
            return inputs[block_name]['block']['fields'].get(field_name)

        # 3. Extract only what the frontend JavaScript needs
        runtime_config = {
            "theme": {
                "primaryColor": get_field('COMMUNITY', 'color'),
                "fontFamily": get_field('THEMECONFIG', 'fontFamily'),
                "colorScheme": get_field('THEMECONFIG', 'colorScheme'),
                "logoUrl": get_field('THEMECONFIG', 'logoPath'),
                "backgroundImage": get_field('THEMECONFIG', 'backgroundImage')
            },
            "constraints": {
                # Ensure these are converted to the right type (int/bool) if needed
                "maxPhotos": int(get_field('ITEMCONFIG', 'maxItemPhotos') or 5),
                "minPhotos": int(get_field('ITEMCONFIG', 'minItemPhotos') or 0)
            },
            "text": {
                "appName": main_block['fields']['name'],
                "communityName": get_field('COMMUNITY', 'name')

            }
        }

        # 4. Create Output Directory if it doesn't exist
        os.makedirs(os.path.dirname(output_json_path), exist_ok=True)

        # 5. Save the clean JSON file
        with open(output_json_path, 'w', encoding='utf-8') as f:
            json.dump(runtime_config, f, indent=4)
        
        print(f"Success! Runtime config generated at: {output_json_path}")
        print(f"   (Preview: Color={runtime_config['theme']['primaryColor']}, App={runtime_config['text']['appName']})")

    except Exception as e:
        print(f"Error parsing DSML structure: {e}")

# ==========================================
#               MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    # Define your file paths here
    INPUT_DSML_FILE = 'DSML_model.json'  # The file exported from Hugo's tool
    OUTPUT_CONFIG_FILE = 'jinja/out/JSON/app_config.json' # Where the web app will look for it
    
    print("--- Starting DSML to AppConfig Extraction ---")
    create_runtime_config(INPUT_DSML_FILE, OUTPUT_CONFIG_FILE)