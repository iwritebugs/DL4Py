import os
import pathlib
import sys

project_pth = pathlib.Path(os.path.abspath(__file__)).parent.parent.parent
sys.path.insert(0, project_pth)


def test_smoke():
    import loaders.simple_loader
    loader = loaders.simple_loader.Loader()

    data_pth = project_pth.joinpath('data', 'animals', 'cats')
    images = [str(data_pth.joinpath(f)) for f in os.listdir(data_pth)]
    data, labels = loader.load(images)
    assert all(label == 'cats' for label in labels)


