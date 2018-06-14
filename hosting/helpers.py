from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account


def get_filename_from_path(path):
    return path.split('\\')[-1]


def get_statistics_from_image(image):
    credentials = service_account.Credentials.from_service_account_file('D:/Python/key.json')

    # Instantiates a client
    client = vision.ImageAnnotatorClient(credentials=credentials)

    content = image.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    statistics = ''
    for label in labels:
        statistics += label.description + ','

    return statistics
