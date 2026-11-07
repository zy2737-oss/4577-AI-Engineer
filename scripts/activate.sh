# Run from the repository root: source scripts/activate.sh
if [ ! -f .venv/bin/activate ]; then
  echo 'Create .venv first; see README.md.'
  return 1
fi
source .venv/bin/activate
export CLOUDSDK_PYTHON="$VIRTUAL_ENV/bin/python"
if [ -d "$PWD/.tools/google-cloud-sdk/bin" ]; then
  export PATH="$PWD/.tools/google-cloud-sdk/bin:$PATH"
fi
# Keep project credentials local and ignored by Git.
export CLOUDSDK_CONFIG="$PWD/.gcloud"
export GOOGLE_APPLICATION_CREDENTIALS="$CLOUDSDK_CONFIG/application_default_credentials.json"
