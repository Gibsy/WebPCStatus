# WebPC Status for Neocities

This is a simple project to track the status of a PC and display it on a Neocities web page.  
The Python script updates `status.json` on Neocities, and the HTML page reads this file to show whether the PC is online or offline.

---

## Features

- Python script `main.py` updates status every 30 seconds.
- Example HTML page (`example.html`) shows:
  - Online/Offline status
  - Time since PC online/offline
  - Offline is detected if the status hasn't updated for more than 1 minute.
- Easy to use, lots of room for improvement!

---

## Quick guide

### 1. Clone the repository

```bash
git clone https://github.com/Gibsy/WebPCStatus.git
cd WebPCStatus 
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Create a .env file in the project root
```bash
API_KEY=YOUR_NEOCITIES_API_KEY
SITE=YOUR_SITE_NAME
```
### 4. Run the Python script
```bash
python main.py
```
