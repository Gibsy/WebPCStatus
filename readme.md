# WebPC Status for Neocities

This is a simple project to track the online/offline status of your PC and display it on a Neocities web page.  
The Python script updates `status.json` on Neocities, and the HTML page reads this file to show whether the PC is online or offline.

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
---

Then just add status.js to your website, you can check for example [here](https://github.com/Gibsy/gibsy.github.io) (use DevTools)
