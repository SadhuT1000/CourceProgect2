import os

from config import DATA_DIR
from src.workJson import JSONSaver


def test_init():
    assert JSONSaver().filename == os.path.join(DATA_DIR, "vacancies.json")
