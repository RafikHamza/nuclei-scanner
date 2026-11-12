# Nuclei Security Scanner — Student Lab

This project checks HTTP security headers on a **local practice website**. You will use Python, Flask, and [ProjectDiscovery Nuclei](https://github.com/projectdiscovery/nuclei). Findings appear in your browser and are saved as JSONL files.

**Use only systems you own or are explicitly authorized to test.** For this assignment, scan the local practice website described below.

## 1. Install the tools

You need **Python 3.10 or newer**, **Git**, and **Nuclei**.

### Windows students

1. Install [Python](https://www.python.org/downloads/windows/) and [Git](https://git-scm.com/downloads/win).
2. Download the **Windows** Nuclei executable from the [official releases](https://github.com/projectdiscovery/nuclei/releases). Extract `nuclei.exe` and add its folder to your system's `PATH`.
3. Open **PowerShell** and check:

```powershell
py --version
git --version
nuclei -version
```

### macOS students (Apple Silicon or Intel)

1. Install [Python](https://www.python.org/downloads/macos/) and [Git](https://git-scm.com/downloads/mac).
2. Install [Homebrew](https://brew.sh/) if you do not already have it. In **Terminal**, run:

```bash
brew install nuclei
```

3. Check that all three tools are available:

```bash
python3 --version
git --version
nuclei -version
```

If you prefer not to use Homebrew, download the appropriate **macOS** Nuclei executable (Apple Silicon: ARM64; Intel: AMD64) from the [official releases](https://github.com/projectdiscovery/nuclei/releases) and follow the included installation instructions.

**Check the Python version:** it must be 3.10 or newer. If any command is not found, resolve that installation before continuing.

## 2. Download and set up the project

First **fork this repository** on GitHub to your own account. In the commands below, replace `YOUR_USERNAME` with your GitHub username.

### Windows — PowerShell

```powershell
git clone https://github.com/YOUR_USERNAME/nuclei-scanner.git
cd nuclei-scanner
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### macOS — Terminal

```bash
git clone https://github.com/YOUR_USERNAME/nuclei-scanner.git
cd nuclei-scanner
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
```

You need to do this setup only once per local project copy.

## 3. Start the practice website

Open **Terminal 1** in the `nuclei-scanner` folder and leave it running.

**Windows (PowerShell)**

```powershell
.\.venv\Scripts\python.exe -m http.server 8000 --bind 127.0.0.1
```

**macOS (Terminal)**

```bash
./.venv/bin/python -m http.server 8000 --bind 127.0.0.1
```

The practice website is now available at **http://127.0.0.1:8000**.

## 4. Run the scanner

Open **Terminal 2** in the **same** `nuclei-scanner` folder. Keep Terminal 1 running.

**Windows (PowerShell)**

```powershell
.\.venv\Scripts\python.exe app.py
```

**macOS (Terminal)**

```bash
./.venv/bin/python app.py
```

Open **http://127.0.0.1:10000** in your browser. Enter **http://127.0.0.1:8000** and select **Scan**.

Review the findings. To stop the application, press `Ctrl+C` in each terminal.

## 5. Understand what the scanner does

1. The browser sends the target URL to Flask.
2. Flask checks that it is an authorized laboratory target.
3. Nuclei uses the included YAML template to inspect the HTTP response.
4. Nuclei writes findings to `results/` as JSONL.
5. Flask shows the findings in the browser.

The template checks for four common headers: `X-Content-Type-Options`, `Content-Security-Policy`, `X-Frame-Options`, and `Referrer-Policy`.

**Interpret results carefully:** a missing header does not always indicate a vulnerability, and no findings do not prove that a website is secure. Scanner errors are displayed separately.

## 6. Assignment

1. Run the local practice website and scanner; take screenshots showing that both work.
2. Explain the browser → Flask → Nuclei template → JSONL → results process.
3. Identify one limitation and implement **one improvement**, such as a severity summary, scan history, JSONL download, or clearer validation messages.
4. Test your improvement with a normal case **and** a failure case. Explain what changed.
5. Submit your fork URL, relevant screenshots or sanitized logs, and a **1–2 page report** describing the architecture, changes, tests, and one difficulty you resolved.

### Example marking rubric (10 points)

| Criterion | Points |
| --- | ---: |
| Correct local setup | 2 |
| Explanation of how the application works | 2 |
| Individual improvement | 2.5 |
| Testing and evidence | 2 |
| Report and responsible testing | 1.5 |
| **Total** | **10** |

This example rubric does not replace the official course assessment rules.

## Troubleshooting

- **Python or Nuclei command not found:** verify the installation and check `PATH`.
- **Target not authorized:** use `http://127.0.0.1:8000` as instructed.
- **Cannot open the scanner page:** check that Terminal 2 is still running.
- **Port already in use:** stop another process using that port.
- **Scanner error:** read the error displayed in your browser.

To run the included automated checks from your project folder:

**Windows**

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

**macOS**

```bash
./.venv/bin/python -m unittest discover -s tests -v
```

Keep this application on your own computer. Do not expose it publicly or include passwords, private data, or unauthorized scan results in your submission.
