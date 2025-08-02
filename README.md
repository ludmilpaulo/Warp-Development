# CV Submission Brute-Force App

This project is a technical challenge solution designed to demonstrate problem-solving, backend automation, and secure file handling via a brute-force Basic Authentication attack followed by an automated file submission to a REST API.

## 📋 Problem Summary

You are tasked with retrieving a temporary upload URL from a protected API using Basic Auth. However, the password is forgotten but known to be a permutation of `"password"`, with common substitutions (`a → @`, `s → 5`, `o → 0`) and case variations.

Once the correct password is found, the application:

1. Retrieves the temporary upload URL.
2. Zips the following files:
   - `cv.pdf` — the applicant's résumé
   - `dict.txt` — the generated password permutations
   - `submissions/utils.py` — the Python source code
3. Encodes the ZIP file in Base64.
4. Submits the encoded ZIP along with applicant details to the provided upload URL via JSON.

---

## 🧪 Technologies Used

- **Python 3.11+**
- **Django 5.x**
- **Redux Toolkit (RTK Query)**
- **Next.js (Frontend)** and **React Native (optional mobile)**
- **TailwindCSS** for professional and modern UI/UX
- **Headless UI** for animated transitions
- **`requests`** for HTTP communication
- **`zipfile`, `base64`, `itertools`** for file handling and encoding

---

## 📂 Project Structure

