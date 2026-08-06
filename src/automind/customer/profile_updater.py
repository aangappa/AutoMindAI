from customer.customer_profile import CustomerProfile
from models.conversation_update import ConversationUpdate


class ProfileUpdater:
    """
    Applies structured profile updates
    to the Customer Profile.
    """

    def apply(
        self,
        profile: CustomerProfile,
        updates: list[ConversationUpdate],
    ):

        for update in updates:

            setattr(
                profile,
                update.field,
                update.value,
            )