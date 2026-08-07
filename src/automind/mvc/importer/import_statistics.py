from dataclasses import (
    dataclass,
)


@dataclass
class ImportStatistics:
    """
    Runtime statistics for an
    import execution.
    """

    total_rows: int = 0

    processed_rows: int = 0

    skipped_rows: int = 0

    failed_rows: int = 0

    created_makes: int = 0

    created_models: int = 0

    created_generations: int = 0

    created_variants: int = 0

    matched_makes: int = 0

    matched_models: int = 0

    matched_generations: int = 0

    matched_variants: int = 0

    provider_links_created: int = 0

    raw_payloads_saved: int = 0

    def reset(
        self,
    ) -> None:

        self.total_rows = 0

        self.processed_rows = 0

        self.skipped_rows = 0

        self.failed_rows = 0

        self.created_makes = 0

        self.created_models = 0

        self.created_generations = 0

        self.created_variants = 0

        self.matched_makes = 0

        self.matched_models = 0

        self.matched_generations = 0

        self.matched_variants = 0

        self.provider_links_created = 0

        self.raw_payloads_saved = 0