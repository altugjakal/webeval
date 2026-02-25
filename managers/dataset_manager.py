from utils.loaded_dataset import LoadedDataset

_dataset = None

def get_dataset():
    global _dataset
    if _dataset is None:
        _dataset = LoadedDataset()
        _dataset.load()
        return _dataset
    else:
        return _dataset