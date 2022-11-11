from ner.data import prepare_batch, load_data, gensim_to_torch_embedding
import gensim.downloader as api

def create_tags_to_ids():
    dataset = load_data()
    tags = dataset["train"].features["ner_tags"].feature.names
    tags_to_ids = {tag: i for i, tag in enumerate(tags)}
    return tags_to_ids


def test_prepare_batch():
    """test that the prepare batch function outputs the correct shape"""
    sample_texts = [
        ["I", "am", "happy"],
        ["I", "like", "to", "eat", "pizza"],
        ["Anders", "like", "to", "eat", "pizza"],
    ]
    sample_labels = [
        ["O", "O", "O"],
        ["O", "O", "O", "O", "O"],
        ["I-PER", "O", "O", "O", "O"],
    ]

    tags_to_ids = create_tags_to_ids()
    sample_labels = [[tags_to_ids[tag] for tag in tags] for tags in sample_labels]

    embedding_layer, vocab = gensim_to_torch_embedding(api.load("glove-wiki-gigaword-50"))

    X, y = prepare_batch(sample_texts, sample_labels, vocab)

    assert X.shape == (3, 5), "Your prepared batch does not have the correct size"
    assert all(i in y.unique() for i in [-1, 0, 2]), "Your prepared batch does not contain the correct labels"
