import requests
from urllib.parse import urlparse


class RequestManager:
    def __init__(self, timeout: int = 5, max_size: int = 2000000):
        self.timeout = timeout
        self.max_size = max_size

    def fetch_html(self, url: str) -> dict:
        url = url.strip()

        # ---|url validation|--- #
        input_url_parsed = urlparse(url)

        if input_url_parsed.scheme not in ("http", "https"):
            return {"ok": False, "error": "URL Error: Invalid URL scheme"}
        if not input_url_parsed.netloc:
            return {"ok": False, "error": "URL Error: Missing domain"}
        
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

            response = requests.get(url, timeout=self.timeout, headers=headers, allow_redirects=True)

            # ---|check potential redirects|--- #
            if response.url != url:
                url_lower = response.url.lower()
                potential_redirects = ["/login", "/signin", "/auth", "/account", "/dashboard"]

                for redirect in potential_redirects:
                    if redirect in url_lower:
                        return {"ok": False, "error": "Redirected to a non public page"}

            # ---|check content type--- #
            content_type = response.headers.get("Content-Type", "").lower()
            if not ("text/html" in content_type or "application/xhtml+xml" in content_type):
                return {"ok": False, "error": f"Unsupported content type: {content_type}"}

            # ---|limit file size--- #
            content_length = response.headers.get("Content-Length")
            if content_length is not None:
                try:
                    size = int(content_length)
                    if size > self.max_size:
                        return {"ok": False, "error": "Response too large"}
                except ValueError:
                    pass

            # ---|return html--- #
            return {"ok": True, "html": response.text}
        except Exception as error:
            return {"ok": False, "error": str(error)}
