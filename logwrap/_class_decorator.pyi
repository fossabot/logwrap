import abc
import typing

PY3: bool

class BaseDecorator:
    def __init__(self, func: typing.Optional[typing.Callable]=...) -> None: ...

    @property
    def _func(self) -> typing.Optional[typing.Callable]: ...

    @abc.abstractmethod
    def _get_function_wrapper(self, func: typing.Callable) -> typing.Callable: ...

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any: ...
