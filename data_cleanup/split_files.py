import json
import os

def write_objects_to_files(json_file_path, output_dir, key_attribute):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Write each object to a new file
    for obj in data:
        # Construct the filename using the key_attribute
        filename = f"project_{obj[key_attribute]}.json"
        output_path = os.path.join(output_dir, filename)

        # Write the object to a new file
        with open(output_path, 'w') as output_file:
            json.dump(obj, output_file, indent=4)

    print(f"Successfully wrote {len(data)} files to {output_dir}")

# Usage example
write_objects_to_files('/Users/haiyangliu/Workspace/gov_opportunity_new/content/opportunities/merged_opportunities_small.json', 'projects', 'ProjectID')