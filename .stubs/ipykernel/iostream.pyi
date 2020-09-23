# Copyright 2018-2020 Jakub Kuczys (https://github.com/jack1142)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This an incomplete stub of ipykernel library for use of cogs in this repo.
Nobody have made a full stub for this library so only stuff used by this repo is typed.
"""

from io import TextIOBase
from typing import Optional

from jupyter_client.session import Session

class IOPubThread:
    def start(self) -> None: ...

class OutStream(TextIOBase):
    name: str
    def __init__(
        self,
        session: Session,
        pub_thread: Optional[IOPubThread],
        name: str,
        pipe: None = None,
        echo: Optional[TextIOBase] = None,
    ): ...
    def _flush(self) -> None: ...
    # not like I can control what upstream does...
    def write(self, string: str) -> None: ...  # type: ignore[override]