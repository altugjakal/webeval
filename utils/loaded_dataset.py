from beir import util
from beir.datasets.data_loader import GenericDataLoader

class LoadedDataset:
    def __init__(self, dataset='scifact'):
        self.dataset = dataset
        self.corpus = None
        self.queries = None
        self.qrels = None
        self.loader = GenericDataLoader(dataset)


    def load(self):
        url = "https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/{}.zip".format(self.dataset)
        data_path = util.download_and_unzip(url, "datasets")
        self.corpus, self.queries, self.qrels = GenericDataLoader(data_folder=data_path).load(split="test")

    def get_by_doc_id(self, doc_id):
        return self.corpus[str(doc_id)]

    def get_all_corpus(self):
        return self.corpus.keys()

