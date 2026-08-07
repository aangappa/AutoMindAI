class ImportException(
    Exception,
):
    """
    Base exception for all
    AutoMind import errors.
    """

    pass


class ProviderException(
    ImportException,
):
    """
    Raised when a provider
    cannot supply data.
    """

    pass


class EntityMatchingException(
    ImportException,
):
    """
    Raised when canonical
    entity matching fails.
    """

    pass


class CanonicalImportException(
    ImportException,
):
    """
    Raised when canonical
    persistence fails.
    """

    pass


class ProviderMappingException(
    ImportException,
):
    """
    Raised when provider
    cross-reference creation
    fails.
    """

    pass