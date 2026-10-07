# Program 9: Use Google App Engine Launcher to launch web applications


## Aim
To use Google App Engine (Launcher) to create and run a simple web application.

## Prerequisites
- Google App Engine SDK + GoogleAppEngineLauncher (legacy Python 2 runtime, as in the manual), **or** Python 3 + Flask for the modern version

## Repository contents
```
09-google-app-engine/
├── .gitignore
├── README.md
├── code.txt
├── output/output_screenshot.png
├── src/legacy/app.yaml
├── src/legacy/index.py
├── src/modern/app.yaml
├── src/modern/main.py
├── src/modern/requirements.txt
├── src/run_local.py
```
`code.txt` contains every program/command used, in one plain-text file.

## Procedure
1. Create folder `apps/ae-01-trivial`.
2. Create `app.yaml` and `index.py` there (from `src/legacy/`).
3. Open **GoogleAppEngineLauncher** > **File > Add Existing Application** > select the `ae-01-trivial` folder.
4. Select the app and click **Run** (green icon) then **Browse** - the app opens at `http://localhost:8080/`.
5. Edit `index.py` to put your own name and refresh the browser.
6. Use **Logs** to watch the GET requests. A yellow icon means an error in `app.yaml` - check the log.
7. **Without the Launcher:** `python src/run_local.py` serves the legacy script locally, or run the Flask version in `src/modern/` (`pip install -r requirements.txt && python main.py`).

## Expected output
The browser shows `Hello there <your name>`.


## Result
The Google App Engine web application was created and run successfully.

