import itertools
import requests
from requests.auth import HTTPBasicAuth
import zipfile
import base64
from pathlib import Path


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


def create_zip(temp_url):
    try:
        files_to_zip = ['dict.txt', 'cv.pdf', 'submissions/utils.py']
        zip_filename = 'submission.zip'

        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for file in files_to_zip:
                zipf.write(file)

        with open(zip_filename, 'rb') as file:
            encoded_zip = base64.b64encode(file.read()).decode()

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
