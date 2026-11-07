"""Team-authored Week 1 smoke check; not the instructor's missing script.

Default: one real Vertex AI request. --check-only never calls a model.
"""

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types
import google.auth
from google.auth.exceptions import DefaultCredentialsError


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    load_dotenv(root / '.env', override=False)
    if sys.version_info < (3, 11):
        print('FAIL: Python 3.11+ required.', file=sys.stderr)
        return 1
    print(f'Python: {sys.version.split()[0]} | SDK import: OK', flush=True)
    settings = {key: os.getenv(key, '').strip() for key in (
        'GOOGLE_CLOUD_PROJECT', 'GOOGLE_CLOUD_LOCATION', 'GOOGLE_CLOUD_MODEL'
    )}
    missing = [key for key, value in settings.items() if not value]
    if missing:
        print('PENDING: set ' + ', '.join(missing) + ' in .env.', file=sys.stderr)
        return 1
    try:
        google.auth.default(scopes=['https://www.googleapis.com/auth/cloud-platform'])
    except DefaultCredentialsError:
        print('PENDING: run gcloud auth application-default login.', file=sys.stderr)
        return 1
    if args.check_only:
        print('Local configuration and credentials found. No API call made; live access unverified.')
        return 0
    print('Making a real Vertex AI model request...', flush=True)
    try:
        with genai.Client(
            vertexai=True,
            project=settings['GOOGLE_CLOUD_PROJECT'],
            location=settings['GOOGLE_CLOUD_LOCATION'],
            http_options=types.HttpOptions(api_version='v1', timeout=60000),
        ) as client:
            response = client.models.generate_content(
                model=settings['GOOGLE_CLOUD_MODEL'],
                contents='Say hello to our AI engineering class in one short sentence.',
                config=types.GenerateContentConfig(max_output_tokens=256),
            )
        if not response.text or not response.text.strip():
            print('FAIL: no text response received.', file=sys.stderr)
            return 1
        print(response.text)
        print('PASS: real model response received.')
        return 0
    except Exception as exc:
        print(f'FAIL: {type(exc).__name__}: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
