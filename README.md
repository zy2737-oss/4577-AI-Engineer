# 4577 AI Engineering — Team Repository

Columbia IEOR E4577 section 005, 2026.

Project topic and proposal: pending team agreement.

## Week 1 setup

Prerequisites: Python 3.11+, Git, Google Cloud CLI, and access to the course Google Cloud project and credits.

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

For the exact dependency versions verified on the setup Mac, install `requirements.lock.txt` instead of `requirements.txt`.

On this Mac, Python 3.11 is also available at `/Users/jerryyan/miniconda3/bin/python`.
The local Google Cloud CLI is installed under `.tools/google-cloud-sdk` (ignored by Git).
On other machines, follow [Google's CLI installation instructions](https://cloud.google.com/sdk/docs/install).

From the repository root, activate both Python and the local CLI:

```bash
source scripts/activate.sh
gcloud --version
```

Redeem the **course** credits using the instructor's link. Then fill in `.env` with your actual course Project ID, region, and a Gemini model ID available in that project. Do not commit `.env` or credentials.

Authenticate in the browser with the account that has access to the course project:

```bash
gcloud auth login
gcloud auth application-default login
```

Replace `YOUR-PROJECT-ID` below with that same course Project ID:

```bash
gcloud config set project YOUR-PROJECT-ID
gcloud services enable aiplatform.googleapis.com --project YOUR-PROJECT-ID
gcloud auth application-default set-quota-project YOUR-PROJECT-ID
python 01-introduction-to-ai-engineering/test_setup.py --check-only
python 01-introduction-to-ai-engineering/test_setup.py
```

The final command makes a **real, potentially billable API request**. Week 1 model access passes only when it prints a nonempty model response followed by `PASS`. The local check alone does not verify API enablement, billing, permissions, model availability, or live inference.

## Status (2026-11-07)

- Team repository created. Collaborators include `ciro-greco`, `thevoid12`, `mike10wu`, `tianazeng`, and `zy2737-oss` (verified through GitHub).
- Local setup verification is documented in [docs/week1-status.md](docs/week1-status.md).
- Course credits, project selection, browser authentication, Vertex AI enablement, and a real model response remain unverified.

## Provenance

Requirements come from the [2026 course syllabus](https://github.com/ciro-greco/AI-engineering-and-applications-IEORE4577-005/blob/main/SYLLABUS-2026.md).
At inspection on 2026-11-07, the official Week 1 directory contained only a lecture PDF; the README and `test_setup.py` referenced by the syllabus were absent.
This repository's requirements, activation helper, and smoke-check script are team setup files, not copies of instructor-provided code.
The smoke check follows the [Google Gen AI SDK](https://github.com/googleapis/python-genai) client interface.
