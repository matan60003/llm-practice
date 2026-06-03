from classifier import classifier_text

def test_financial_classification():
    assert classifier_text("מה המחיר של השירות?") == "פיננסי"

def test_general_classification():
    assert classifier_text("שלום, רציתי לשאול שאלה") == "כללי"