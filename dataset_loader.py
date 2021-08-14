from pandas import DataFrame


class DatasetLoader:
    def load(self, path: str) -> DataFrame:
        ...
