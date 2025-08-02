import itertools
import requests
from requests.auth import HTTPBasicAuth
import zipfile
import base64
from pathlib import Path
import os



def generate_password_dict():
    chars = [('p', 'P'), ('a', 'A', '@'), ('s', 'S', '5'), ('s', 'S', '5'),
             ('w', 'W'), ('o', 'O', '0'), ('r', 'R'), ('d', 'D')]
    permutations = itertools.product(*chars)

    with open('dict.txt', 'w') as file:
        for perm in permutations:
            password = ''.join(perm)
            file.write(password + '\n')


def brute_force_authenticate():
    print("🔐 Starting brute force...")
    url = 'http://recruitment.warpdevelopment.co.za/api/authenticate'
    username = 'John'

    try:
        with open('dict.txt', 'r') as file:
            passwords = file.read().splitlines()

        for password in passwords[:5000]:
            print(f"🔍 Trying: {password}")
            response = requests.get(url, auth=HTTPBasicAuth(username, password))
            if response.status_code == 200:
                print("✅ Found Password:", password)
                print("🌐 Temp URL:", response.text)
                return response.text.strip()

    except Exception as e:
        print("❌ Brute force error:", e)

    print("❌ Password not found.")
    return None




EXCLUDED_DIRS = {"node_modules", ".expo", ".next", "__pycache__"}

def create_zip(temp_url):
    zip_filename = "submission.zip"
    included_items = [
        "cvfrontend",
        "cvsubmission",
        "cvsubmission-app",
        "cv.pdf",
        "README.md",
    ]

    try:
        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
            for item in included_items:
                if os.path.isdir(item):
                    for root, dirs, files in os.walk(item):
                        # Filter out excluded directories
                        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path)
                            zipf.write(file_path, arcname)
                            print(f"📦 Zipped: {arcname}")
                elif os.path.isfile(item):
                    zipf.write(item, os.path.basename(item))
                    print(f"📄 Zipped: {item}")
        
        # Encode zip to base64
        with open(zip_filename, "rb") as f:
            encoded_zip = base64.b64encode(f.read()).decode("utf-8")

        return submit_cv(encoded_zip, temp_url)

    except Exception as e:
        print("❌ ZIP Creation Error:", e)
        return False



def submit_cv(encoded_zip, temp_url):
    data = {
        "Data": encoded_zip,
        "Name": "Ludmil",
        "Surname": "Avelino",
        "Email": "ludmilpaulo@gmail.com"
    }

    try:
        response = requests.post(temp_url, json=data)
        if response.status_code == 200:
            print("✅ Submission Successful")
            return True
        else:
            print("❌ Submission Failed", response.status_code, response.text)
            return False
    except Exception as e:
        print("🚨 Error during submission:", e)
        return False
