# 예약 자동화

사이트별 예약 절차는 `sites/` 아래에 각각 구현하고, 여러 사이트에서
공통으로 쓰는 브라우저 기능은 `common/`에 둡니다. `index.py`에서
실행할 사이트 어댑터를 선택합니다.

## 실행

```powershell
python index.py
```

현재 `example` 어댑터는 구조 확인용 예제입니다. 실제 예약 동작을 위해서는
`sites/example.py`에 해당 사이트의 URL과 예약 절차를 구현해야 합니다.

## Playwright 설치

```powershell
pip install -r requirements.txt
playwright install chromium
```

공통 브라우저 기능은 `common.browser.browser_page(url)`을 사용합니다.
기본적으로 브라우저 화면은 숨겨져 있으며, 화면을 보면서 실행하려면
`browser_page(url, headless=False)`로 호출하세요.
