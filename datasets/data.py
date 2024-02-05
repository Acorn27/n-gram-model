from util import load_csv
from config import ROOT_DIR
import os

def load_sample_data():
    return _load_dataset('test1.csv')

def load_dataset(dataset_name):
    return _load_dataset(dataset_name)


def _load_dataset(file_name):
    return load_csv(_get_path(file_name))

def _get_path(file_name):
    path = os.path.join(ROOT_DIR, 'datasets', 'data', file_name)
    return os.path.abspath(path)