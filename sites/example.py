from sites.base import SiteAdapter


class ExampleSite(SiteAdapter):
    def run(self) -> None:
        print(
            "예제 사이트 어댑터입니다. "
            "sites/example.py에 사이트 주소와 예약 절차를 구현하세요."
        )
