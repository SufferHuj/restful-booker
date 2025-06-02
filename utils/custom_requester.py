import json
import logging
import os
import requests

class CustomRequester:
    def __init__(self, base_url, session=None):
        self.base_url = base_url.rstrip("/")
        self.session = session or requests.Session()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

        if not self.logger.handlers:
            handler = logging.StreamHandler()
            self.logger.addHandler(handler)

    def send(self, method, endpoint, headers=None, data=None, expected_status=200, log=True):
        url = f"{self.base_url}{endpoint}"
        headers = headers or {}
        json_data = data

        response = self.session.request(method, url, headers=headers, json=json_data)

        if log:
            self._log(response)

        if response.status_code != expected_status:
            raise AssertionError(
                f"Expected {expected_status}, got {response.status_code}: {response.text}"
            )

        return response

    def _log(self, response):
        try:
            request = response.request
            GREEN, RED, RESET = "\033[32m", "\033[31m", "\033[0m"

            curl_parts = [
                f"curl -X {request.method} '{request.url}'"
            ]
            for h, v in request.headers.items():
                curl_parts.append(f"-H '{h}: {v}'")
            if request.body:
                body = request.body.decode() if isinstance(request.body, bytes) else request.body
                curl_parts.append(f"-d '{body}'")

            full_test = os.environ.get('PYTEST_CURRENT_TEST', '').replace(' (call)', '')
            self.logger.info(f"\n{'=' * 30} REQUEST: {full_test} {'=' * 30}")
            self.logger.info(GREEN + " \\\n".join(curl_parts) + RESET)

            try:
                response_body = json.dumps(response.json(), indent=4, ensure_ascii=False)
            except Exception:
                response_body = response.text

            self.logger.info(f"{'=' * 30} RESPONSE {'=' * 30}")
            status_color = GREEN if response.ok else RED
            self.logger.info(f"Status: {status_color}{response.status_code}{RESET}")
            self.logger.info(f"Response:\n{response_body}")
            self.logger.info("=" * 80 + "\n")
        except Exception as e:
            self.logger.error(f"Logging failed: {e}")