# Nuclei Scanner — Local Docker Lab

A small Flask application that runs a Nuclei security-header check and displays the findings in a web page. This repository is the starter for a cybersecurity assignment.

## How the starter works

The web form in `templates/index.html` sends a target URL to the Flask `/scan` endpoint in `app.py`. Flask launches Nuclei with a fixed missing-security-headers template, writes JSONL results under `results/`, and renders findings in the web page. The container starts Gunicorn on port 10000.

**Note:** The current code does not enforce an authorized-target allowlist or distinguish every scan failure from a scan with no findings. Students should identify these limitations. The template path in `app.py` also depends on the template being present in the container. This starter has not been presented as a verified production scanner.

## Assignment: Build and evaluate a local vulnerability-scanning application

**Aim:** Understand how a Python web service, Docker and Nuclei work together, then make one small, testable improvement.

1. **Fork and clone** [this repository](https://github.com/RafikHamza/nuclei-scanner).
2. **Build the Docker image** from your fork:
   ```bash
   docker build -t nuclei-scanner-student .
   ```
3. **Run it locally** (not as a public web service):
   ```bash
   docker run --rm -p 127.0.0.1:10000:10000 nuclei-scanner-student
   ```
   Open `http://localhost:10000`.
4. **Test only an explicitly authorized laboratory target.** Record what happens. Check the container logs and the Nuclei messages if the scan fails. Do not scan third-party websites without permission.
5. **Explain the data flow:** browser form → Flask → Nuclei template → JSONL output → findings table. Identify one limitation in the starter.
6. **Add one improvement** of your own. Examples: validate/allowlist targets; distinguish scanner errors from an empty result; summarize findings by severity; provide a scan-history view; or offer a JSONL download. Do not remove the permission requirement.
7. **Test before and after your change.** Show the result of a normal case and a failure case, and explain what the evidence shows.

### Submit

- Link to your fork with the modified source and a brief README describing your contribution.
- Screenshot of the running Docker container and the application at `localhost:10000`.
- Evidence of a normal test and an error/failure test (screenshots or short, sanitized logs).
- **1–2 page report:** architecture, tools used, how Docker/Flask/Nuclei are connected, your improvement, test results, one difficulty and how you resolved it.

Never include passwords, tokens, private customer information, or unauthorized scan targets in the submission.

### Marking rubric (10 points)

| Criterion | Points | What is evaluated |
|---|---:|---|
| Local setup | 2 | Fork, Docker build, local service, reproducible commands |
| System understanding | 2 | Accurate explanation of Flask, Nuclei, template, JSONL and web output |
| Individual improvement | 2.5 | Useful implementation with clear rationale and readable code |
| Testing and evidence | 2 | Normal and failure cases, evidence linked to conclusions |
| Report and responsible practice | 1.5 | Clear 1–2 page report, honest limitations, authorized-target testing |
| **Total** | **10** | |

The rubric is a **sample marking scheme for this teaching material**; it does not replace the course-level assessment weights in the official syllabus.
