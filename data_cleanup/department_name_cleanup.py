import csv

# Define a mapping from the original value to the more human-readable format
department_mapping = {
    "AGENCY FOR INTERNATIONAL DEVELOPMENT": "Agency for International Development",
    "AGRICULTURE, DEPARTMENT OF": "Department of Agriculture",
    "AMERICAN BATTLE MONUMENTS COMMISSION": "American Battle Monuments Commission",
    "ARCHITECT OF THE CAPITOL": "Architect of the Capitol",
    "COMMERCE, DEPARTMENT OF": "Department of Commerce",
    "COURT SERVICES AND OFFENDER SUPERVISION AGENCY": "Court Services and Offender Supervision Agency",
    "DEPT OF DEFENSE": "Department of Defense",
    "DISTRICT OF COLUMBIA COURTS": "District of Columbia Courts",
    "ENERGY, DEPARTMENT OF": "Department of Energy",
    "ENVIRONMENTAL PROTECTION AGENCY": "Environmental Protection Agency",
    "GENERAL SERVICES ADMINISTRATION": "General Services Administration",
    "HEALTH AND HUMAN SERVICES, DEPARTMENT OF": "Department of Health and Human Services",
    "HOMELAND SECURITY, DEPARTMENT OF": "Department of Homeland Security",
    "INTERIOR, DEPARTMENT OF THE": "Department of the Interior",
    "INTERNATIONAL BOUNDARY AND WATER COMMISSION: US-MEXICO": "International Boundary and Water Commission: US-Mexico",
    "JUSTICE, DEPARTMENT OF": "Department of Justice",
    "LABOR, DEPARTMENT OF": "Department of Labor",
    "MILLENNIUM CHALLENGE CORPORATION": "Millennium Challenge Corporation",
    "NATIONAL AERONAUTICS AND SPACE ADMINISTRATION": "National Aeronautics and Space Administration",
    "NATIONAL CAPITAL PLANNING COMMISSION": "National Capital Planning Commission",
    "NATIONAL SCIENCE FOUNDATION": "National Science Foundation",
    "NUCLEAR REGULATORY COMMISSION": "Nuclear Regulatory Commission",
    "POSTAL SERVICE": "Postal Service",
    "SMITHSONIAN INSTITUTION": "Smithsonian Institution",
    "STATE, DEPARTMENT OF": "Department of State",
    "TRANSPORTATION, DEPARTMENT OF": "Department of Transportation",
    "TREASURY, DEPARTMENT OF THE": "Department of the Treasury",
    "UNITED STATES GOVERNMENT PUBLISHING OFFICE": "United States Government Publishing Office",
    "UNITED STATES HOLOCAUST MEMORIAL MUSEUM": "United States Holocaust Memorial Museum",
    "VETERANS AFFAIRS, DEPARTMENT OF": "Department of Veterans Affairs"
}

# Define a mapping from the original value to the more human-readable format
sub_tier_mapping = {
    "AGENCY FOR INTERNATIONAL DEVELOPMENT": "Agency for International Development",
    "AGRICULTURAL RESEARCH SERVICE": "Agricultural Research Service",
    "AMERICAN BATTLE MONUMENTS COMMISSION": "American Battle Monuments Commission",
    "ANIMAL AND PLANT HEALTH INSPECTION SERVICE": "Animal and Plant Health Inspection Service",
    "ARCHITECT OF THE CAPITOL": "Architect of the Capitol",
    "ARMY/AIR FORCE EXCHANGE SERVICE": "Army/Air Force Exchange Service",
    "BUREAU OF INDIAN AFFAIRS": "Bureau of Indian Affairs",
    "BUREAU OF LAND MANAGEMENT": "Bureau of Land Management",
    "BUREAU OF RECLAMATION": "Bureau of Reclamation",
    "BUREAU OF THE FISCAL SERVICE": "Bureau of the Fiscal Service",
    "CENTERS FOR DISEASE CONTROL AND PREVENTION": "Centers for Disease Control and Prevention",
    "COURT SERVICES AND OFFENDER SUPERVISION AGENCY": "Court Services and Offender Supervision Agency",
    "DEFENSE COMMISSARY AGENCY  (DECA)": "Defense Commissary Agency (DECA)",
    "DEFENSE FINANCE AND ACCOUNTING SERVICE (DFAS)": "Defense Finance and Accounting Service (DFAS)",
    "DEFENSE HEALTH AGENCY (DHA)": "Defense Health Agency (DHA)",
    "DEFENSE INFORMATION SYSTEMS AGENCY (DISA)": "Defense Information Systems Agency (DISA)",
    "DEFENSE LOGISTICS AGENCY": "Defense Logistics Agency",
    "DEPARTMENTAL OFFICES": "Departmental Offices",
    "DEPT OF DEFENSE EDUCATION ACTIVITY (DODEA)": "Dept of Defense Education Activity (DODEA)",
    "DEPT OF THE AIR FORCE": "Dept of the Air Force",
    "DEPT OF THE ARMY": "Dept of the Army",
    "DEPT OF THE NAVY": "Dept of the Navy",
    "DISTRICT OF COLUMBIA COURTS": "District of Columbia Courts",
    "EMPLOYMENT AND TRAINING ADMINISTRATION": "Employment and Training Administration",
    "ENERGY, DEPARTMENT OF": "Department of Energy",
    "ENVIRONMENTAL PROTECTION AGENCY": "Environmental Protection Agency",
    "FARM PRODUCTION AND CONSERVATION BUSINESS CENTER": "Farm Production and Conservation Business Center",
    "FEDERAL ACQUISITION SERVICE": "Federal Acquisition Service",
    "FEDERAL AVIATION ADMINISTRATION": "Federal Aviation Administration",
    "FEDERAL BUREAU OF INVESTIGATION": "Federal Bureau of Investigation",
    "FEDERAL EMERGENCY MANAGEMENT AGENCY": "Federal Emergency Management Agency",
    "FEDERAL HIGHWAY ADMINISTRATION": "Federal Highway Administration",
    "FEDERAL PRISON INDUSTRIES, INC": "Federal Prison Industries, Inc.",
    "FEDERAL PRISON SYSTEM / BUREAU OF PRISONS": "Federal Prison System / Bureau of Prisons",
    "FOOD AND DRUG ADMINISTRATION": "Food and Drug Administration",
    "FOREST SERVICE": "Forest Service",
    "GREAT LAKES ST LAWRENCE SEAWAY DEVELOPMENT CORPORATION": "Great Lakes St. Lawrence Seaway Development Corporation",
    "INDIAN HEALTH SERVICE": "Indian Health Service",
    "INTERNATIONAL BOUNDARY AND WATER COMMISSION: US-MEXICO": "International Boundary and Water Commission: US-Mexico",
    "MARITIME ADMINISTRATION": "Maritime Administration",
    "MILLENNIUM CHALLENGE CORPORATION": "Millennium Challenge Corporation",
    "NATIONAL AERONAUTICS AND SPACE ADMINISTRATION": "National Aeronautics and Space Administration",
    "NATIONAL CAPITAL PLANNING COMMISSION": "National Capital Planning Commission",
    "NATIONAL GEOSPATIAL-INTELLIGENCE AGENCY (NGA)": "National Geospatial-Intelligence Agency (NGA)",
    "NATIONAL HIGHWAY TRAFFIC SAFETY ADMINISTRATION": "National Highway Traffic Safety Administration",
    "NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY": "National Institute of Standards and Technology",
    "NATIONAL INSTITUTES OF HEALTH": "National Institutes of Health",
    "NATIONAL OCEANIC AND ATMOSPHERIC ADMINISTRATION": "National Oceanic and Atmospheric Administration",
    "NATIONAL PARK SERVICE": "National Park Service",
    "NATIONAL SCIENCE FOUNDATION": "National Science Foundation",
    "OFFICE OF THE ASSISTANT SECRETARY FOR ADMINISTRATION AND MANAGEMENT": "Office of the Assistant Secretary for Administration and Management",
    "OFFICE OF THE SECRETARY": "Office of the Secretary",
    "POSTAL SERVICE": "Postal Service",
    "PUBLIC BUILDINGS SERVICE": "Public Buildings Service",
    "SMITHSONIAN INSTITUTION": "Smithsonian Institution",
    "STATE, DEPARTMENT OF": "Department of State",
    "TRANSPORTATION SECURITY ADMINISTRATION": "Transportation Security Administration",
    "UNITED STATES GOVERNMENT PUBLISHING OFFICE": "United States Government Publishing Office",
    "UNITED STATES HOLOCAUST MEMORIAL MUSEUM": "United States Holocaust Memorial Museum",
    "US COAST GUARD": "US Coast Guard",
    "US CUSTOMS AND BORDER PROTECTION": "US Customs and Border Protection",
    "US FISH AND WILDLIFE SERVICE": "US Fish and Wildlife Service",
    "US GEOLOGICAL SURVEY": "US Geological Survey",
    "US SPECIAL OPERATIONS COMMAND (USSOCOM)": "US Special Operations Command (USSOCOM)",
    "USDA, DEPARTMENTAL ADMINISTRATION": "USDA, Departmental Administration",
    "VETERANS AFFAIRS, DEPARTMENT OF": "Department of Veterans Affairs",
    "WASHINGTON HEADQUARTERS SERVICES (WHS)": "Washington Headquarters Services (WHS)"
}

def update_department_field(input_csv, output_csv):
    with open(input_csv, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for row in reader:
            department = row.get("Department/Ind.Agency", "")
            if department in department_mapping:
                row["Department/Ind.Agency"] = department_mapping[department]
            sub_tier = row.get("Sub-Tier", "")
            if sub_tier in sub_tier_mapping:
                row["Sub-Tier"] = sub_tier_mapping[sub_tier]
            writer.writerow(row)

if __name__ == "__main__":
    update_department_field('/Users/haiyangliu/Workspace/gov_opportunity_new/content/opportunities/opportunities_transformed_no_description.csv', 'opportunities_transformed_no_description_clean.csv')
