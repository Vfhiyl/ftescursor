"""Shared HTTP helpers with polite retries."""

from __future__ import annotations

import json
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Mapping, MutableMapping, Optional


def build_ua(mailto: str) -> str:
    from .config import USER_AGENT_TEMPLATE

    return USER_AGENT_TEMPLATE.format(mailto=mailto)


def fetch_bytes(
    url: str,
    *,
    mailto: str,
    headers: Optional[Mapping[str, str]] = None,
    timeout: float = 60.0,
    retries: int = 3,
    sleep_s: float = 0.8,
) -> bytes:
    hdrs: MutableMapping[str, str] = {"User-Agent": build_ua(mailto)}
    if headers:
        hdrs.update(headers)
    ctx = ssl.create_default_context()
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=dict(hdrs))
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                return resp.read()
        except urllib.error.HTTPError as exc:
            last_err = exc
            # Retry rate limits / transient server errors.
            if exc.code in {429, 500, 502, 503, 504} and attempt + 1 < retries:
                time.sleep(sleep_s * (attempt + 1) * 2)
                continue
            raise
        except Exception as exc:  # noqa: BLE001 - network surface is broad
            last_err = exc
            if attempt + 1 < retries:
                time.sleep(sleep_s * (attempt + 1))
                continue
            raise
    assert last_err is not None
    raise last_err


def fetch_text(
    url: str,
    *,
    mailto: str,
    headers: Optional[Mapping[str, str]] = None,
    timeout: float = 60.0,
    retries: int = 3,
    encoding: str = "utf-8",
) -> str:
    return fetch_bytes(
        url, mailto=mailto, headers=headers, timeout=timeout, retries=retries
    ).decode(encoding, errors="replace")


def fetch_json(
    url: str,
    *,
    mailto: str,
    headers: Optional[Mapping[str, str]] = None,
    timeout: float = 60.0,
    retries: int = 3,
) -> object:
    text = fetch_text(
        url, mailto=mailto, headers=headers, timeout=timeout, retries=retries
    )
    return json.loads(text)


def post_json(
    url: str,
    payload: Mapping[str, object] | list[object],
    *,
    mailto: str,
    headers: Optional[Mapping[str, str]] = None,
    timeout: float = 60.0,
    retries: int = 3,
    sleep_s: float = 0.8,
) -> object:
    """POST JSON body and parse JSON response."""
    hdrs: MutableMapping[str, str] = {
        "User-Agent": build_ua(mailto),
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if headers:
        hdrs.update(headers)
    data = json.dumps(payload).encode("utf-8")
    ctx = ssl.create_default_context()
    last_err: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url, data=data, headers=dict(hdrs), method="POST"
            )
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
                return json.loads(resp.read().decode("utf-8", errors="replace"))
        except urllib.error.HTTPError as exc:
            last_err = exc
            if exc.code in {429, 500, 502, 503, 504} and attempt + 1 < retries:
                time.sleep(sleep_s * (attempt + 1) * 2)
                continue
            raise
        except Exception as exc:  # noqa: BLE001
            last_err = exc
            if attempt + 1 < retries:
                time.sleep(sleep_s * (attempt + 1))
                continue
            raise
    assert last_err is not None
    raise last_err


def url_with_query(base: str, params: Mapping[str, object]) -> str:
    q = urllib.parse.urlencode(
        {k: str(v) for k, v in params.items() if v is not None},
        safe=":|[],",
    )
    sep = "&" if "?" in base else "?"
    return f"{base}{sep}{q}"
