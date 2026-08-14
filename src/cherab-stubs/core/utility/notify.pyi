from collections.abc import Callable, Iterable
from typing import SupportsIndex, TypeVar

_T = TypeVar("_T")
_Callback = Callable[[], object]

class Notifier:
    """
    Allows objects to broadcast notifications to observing objects.

    This object implements a version of the observer pattern. Objects wishing
    to be notified may register a callback function with the notifier. The
    callbacks will be called when the notify method of the Notifier is called.

    The primary purpose of this class is to permit cache control between
    disconnected objects. To speed up calculations, objects may cache the
    results of a calculation involving a source object. If the source object
    data changes, the caches of the dependent objects must be invalidated
    otherwise stale data may be used in subsequent calculations.

    Callbacks are assumed to have no arguments.

    This object holds weak references to callbacks. If an observing object has
    registered a method as a callback and that object is subsequently deleted,
    the callback will be automatically removed from the list of registered
    callbacks. The Notifier will not prevent referenced objects being garbage
    collected.
    """
    def __init__(self) -> None: ...
    def add(self, callback: _Callback) -> None: ...
    def remove(self, callback: _Callback) -> None: ...
    def is_present(self, callback: _Callback) -> bool: ...
    def notify(self) -> None: ...

class NotifyingList(list[_T]):
    """
    A list that reports changes to its contents.

    The NotifyingList class is a subclass of the builtin list type. It extends
    the list type to add a Notifier object that generates notifications
    whenever the list contents are modified. A notifier attribute is provided
    to supply access to configure the internal Notifier object.

    The NotifierList implements the entire list interface. Please note however
    that __add__ or __mul__ operations involving a NotifyingList will return
    a basic builtin list.
    """
    def __init__(self, iterable: Iterable[_T] = (), /) -> None: ...
    @property
    def notifier(self) -> Notifier: ...
    def append(self, p_object: _T) -> None: ...
    def insert(self, index: SupportsIndex, p_object: _T) -> None: ...
    def extend(self, iterable: Iterable[_T]) -> None: ...
    def pop(self, index: SupportsIndex = -1) -> _T: ...
    def remove(self, value: _T) -> None: ...
