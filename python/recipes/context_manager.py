from typing import BaseException, Optional, TracebackType, Type


class Foo:
    def __init__(self) -> None:
        pass

    def __enter__(self) -> "Foo":
        return self
    
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], traceback: Optional[TracebackType]) -> None:
        pass

class SMTPConnection:
    def __init__(self) -> None:
        pass

    async def __aenter__(self):
        pass

    async def __aexit__(
        self,
        exctype: Optional[Type[BaseException]],
        excinst: Optional[BaseException],
        exctb: Optional[TracebackType],
    ) -> bool:
        pass
