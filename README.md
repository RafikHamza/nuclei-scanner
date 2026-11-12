# Nuclei Security Scanner — Student Lab

This project is a small web application for checking HTTP security headers on a **local practice website**.

You will use Python, Flask, and [Nuclei](https://github.com/projectdiscovery/nuclei). The scanner shows findings in your browser and saves results in JSONL format.

**Only scan websites you own or have explicit permission to test.** Use the local practice website below for this assignment.

## 1. Install the required software

- **Python 3.10 or newer:** [python.org/downloads](https://www.python.org/downloads/)
- **Nuclei:** [ProjectDiscovery releases](https://github.com/projectdiscovery/nuclei/releases)
- **Git:** [git-scm.com/downloads](https://git-scm.com/downloads) (or download the project ZIP)

On Windows, download the Nuclei Windows release, extract `nuclei.exe`, and add its directory to your system `PATH`. On Linux/macOS, follow the [Nuclei installation guide](https://docs.projectdiscovery.io/tools/nuclei/install).

Check that Nuclei is available:

```text
nuclei -version
```

## 2. Set up the project

**Windows (PowerShell)**

```powershell
git clone https://github.com/RafikHamza/nuclei-scanner.git
cd nuclei-scanner
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**Linux/macOS**

```bash
git clone https://github.com/RafikHamza/nuclei-scanner.git
cd nuclei-scanner
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
```

For your submission, **fork the repository first and clone your own fork** so you can commit your improvements.

## 3. Start the practice website

Open **Terminal 1** in the project folder.

**Windows:**

```powershell
.\.venv\Scripts\python.exe -m http.server 8000 --bind 127.0.0.1
```

**Linux/macOS:**

```bash
./.venv/bin/python -m http.server 8000 --bind 127.0.0.1
```

Leave this terminal running. Your practice website is **http://127.0.0.1:8000**.

## 4. Start the scanner

Open **Terminal 2** in the same project folder.

**Windows:**

```powershell
.\.venv\Scripts\python.exe app.py
```

**Linux/macOS:**

```bash
./.venv/bin/python app.py
```

Open **http://127.0.0.1:10000** in your browser. Enter **http://127.0.0.1:8000** and click **Scan**. Review the findings. Press `Ctrl+C` in both terminals when finished.

## 5. Understand the results

1. Your browser sends the URL to Flask.
2. Flask verifies that the URL is an authorized laboratory target.
3. Nuclei runs the provided YAML security-header template.
4. Nuclei saves the results in the `results/` folder as JSONL.
5. Flask displays the findings in the browser.

The template checks four common headers: `X-Content-Type-Options`, `Content-Security-Policy`, `X-Frame-Options`, and `Referrer-Policy`.

**Important:** A missing header is not automatically a vulnerability. No findings do not mean a website is secure. Scanner errors appear separately.

## 6. Your assignment

1. Fork this repository to your GitHub account and clone your fork.
2. Run the practice website and scanner. Capture a screenshot of the result.
3. Explain how Flask, Nuclei, the YAML template, and JSONL results work together.
4. Identify one limitation and implement **one improvement** (for example, a severity summary, scan history, JSONL download, or improved validation messages).
5. Test before and after your change. Document a successful case and an error case.
6. Submit your GitHub fork link, screenshots or short sanitized logs, and a **1–2 page report** describing the system, improvement, tests, and one difficulty encountered.

### Example marking rubric (10 points)

| Criterion | Points |
| --- | ---: |
| Correct local setup | 2 |
| Explanation of how the application works | 2 |
| Individual improvement | 2.5 |
| Testing and evidence | 2 |
| Report and responsible testing | 1.5 |
| **Total** | **10** |

This example rubric does not replace your course's official assessment rules.

## Troubleshooting

- **Nuclei command not found:** check installation and your system `PATH` (or configure `NUCLEI_BIN`).
- **Target not authorized:** use `http://127.0.0.1:8000`.
- **Scanner error:** check the message displayed on the page.
- **Port already in use:** stop previous processes using that port.

Run the automated tests from the project folder:

```bash
python -m unittest discover -s tests -v
```

On Windows, use `.\.venv\Scripts\python.exe` instead of `python` if needed.

Keep the application on your computer; do not expose the scanner publicly. Never include credentials, private data, or unauthorized scan results in your submission.
