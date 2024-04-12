

































import requests
import json

def fetch_data(brand_name, top_param):
    base_url = "https://public.dra.gov.pk/cp/RDI_Pricing.svc/PricningImports1"
    filter_query = f"substringof('{brand_name}', BrandName) and isPublic eq true"
    
    try:
        top_param = int(top_param)
    except ValueError:
        print("Invalid input for 'top' parameter. Please enter an integer value.")
        return None
    
    if top_param <= 0:
        print("Invalid value for 'top' parameter. Please enter a positive integer.")
        return None
    
    url = f"{base_url}?$filter=({filter_query})&$top={top_param}"
    
    headers = {
        "Accept": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        print(f"Response content: {response.content}")
        return None

def main():
    brand_name = input("Enter the brand name: ")
    top_param = input("Enter the value for the 'top' parameter: ")
    
    data = fetch_data(brand_name, top_param)
    
    if data:
        with open("result.json", "w") as file:
            json.dump(data, file)
        print("Data saved successfully to result.json")

if __name__ == "__main__":
    main()











































































































































































































