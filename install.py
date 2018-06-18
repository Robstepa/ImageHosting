import os

resources = [
    'django',
    'google-cloud-vision'
]

for app in resources:
    os.system('pip install %s' % app)
