from acf.discover import DiscoverMethodology
from consultation.consultation_context import (
    ConsultationContext,
)
from conversation.interpreter import (
    ConversationInterpreter,
)
from customer.profile_updater import (
    ProfileUpdater,
)
from define.define_methodology import (
    DefineMethodology,
)
from evaluate.evaluate_methodology import (
    EvaluateMethodology,
)


class ACFEngine:
    """
    Orchestrates the Automotive
    Consulting Framework.

    Discover
        ↓
    Define
        ↓
    Evaluate
    """

    def __init__(self):

        self.interpreter = (
            ConversationInterpreter()
        )

        self.profile_updater = (
            ProfileUpdater()
        )

        self.discover = (
            DiscoverMethodology()
        )

        self.define = (
            DefineMethodology()
        )

        self.evaluate = (
            EvaluateMethodology()
        )

    def process(
        self,
        context: ConsultationContext,
        fact_repository,
    ):

        result = self.interpreter.interpret(
            context=context,
        )

        if result.success:

            self.profile_updater.apply(

                context.customer_profile,

                result.updates,

            )

        context.customer_dna = (
            self.define.update_customer_dna(

                customer_profile=
                context.customer_profile,

                customer_dna=
                context.customer_dna,

                fact_repository=
                fact_repository,

                conversation_history=
                context.conversation_history,

            )
        )

        if self.discover.is_complete(

            context.customer_profile

        ):

            return self.evaluate.evaluate(

                context.customer_dna

            )

        return None