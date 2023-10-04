# Import libraries
import requests
import json

# Call the 'upload_to_artifactory' function using the loaded configuration values.
def jfrog_artifactory(jar_path, artifactory_url, username, password):
    # Retrieve individual configuration values using the respective keys.
    jar_path = config["jar_path"]
    artifactory_url = config["artifactory_url"]
    username = config["username"]
    password = config["password"]
    
    # Load configurations from the external file 'config.json'.
    # This allows the configuration to be separated from the main code.
    with open("config.json", "r") as config_file:
         # Parse the JSON content of the configuration file into a Python dictionary.
         config = json.load(config_file)
        
         # Send an HTTP PUT request to the specified Artifactory URL.
         response = requests.put(artifactory_url,data=config_file,auth=(username, password))
        
         # Check the HTTP response status to see if the upload was successful.
         if response.status_code == 201:
             print(f"Successfully uploaded {jar_path} to {artifactory_url}")
         else:
             # Print an error message if the upload failed.
             print(f"Failed to upload {jar_path}. Response: {response.status_code} - {response.text}")