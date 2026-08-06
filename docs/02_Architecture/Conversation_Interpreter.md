## Output Contract

The Conversation Interpreter always returns a structured response.

```json
{
    "success": true,
    "confidence": 0.98,
    "updates": [
        {
            "field": "annual_running",
            "value": 10000
        }
    ]
}
```

### success

Indicates whether the interpreter was able to confidently understand the customer's response.

### confidence

A value between 0.0 and 1.0 representing the confidence of the interpretation.

### updates

One or more structured customer profile updates.

Each update contains:

- field
- value
```