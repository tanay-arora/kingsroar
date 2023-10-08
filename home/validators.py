from django.core.exceptions import ValidationError

def clean_image(self):
    image = self.file
    if image:
        if image.size > 1*1024*1024:
            raise ValidationError("Image file is larger than 1mb")
        return image
    else:
        raise ValidationError("Couldn't read uploaded image")

def get_clean_image(self):
    image = self
    if image:
        if image.size > 1*1024*1024:
            return "Image file is larger than 1mb"
    else:
        return "Couldn't read uploaded image"