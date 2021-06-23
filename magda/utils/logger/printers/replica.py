from __future__ import annotations
from typing import Optional

from colorama import Fore, Style

from magda.utils.logger.parts import LoggerParts
from .base import BasePrinter


class ReplicaPrinter(BasePrinter):
    def _with_colors(self, text: str) -> str:
        return (
            Fore.CYAN + Style.BRIGHT
            + text
            + Fore.RESET + Style.NORMAL
        )

    def flush(
        self,
        colors: bool,
        group: Optional[LoggerParts.Group] = None,
        **kwargs,
    ) -> Optional[str]:
        if group is not None and group.replica is not None:
            text = f'({group.replica})'
            return self._with_colors(text) if colors else text
        return None
