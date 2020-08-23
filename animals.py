import pathlib
import random


animals_folder = pathlib.Path('data/images/animals')
animal_pictures = list(animals_folder.glob('*.jpg'))


def get_random_animal_pairs(size=None):
    """Returns a random list of pairs of animal pictures as pathlib.Paths.

    If `size` is provided, it should be an even number representing the total
    amount of pictures that should be returned.
    By default, all available pictures will be included.
    """
    pictures = animal_pictures

    if size:
        pictures = animal_pictures[:size // 2]

    random_pairs = pictures * 2
    random.shuffle(random_pairs)
    return random_pairs
