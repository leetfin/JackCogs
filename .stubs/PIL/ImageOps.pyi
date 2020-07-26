"""
This an incomplete stub of pillow library for use of cogs in this repo.
Nobody have made a full stub for this library so only stuff used by this repo is typed.

---

Copyright 2018-2020 Jakub Kuczys (https://github.com/jack1142)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from typing import Tuple
from . import Image

XY = Tuple[int, int]
Coord = XY
Size = XY

def fit(
    image: Image.Image,
    size: Size,
    method: int = ...,
    bleed: float = ...,
    centering: Tuple[float, float] = ...,
) -> Image.Image: ...