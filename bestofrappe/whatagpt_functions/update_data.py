import frappe
import requests

@frappe.whitelist()
def update_data(doctype, documentName, params):
    header = {
     "Authorization": "token cd44217d68c187d:2c48de9b37526f8"  # Use appropriate token type (Bearer, etc.)
    }
    # Define the URL and parameters
    
    url = f"https://demo.customized.bestoerp.com/api/resource/{doctype}/{documentName}?subscription={params}"
    
    # Make the API request
    request = requests.put(url, headers=header)
    if request.status_code == 200:
        # Parse the response JSON
        # Extract data from the API response as needed  
        # For example, you can access api_response["output"] to get the output of the command
        # Return the "title" value along with the API response data
        return f"Data updated"

    else:
        return f"API request failed with status code {request.status_code}"