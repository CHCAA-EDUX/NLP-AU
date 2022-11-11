from ner.main import main


def test_main():
    """test that main run using a single epoch"""

    main(gensim_embedding="glove-wiki-gigaword-50", epochs=1, batch_size=5, learning_rate=0.1)
