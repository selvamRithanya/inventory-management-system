import requests  # type: ignore[import-not-found]
import time


def send_request(url, method, payload=None):

    try:
        start_time = time.time()

        if method == "GET":
            response = requests.get(url, timeout=10)

        elif method == "POST":
            response = requests.post(
                url,
                json=payload,
                timeout=10
            )

        else:
            return {
                "error": "Unsupported HTTP method"
            }

        end_time = time.time()

        try:
            response_data = response.json()
        except ValueError:
            response_data = response.text

        return {
            "status_code": response.status_code,
            "response_time": round(end_time - start_time, 3),
            "headers": dict(response.headers),
            "response": response_data
        }

    except requests.exceptions.RequestException as e:

        return {
            "error": str(e)
        }