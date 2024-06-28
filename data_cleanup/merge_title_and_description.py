import csv
import json

def merge_csv_to_json(desc_csv, no_desc_csv, output_json):
    # Read the descriptions CSV into a dictionary
    desc_dict = {}
    with open(desc_csv, mode='r', newline='', encoding='utf-8') as desc_file:
        desc_reader = csv.DictReader(desc_file)
        for row in desc_reader:
            project_id = row['ProjectID']
            desc_dict[project_id] = row['Description']

    # Read the no-description CSV and merge with descriptions
    merged_data = []
    with open(no_desc_csv, mode='r', newline='', encoding='utf-8') as no_desc_file:
        no_desc_reader = csv.DictReader(no_desc_file)
        for row in no_desc_reader:
            project_id = row['ProjectID']
            if project_id in desc_dict:
                merged_row = {
                    'ProjectID': project_id,
                    'Title': row['Title'],
                    'Department/Ind.Agency': row['Department/Ind.Agency'],
                    'NaicsCode': row['NaicsCode'],
                    'ProductServiceCode': row['ProductServiceCode'],
                    'Description': desc_dict[project_id],
                    'PlaceOfPerformanceCountry': row['PlaceOfPerformanceCountry'],
                    'PlaceOfPerformanceState': row['PlaceOfPerformanceState'],
                    'PlaceOfPerformanceCity': row['PlaceOfPerformanceCity'],
                    'PlaceOfPerformanceStreetAddress': row['PlaceOfPerformanceStreetAddress'],
                    'PlaceOfPerformanceZip': row['PlaceOfPerformanceZip'],
                    'Sub-Tier': row['Sub-Tier'],
                    'ResponseDueDate': row['ResponseDueDate'],
                    'SetASide': row['SetASide'],
                    'SetASideCode': row['SetASideCode'],
                    'Type': row['Type'],
                    'PostedDate': row['PostedDate']
                }
                merged_data.append(merged_row)

    # Write the merged data to a JSON file
    with open(output_json, mode='w', encoding='utf-8') as output_file:
        json.dump(merged_data, output_file, indent=4)

# Example usage
merge_csv_to_json(
    '/Users/haiyangliu/Workspace/gov_opportunity_new/content/opportunities/opportunities_transformed_description_only.csv',
    '/Users/haiyangliu/Workspace/gov_opportunity_new/content/opportunities/opportunities_transformed_no_description_clean.csv',
    '/Users/haiyangliu/Workspace/gov_opportunity_new/content/opportunities/merged_opportunities.json'
)
