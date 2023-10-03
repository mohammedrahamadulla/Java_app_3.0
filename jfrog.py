#!/usr/bin/env python3

# Import libraries
import requests

# Call the 'upload_to_artifactory
def jfrogUpload():
    url = 'http://3.85.110.208:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    jar_path = '/home/ubuntu/Java_app_3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    username = 'admin'
    password = 'India@123'
    
    # Open the local JAR file in binary read mode
    with open(jar_path, 'rb') as file:
        # Send an HTTP PUT request to the specified Artifactory URL.
        response = requests.put(url, auth=(username,password), data=file)
        
        # Check if the upload was successful based on the HTTP response status code
        if response.status_code == 201:
            print(f"\nSuccessfully uploaded!")
        else:
            # Print an error message if the upload failed.
            print(f"Failed to upload {response.status_code}")
    
jfrogUpload()


