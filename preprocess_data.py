from preprocess_face.face_extractor import extract_faces
from preprocess_face.augment_data import make_augmentation
from preprocess_face.create_dataset import make_dataset


def preprocess_data():
    # Parameters
    extract_from_video = True
    samples = 10000
    resolution = (256, 256)
    splitted = 10  # 'Splitted' parameter use when dataset is to huge to load in memory and you need to split it

    # extract_faces(extract_from_video=extract_from_video, resolution=resolution)
    # make_augmentation(samples=samples)
    make_dataset(splitted=splitted)


if __name__ == "__main__":

    preprocess_data()