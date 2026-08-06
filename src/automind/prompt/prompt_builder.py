from pathlib import Path


class PromptBuilder:
    """
    Loads a prompt template and replaces placeholders
    with runtime values.
    """

    @staticmethod
    def build(
        prompt_name: str,
        variables: dict | None = None,
    ) -> str:

        prompt_path = (
            Path(__file__).parent.parent
            / "prompts"
            / prompt_name
        )

        with open(
            prompt_path,
            "r",
            encoding="utf-8",
        ) as file:

            prompt = file.read()

        if variables:

            for key, value in variables.items():

                placeholder = "{{" + key + "}}"

                prompt = prompt.replace(
                    placeholder,
                    str(value),
                )

        return prompt