import requests

def jfrogupload():
    local_jar_path = "/home/ubuntu/Java_app_3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"
    artifactory_url = "http://34.201.127.250:8082/artifactory/example-repo-local/"
    username = "admin"
    password = "India@123"
    with open(local_file_path, 'rb') as file:
        response = requests.put(artifactory_url,data=file,auth=(username, password))
            
        if response.status_code == 201:
            print(f"Successfully uploaded {local_file_path} to {artifactory_url}")
        else:
            print(f"Failed to upload {local_file_path}. Response: {response.status_code} - {response.text}")
















#!/usr/bin/env python3

import requests

def jfrogUpload():
    url = 'http://34.201.127.250:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    jar_path = '/home/ubuntu/Java_app_3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    username = 'admin'
    password = 'India@123'
    with open(jar_path, 'rb') as file:
        response = requests.put(url, auth=(username,password), data=file)

        if response.status_code == 201:
            print(f"\nSuccessfully uploaded!")
        else:
            print(f"PUT request failed with status code {response.status_code}")
            