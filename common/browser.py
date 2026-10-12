from contextlib import contextmanager
from typing import Iterator


@contextmanager
def browser_page(url: str, headless: bool = True) -> Iterator[object]:
    """Playwright 브라우저를 열고 페이지를 제공한다."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as error:
        raise RuntimeError(
            "Playwright가 설치되지 않았습니다. "
            "'pip install -r requirements.txt'와 "
            "'playwright install chromium'을 실행하세요."
        ) from error

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless)
        try:
            page = browser.new_page()
            page.goto(url)
            yield page
        finally:
            browser.close()
