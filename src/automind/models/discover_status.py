from dataclasses import dataclass


@dataclass
class DiscoverStatus:
    """
    Represents the outcome of the
    Discover phase.
    """

    completed: bool

    ready_for_define: bool

    completion_percentage: int

    missing_critical: int

    missing_important: int