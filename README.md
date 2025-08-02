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

