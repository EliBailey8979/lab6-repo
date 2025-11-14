import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    text = "My name is Bond."
    start = 11
    end = 15
    result = sample_run_anonymizer(text, start, end)
    assert result.text == "My name is BIP."

    assert isinstance(result.items, list)
    assert len(result.items) == 1

    item = result.items[0]

    assert item.start == 11
    assert item.end == 14
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"