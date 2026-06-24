from flask import Flask, request, render_template
import subprocess, os, time, json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    target = request.form["target"]

    os.makedirs("results", exist_ok=True)
    output_file = f"results/output_{int(time.time())}.jsonl"

    cmd = [
        "nuclei",
        "-u", target,
        "-j",
        "-o", output_file,
        "-severity", "critical,high",
        "-rl", "3",
        "-c", "3",
        "-silent",
        "-duc"
    ]

    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)

        if r.returncode != 0:
            return f"""
            <h2>Scan failed</h2>
            <pre>{r.stderr}</pre>
            <a href="/">Back</a>
            """

    except subprocess.TimeoutExpired:
        return "Scan timed out. Try another target or lower scan options."

    findings = []

    if os.path.exists(output_file):
        with open(output_file) as f:
            for line in f:
                if line.strip():
                    findings.append(json.loads(line))

    return render_template("index.html", findings=findings, target=target)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
