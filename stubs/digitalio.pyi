import Pull
import digitalio
import microcontroller
from typing import Any

"""
digitalio
"""


# shared-bindings/digitalio/DigitalInOut.c:56
class DigitalInOut:
    def __init__(self, pin: microcontroller.Pin): ...
    def deinit(self, ) -> Any: ...
    def __enter__(self, ) -> Any: ...
    def __exit__(self, ) -> Any: ...
    def switch_to_output(self, value: bool = False, drive_mode: digitalio.DriveMode = digitalio.DriveMode.PUSH_PULL) -> Any: ...
    def switch_to_input(self, pull: Pull = None) -> Any: ...
    direction: Any = ...
    value: Any = ...
    drive_mode: Any = ...
    pull: Any = ...

# shared-bindings/digitalio/Pull.c:34
class Pull:
    def __init__(self, ): ...
    UP: Any = ...
    DOWN: Any = ...

# shared-bindings/digitalio/Direction.c:46
class Direction:
    def __init__(self, ): ...
    INPUT: Any = ...
    OUTPUT: Any = ...

# shared-bindings/digitalio/DriveMode.c:34
class DriveMode:
    def __init__(self, ): ...
    PUSH_PULL: Any = ...
    OPEN_DRAIN: Any = ...
