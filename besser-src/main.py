import os
import sys
import json
import shutil


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# Define paths relative to BASE_DIR
DSML_PATH = os.path.join(BASE_DIR, 'DSML_model.json')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'jinja', 'templates')
CONFIG_OUTPUT_DIR = os.path.join(OUTPUT_DIR, 'JSON')
APP_CONFIG_FILE = os.path.join(CONFIG_OUTPUT_DIR, 'app_config.json')

try:
    from model_to_model_transformations.structural_meta_to_model import create_domain_model_from_dsml
    from model_to_model_transformations.gui_meta_to_model import create_gui_model_from_dsml
    from model_to_text.dsmlToAppConfig import create_runtime_config
    from model_to_text.guiGenerator import GuiGenerator
except ImportError as e:
    print(f"Import Error: {e}")
    sys.exit(1)

def main():

    if os.path.exists(OUTPUT_DIR):
        print(f"Cleaning output directory: {OUTPUT_DIR}")
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    # Model-to-Model Structural
    structural_model = create_domain_model_from_dsml(DSML_PATH)
    if structural_model:
        print(f"- Structural Model created: {structural_model.name}")
    else:
        print("- Error: Structural Model generation failed.")
        sys.exit(1)

    # Model-to-Model GUI
    gui_model = create_gui_model_from_dsml(DSML_PATH)
    if gui_model:
        print(f"- GUI Model created: {gui_model.name}")
    else:
        print("- Error: GUI Model generation failed.")
        sys.exit(1)

    # DSML to App Config (Cleaned JSON)
    create_runtime_config(DSML_PATH, APP_CONFIG_FILE)
    
    dsml_config = {}
    if os.path.exists(APP_CONFIG_FILE):
        with open(APP_CONFIG_FILE, 'r', encoding='utf-8') as f:
            dsml_config = json.load(f)
    else:
        print("- Error: App config file was not created.")

    # Model-to-Text Code Generation
    print("\nRunning Besser Generator...")
    generator = GuiGenerator(
        model=gui_model,
        dsml_config=dsml_config,
        output_dir=OUTPUT_DIR,
        template_dir=TEMPLATES_DIR
    )
    
    generator.generate()
    
    print("\n=========================================")
    print(f"Output located at: {OUTPUT_DIR}")
    print("=========================================")

if __name__ == "__main__":
    main()