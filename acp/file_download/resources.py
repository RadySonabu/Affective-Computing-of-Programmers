from import_export import resources
from file_upload.models import Emotion


class Documents(resources.ModelResource):
    class Meta:
        model = Emotion
