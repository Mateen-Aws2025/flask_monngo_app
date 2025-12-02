# Flask + MongoDB Atlas Assignment

## What this project includes
- `app.py` — Flask application with:
  - `/api` route that reads from `data.json` and returns JSON list.
  - `/` route: form to submit name and email.
  - `/submit` route: inserts into MongoDB Atlas and redirects to `/success` on success.
  - `/success` route: shows "Data submitted successfully".
- `data.json` — backend data file used by `/api`.
- `templates/` — HTML templates for the form and success page.
- `requirements.txt`

## Setup locally (macOS / Linux)
1. Clone repo or unzip project folder.
2. Create virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Set your MongoDB Atlas connection string (replace `<your-conn-string>`):
```bash
export MONGODB_URI='<your-conn-string>'
```
The connection string should include username, password, and default database (or the server will use 'test'). Example: `mongodb+srv://user:pass@cluster0.abcd.mongodb.net/mydb?retryWrites=true&w=majority`

4. Run the app:
```bash
python app.py
```
5. Open `http://127.0.0.1:5000` in your browser. The `/api` endpoint is at `http://127.0.0.1:5000/api`.

## Testing API with curl
```bash
curl http://127.0.0.1:5000/api
```

## GitHub-ready
- Initialize a git repo, commit, and push to your GitHub remote.

## Screenshots
On macOS you can take screenshots using:
- Full screen: `Cmd+Shift+3`
- Selection: `Cmd+Shift+4` (then drag)
- From terminal: `screencapture -x screenshot.png`

Include screenshots of:
- Terminal commands (venv & running app)
- Browser showing form
- Browser showing success message
- Output of `/api` (curl or browser)

