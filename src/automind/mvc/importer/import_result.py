from dataclasses import (
    dataclass,
    field,
)


@dataclass
class ImportResult:
    """
    Summary of an import
    execution.
    """

    provider_name: str

    total_records: int = 0

    imported_records: int = 0

    updated_records: int = 0

    skipped_records: int = 0

    failed_records: int = 0

    created_makes: int = 0

    created_models: int = 0

    created_generations: int = 0

    created_variants: int = 0

    errors: list[str] = field(
        default_factory=list,
    )

    warnings: list[str] = field(
        default_factory=list,
    )

    def success(
        self,
    ) -> bool:

        return (
            self.failed_records
            == 0
        )