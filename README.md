# Nuclei Scanner — Docker-Free Local Lab

A classroom Flask application calling the **native ProjectDiscovery Nuclei CLI** with one fixed, bundled HTTP security-header template. Results are saved as JSONL and displayed in the web browser. **Docker, a Go compiler, and the full Nuclei template catalog are not required.**

This is not a production vulnerability scanner. Only scan systems you own or are explicitly authorized to test.

## Requirements

- Python 3.10+ and Git (or download the GitHub ZIP)
- The [ProjectDiscovery Nuclei executable](https://github.com/projectdiscovery/nuclei/releases), installed on `PATH`. On Windows, extract `nuclei.exe` from the Windows ZIP and add its directory to `PATH`. On Linux/macOS, follow the [official installation guide](https://docs.projectdiscovery.io/tools/nuclei/install).
- Verify the executable via `nuclei -version`. Do **not** install the unrelated Python package `nuclei`. You do not need `nuclei -ut`: a minimal YAML template is bundled.

## Windows PowerShell (fresh student installation)

```powershell
git clone https://github.com/RafikHamza/nuclei-scanner.git
cd nuclei-scanner
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
nuclei -version
```

Terminal 1: Start your authorized local test website.

```powershell
.\.venv\Scripts\python.exe -m http.server 8000 --bind 127.0.0.1
```

Terminal 2: Run the scanner.

```powershell
.\.venv\Scripts\python.exe app.py
```

Open **http://127.0.0.1:10000** and scan **http://127.0.0.1:8000**. Stop both terminals with Ctrl+C.

## Linux/macOS (fresh student installation)

```bash
git clone https://github.com/RafikHamza/nuclei-scanner.git
cd nuclei-scanner
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
nuclei -version
```

In terminal 1:

```bash
./.venv/bin/python -m http.server 8000 --bind 127.0.0.1
```

In terminal 2:

```bash
./.venv/bin/python app.py
```

Visit **http://127.0.0.1:10000** and scan **http://127.0.0.1:8000**.

## Architecture and safety

Browser form → Flask `/scan` → exact-origin allowlist → native Nuclei CLI → fixed YAML header template → `results/*.jsonl` → HTML table.

The template performs a single GET with redirects disabled. It identifies four commonly missing response headers, for educational purposes only. No matches **does not imply security**. A scanner failure is reported separately.

The scanner listens on **127.0.0.1:10000** only. By default, the only allowed scanning origins are `http://127.0.0.1:8000` and `http://localhost:8000`. Only with explicit authorization may you set `ALLOWED_ORIGINS` to a comma-separated list of exact origins (e.g. `http://127.0.0.1:8000,http://192.0.2.10:8080`). If Nuclei is not on PATH, set `NUCLEI_BIN` to the executable path.

**Security limitation:** Native execution is lighter but has less process isolation than Docker. Keep this lab local, do not expose the web app, and do not load arbitrary external templates. The allowlist is a teaching safeguard, not complete protection against malicious target services.

## Tests and troubleshooting

Run unit tests (no external network requests):

```bash
python -m unittest discover -s tests -v
```

Tests cover URL blocking, normal/empty JSONL, missing executable, nonzero exit, timeout, and invalid output. An actual end-to-end test requires Nuclei and the local practice website started as above.

- **Nuclei not found:** verify `nuclei -version` in the same shell and check `PATH` or `NUCLEI_BIN`.
- **Target not authorized:** use the default lab target or configure an explicitly permitted origin.
- **Scanner error:** inspect the error; it must not be interpreted as a clean scan.
- **No matches:** not proof of safety.

## Student assignment (10-point example rubric)

1. Fork/clone; install native Nuclei and Python, without Docker.
2. Start the local test website and Flask interface, then scan only your authorized lab target.
3. Explain browser → Flask → template → JSONL → results.
4. Implement one improvement, such as severity summaries, scan history, JSONL download, or validation.
5. Compare normal and error test cases before/after your improvement.
6. Submit a fork link, screenshots of the scanner and terminals, sanitized evidence, and a 1–2 page report.

| Criterion | Points |
| --- | ---: |
| Reproducible native setup | 2 |
| Architecture explanation | 2 |
| Individual improvement | 2.5 |
| Testing and evidence | 2 |
| Report and responsible practice | 1.5 |
| **Total** | **10** |

Never publish passwords, tokens, private target data, or unauthorized scan results.
