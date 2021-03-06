.. logwrap function and LogWrap class description.

API: Decorators: `LogWrap` class and `logwrap` function.
========================================================

.. py:module:: logwrap
.. py:currentmodule:: logwrap

.. py:class:: LogWrap(object)

    Log function calls and return values.

    .. versionadded:: 2.2.0

    .. py:method:: __init__(func=None, *, log=logging.getLogger('logwrap'), log_level=logging.DEBUG, exc_level=logging.ERROR, max_indent=20, spec=None, blacklisted_names=None, blacklisted_exceptions=None, log_call_args=True, log_call_args_on_exc=True, log_result_obj=True, )

        :param func: function to wrap
        :type func: typing.Optional[typing.Callable]
        :param log: logger object for decorator, by default used 'logwrap'
        :type log: logging.Logger
        :param log_level: log level for successful calls
        :type log_level: int
        :param exc_level: log level for exception cases
        :type exc_level: int
        :param max_indent: maximum indent before classic `repr()` call.
        :type max_indent: int
        :param spec: callable object used as spec for arguments bind.
                     This is designed for the special cases only,
                     when impossible to change signature of target object,
                     but processed/redirected signature is accessible.
                     Note: this object should provide fully compatible
                     signature with decorated function, or arguments bind
                     will be failed!
        :type spec: typing.Optional[typing.Callable]
        :param blacklisted_names: Blacklisted argument names.
                                  Arguments with this names will be skipped in log.
        :type blacklisted_names: typing.Optional[typing.Iterable[str]]
        :param blacklisted_exceptions: list of exception,
                                       which should be re-raised without
                                       producing log record.
        :type blacklisted_exceptions: typing.Optional[typing.Iterable[typing.Type[Exception]]]
        :param log_call_args: log call arguments before executing wrapped function.
        :type log_call_args: bool
        :param log_call_args_on_exc: log call arguments if exception raised.
        :type log_call_args_on_exc: bool
        :param log_result_obj: log result of function call.
        :type log_result_obj: bool

        .. versionchanged:: 3.3.0 Extract func from log and do not use Union.
        .. versionchanged:: 3.3.0 Deprecation of `*args`
        .. versionchanged:: 4.0.0 Drop of *args

    .. py:method:: pre_process_param(self, arg)

        Process parameter for the future logging.

        :param arg: bound parameter
        :type arg: BoundParameter
        :return: value, value override for logging or None if argument should not be logged.
        :rtype: typing.Union[BoundParameter, typing.Tuple[BoundParameter, typing.Any], None]

        Override this method if some modifications required for parameter value before logging

        .. versionadded:: 3.3.0

    .. py:method:: post_process_param(self, arg, arg_repr)

        Process parameter for the future logging.

        :param arg: bound parameter
        :type arg: BoundParameter
        :param arg_repr: repr for value
        :type arg_repr: typing.Text
        :return: processed repr for value
        :rtype: typing.Text

        Override this method if some modifications required for result of repr() over parameter

        .. versionadded:: 3.3.0

    .. note:: Attributes/properties names the same as argument names and changes
              the same fields.

    .. py:attribute:: log_level
    .. py:attribute:: exc_level
    .. py:attribute:: max_indent
    .. py:attribute:: blacklisted_names

        ``typing.List[str]``, modified via mutability
    .. py:attribute:: blacklisted_exceptions

        ``typing.List[typing.Type[Exception]]``, modified via mutability
    .. py:attribute:: log_call_args
    .. py:attribute:: log_call_args_on_exc
    .. py:attribute:: log_result_obj

    .. py:attribute:: _func

        ``typing.Optional[typing.Callable[..., typing.Awaitable]]``
        Wrapped function. Used for inheritance only.

    .. py:method:: __call__(*args, **kwargs)

        Decorator entry-point. Logic is stored separately and load depends on python version.

        :returns: Decorated function. On python 3.3+ awaitable is supported.
        :rtype: typing.Union[typing.Callable, typing.Awaitable]


.. py:class:: BoundParameter(object)

    Parameter-like object store BOUND with value parameter.

    .. versionadded:: 3.3.0

    .. py:method:: __init__(self, parameter, value=Parameter.empty)

        Parameter-like object store BOUND with value parameter.

        :param parameter: parameter from signature
        :type parameter: ``inspect.Parameter``
        :param value: parameter real value
        :type value: typing.Any
        :raises ValueError: No default value and no value

    .. py:attribute:: POSITIONAL_ONLY

        ``enum.IntEnum``
        Parameter.POSITIONAL_ONLY

    .. py:attribute:: POSITIONAL_OR_KEYWORD

        ``enum.IntEnum``
        Parameter.POSITIONAL_OR_KEYWORD

    .. py:attribute:: VAR_POSITIONAL

        ``enum.IntEnum``
        Parameter.VAR_POSITIONAL

    .. py:attribute:: KEYWORD_ONLY

        ``enum.IntEnum``
        Parameter.KEYWORD_ONLY

    .. py:attribute:: VAR_KEYWORD

        ``enum.IntEnum``
        Parameter.VAR_KEYWORD

    .. py:attribute:: empty

        ``typing.Type``
        Parameter.empty

    .. py:attribute:: parameter

        Parameter object.

        :rtype: inspect.Parameter

    .. py:attribute:: name

        Parameter name.

        :rtype: typing.Union[None, str]

    .. py:attribute:: default

        Parameter default value.

        :rtype: typing.Any

    .. py:attribute:: annotation

        Parameter annotation.

        :rtype: typing.Union[Parameter.empty, str]

    .. py:attribute:: kind

        Parameter kind.

        :rtype: enum.IntEnum

    .. py:attribute:: value

        Parameter value.

        :rtype: typing.Any

    .. py:method:: __hash__(self)

        Block hashing.

        :raises TypeError: Not hashable.


.. py:function:: bind_args_kwargs(sig, *args, **kwargs)

    Bind `*args` and `**kwargs` to signature and get Bound Parameters.

    :param sig: source signature
    :type sig: inspect.Signature
    :return: Iterator for bound parameters with all information about it
    :rtype: typing.Iterator[BoundParameter]

    .. versionadded:: 3.3.0
