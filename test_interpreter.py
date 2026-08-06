import sys
from pathlib import Path

sys.path.insert(
    0,
    str(
        Path(__file__).parent
        / "src"
        / "automind"
    ),
)

from conversation.interpreter import ConversationInterpreter

conversation = [

    {
        "role": "assistant",
        "content":
        "How many kilometers do you drive every year?"
    },

    {
        "role": "user",
        "content":
        "10000"
    }

]

interpreter = ConversationInterpreter()

result = interpreter.interpret(
    conversation
)

print(result)