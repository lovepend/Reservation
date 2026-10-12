import argparse

from sites.example import ExampleSite


SITES = {
    "example": ExampleSite,
}


def main() -> None:
    parser = argparse.ArgumentParser(description="사이트별 예약 자동화 실행기")
    parser.add_argument(
        "--site",
        choices=sorted(SITES),
        default="example",
        help="실행할 사이트 어댑터",
    )
    args = parser.parse_args()

    site = SITES[args.site]()
    site.run()


if __name__ == "__main__":
    main()