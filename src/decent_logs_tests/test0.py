from decent_logs import WithInternalLog


class A(WithInternalLog):
    def go(self) -> None:
        self.debug("Hello")


def test1() -> None:
    a = A()
    a.go()
