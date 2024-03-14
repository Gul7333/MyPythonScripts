import xml.etree.ElementTree as ET
import sqlite3
from datetime import datetime

def get_drugs_from_database(database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Assuming you have a table named 'drugs' with a column 'name'
    cursor.execute("SELECT drug_name FROM medinfo_drugs")
    drugs = [row[0] for row in cursor.fetchall()]

    conn.close()
    return drugs

def create_sitemap(urls):
    # Create the root element
    root = ET.Element("urlset")
    root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    # Iterate over the URLs and create <url> elements
    for url in urls:
        url_elem = ET.SubElement(root, "url")
        
        loc_elem = ET.SubElement(url_elem, "loc")
        loc_elem.text = url
        
        lastmod_elem = ET.SubElement(url_elem, "lastmod")
        lastmod_elem.text = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")  # Format the date and time in W3C format

    # Create XML tree
    tree = ET.ElementTree(root)

    # Write to file
    tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)

# Example usage
base_url = "https://drug-pedia.vercel.app"
database_path = "./druginfostore.db"

# Get drugs from the database
drugs = get_drugs_from_database(database_path)

# Generate URLs
urls = [f"{base_url}/index.html?drug={drug}" for drug in drugs]

# Create sitemap
create_sitemap(urls)








































































































































































