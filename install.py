import os

resources = [
    'django',
    'google-cloud-vision',
    'Pillow==5.0.0'
]

for app in resources:
    os.system('pip install %s' % app)
