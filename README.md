# 🚀 CV Submission Brute-Force App

This repository demonstrates my full-stack engineering skills, combining **backend automation, API integration, file handling, and professional frontend/mobile development** in one cohesive solution.

---

## 📋 Challenge Summary

The technical test required:

- **Brute-forcing** a Basic Auth-protected API where the password is an unknown permutation of `"password"`, using substitutions (`a → @`, `s → 5`, `o → 0`) and case variations.
- On success, **retrieving a temporary upload URL** and then
- **Submitting a zip archive** containing my CV and the project source code.

---

## 🧠 Solution Overview

1. **Dictionary Generation:**  
   Python script (`utils.py`) generates all possible permutations of "password" with allowed substitutions and casing.
2. **Brute-force Logic:**  
   The script attempts each permutation against the API until it authenticates successfully, retrieving the upload URL.
3. **Zip Packaging:**  
   The application zips the following for submission:
   - All project folders:  
     - `cvfrontend/` (Next.js frontend)
     - `cvsubmission/` (Django backend)
     - `cvsubmission-app/` (Expo React Native app)
   - Required files:  
     - `cv.pdf` (My resume)
     - `README.md`
   - Excludes heavy and unnecessary directories: `node_modules/`, `.expo/`, `.next/`, `__pycache__/`
4. **Base64 Encoding & Submission:**  
   The ZIP file is encoded and POSTed to the API with my applicant details.
5. **Frontend & Mobile UI:**  
   The app includes both a modern Next.js/Tailwind web UI and an Expo/React Native mobile UI for submitting and tracking status, using Redux Toolkit (RTK Query) for clean API integration.

---

## 🛠️ Technologies Used

- **Python 3.11+** – Automation, brute-force, zip, API submission
- **Django 5.x** – REST API backend
- **Next.js (TypeScript)** – Web frontend
- **Redux Toolkit / RTK Query** – API data & state management
- **TailwindCSS** – Responsive, professional web UI
- **Expo + React Native + twrnc** – Optional mobile UI (Tailwind for React Native)
- **requests, itertools, zipfile, base64** – Python libraries for HTTP, combinatorics, file I/O, encoding

---

## 📂 Project Structure
cvfrontend/ # Web frontend (Next.js + Tailwind + RTK)
cvsubmission/ # Django backend with brute-force and submission logic
│ └── submissions/ # Backend logic, including utils and views
cvsubmission-app/ # Expo + React Native app (optional mobile UI)
cv.pdf # My resume (PDF)
dict.txt # Generated password permutations (auto-generated)


---

## 🔒 Security & Logic Flow

1. **Generate all "password" permutations:**  
   Uses Python’s `itertools.product()` to create all possible forms, saved to `dict.txt`.

2. **Brute-force API login:**  
   Attempts each password using Basic Auth until the correct one is found, retrieving the temp upload URL.

3. **Zip all relevant code:**  
   Folders and files are zipped (excluding heavy or irrelevant directories), maintaining project structure.

4. **Base64 encode ZIP & submit via API:**  
   The archive is submitted in a JSON POST to the upload URL with my name, surname, and email.

5. **Modern UI/UX:**  
   - **Next.js web UI:** Attractive TailwindCSS design, loading overlay, status feedback.
   - **Expo React Native app:** Mobile-optimized, styled with `twrnc`, native ActivityIndicator for loading.

---

## 🧪 How to Run

### Backend (Django)
```bash
cd cvsubmission
python manage.py runserver

### Web Frontend (Next.js)
cd cvfrontend
npm install
npm run dev

Mobile App (Expo)
cd cvsubmission-app
npm install
npx expo start

🌟 Skills Demonstrated
Secure API automation and Basic Auth brute-forcing (Python)

RESTful Django API, CSRF-exempt views, file and encoding logic

Robust frontend with Next.js, TypeScript, Tailwind, Redux Toolkit

Real-time feedback and animated UI/UX (web and mobile)

Expo/React Native mobile skills with Tailwind-style design

Clean project organization, packaging, and deployment automation

Practical problem-solving and software delivery from backend to UI

📧 Author
Ludmil Avelino
Full Stack Software Engineer
Email: ludmilpaulo@gmail.com



