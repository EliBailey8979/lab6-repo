from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig


def sample_run_anonymizer(text: str, start: int, end: int):
    """Run the anonymizer on the given text and return the result."""
    # Initialize the engine
    engine = AnonymizerEngine()

    # Invoke the anonymize function with the text,
    # analyzer results (potentially coming from presidio-analyzer) and
    # Operators to get the anonymization output:
    result = engine.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(
                entity_type="PERSON",
                start=start,
                end=end,
                score=0.8,
            )
        ],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})},
    )

    # Print for the CLI example
    print(result)

    # Return so tests can assert on it
    return result


if __name__ == "__main__":
    # Example values from the assignment
    example_text = "My name is Bond."
    example_start = 11
    example_end = 15

    anonymization_result = sample_run_anonymizer(
        example_text, example_start, example_end
    )