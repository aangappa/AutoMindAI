from customer.profile_extractor import ProfileExtractor


class ConsultationEngine:

    def __init__(self):
        self.extractor = ProfileExtractor()

    def process_message(self, prompt: str, profile) -> str:

        self.extractor.extract(prompt, profile)

        return (
            "Thank you! I've started understanding your requirements.\n\n"
            "We'll continue building your automotive profile before recommending a vehicle."
        )