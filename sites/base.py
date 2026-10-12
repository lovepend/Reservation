from abc import ABC, abstractmethod


class SiteAdapter(ABC):
    """사이트별 예약 흐름이 구현할 기본 인터페이스."""

    @abstractmethod
    def run(self) -> None:
        """사이트의 예약 흐름을 실행한다."""
        raise NotImplementedError
