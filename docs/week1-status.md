# Week 1 setup verification — 2026-11-07

## Verified

- Cloned the team repository successfully; it was initially empty.
- Git 2.49.0 is installed.
- Created an isolated `.venv` with Python 3.11.5.
- Installed google-genai 3.0.0 and python-dotenv 1.2.4; captured all resolved versions in `requirements.lock.txt`.
- `python -m pip check`: no broken requirements.
- Installed Google Cloud CLI 592.0.0 in `.tools/google-cloud-sdk`; `gcloud --version` succeeds after sourcing `scripts/activate.sh`.
- Downloaded the Apple Silicon archive from Google's official distribution and verified SHA-256 against the installation documentation: `57553ae3c300f4ebaaa8fb4dee8d40c4d8c1141d84d266b41c1daf1669c4001a`.
- The local smoke check imports the SDK successfully and exits with a pending-configuration message when project/model settings are blank.
- GitHub collaborator lookup returned both instructors and the three listed team accounts. The owner also confirmed invitations were completed.

## Pending

- Owner confirms course credits redemption and provides the course Google Cloud Project ID.
- Browser authentication for both gcloud CLI and Application Default Credentials.
- Verify project access/billing, enable Vertex AI API, and select an available Gemini model.
- Run the script and receive a real model response.

No LLM inference was executed. All verification so far used local commands and read-only GitHub/Google documentation requests. Local package/configuration checks do not establish live Vertex AI access.

The official course Week 1 directory contained only a lecture PDF when inspected. The smoke-check script here was written for this repository according to the syllabus; it is not an instructor-provided artifact.
