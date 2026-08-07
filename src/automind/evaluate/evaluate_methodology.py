from discovery.vehicle_discovery import (
    VehicleDiscovery,
)
from evaluate.vehicle_matcher import (
    VehicleMatcher,
)
from models.customer_dna import (
    CustomerDNA,
)
from models.evaluation_result import (
    EvaluationResult,
)
from mvc.catalog_loader import (
    CatalogLoader,
)
from mvc.vehicle_catalog import (
    MasterVehicleCatalog,
)


class EvaluateMethodology:
    """
    Implements the ACF Evaluate phase.

    Customer Profile
            ↓
    Catalog Loader
            ↓
    Vehicle Discovery
            ↓
    Vehicle Matcher
            ↓
    Evaluation Result
    """

    def __init__(self):

        self.catalog = (
            MasterVehicleCatalog()
        )

        self.loader = (
            CatalogLoader(
                self.catalog
            )
        )

        self.discovery = (
            VehicleDiscovery(
                self.catalog
            )
        )

        self.matcher = (
            VehicleMatcher()
        )

    def evaluate(
        self,
        customer_profile,
        customer_dna: CustomerDNA,
    ) -> EvaluationResult:

        # Temporary seed until AKR synchronization
        self.loader.load()

        candidates = (
            self.discovery.discover(
                customer_profile
            )
        )

        evaluations = (
            self.matcher.match(

                customer_dna,

                candidates,

            )
        )

        result = (
            EvaluationResult()
        )

        for evaluation in evaluations:

            result.add(
                evaluation
            )

        result.completed = True

        return result