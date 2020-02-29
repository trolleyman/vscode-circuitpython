import microcontroller
from typing import Any

"""
microcontroller
"""


# shared-bindings/microcontroller/Pin.c:43
class Pin:
    def __init__(self, ): ...
    cpu: Any = ...

# shared-bindings/microcontroller/__init__.c:72
def delay_us(delay: Any) -> Any: ...

# shared-bindings/microcontroller/__init__.c:90
def disable_interrupts() -> Any: ...

# shared-bindings/microcontroller/__init__.c:100
def enable_interrupts() -> Any: ...

# shared-bindings/microcontroller/__init__.c:110
def on_next_reset(run_mode: microcontroller.RunMode) -> Any: ...

# shared-bindings/microcontroller/__init__.c:135
def reset() -> Any: ...
    nvm: Any = ...

# shared-bindings/microcontroller/RunMode.c:34
class RunMode:
    def __init__(self, ): ...
    NORMAL: Any = ...
    SAFE_MODE: Any = ...
    BOOTLOADER: Any = ...

# shared-bindings/microcontroller/Processor.c:51
class Processor:
    def __init__(self, ): ...
    frequency: Any = ...
    temperature: Any = ...
    uid: Any = ...
    voltage: Any = ...
