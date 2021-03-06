from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account


def get_statistics_from_image(image):
    try:
        credentials = service_account.Credentials.from_service_account_file('key.json')
    except FileNotFoundError:
        return "Key not found"

    client = vision.ImageAnnotatorClient(credentials=credentials)

    content = image.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    statistics = ''
    for label in labels:
        statistics += label.description + ','

    return statistics[:-1]


def is_valid_type(file):
    VALID_IMAGE_EXTENSIONS = ["jpg", "jpeg", "png"]
    if file.name.split('.')[-1] in VALID_IMAGE_EXTENSIONS:
        return True
    return False
