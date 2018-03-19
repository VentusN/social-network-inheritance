from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.user=None
        if timestamp:
            self.timestamp = timestamp.strftime('%A, %b %d, %Y')
        else:
            self.timestamp = timestamp

    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super(TextPost,self).__init__(text,timestamp)
        
        
    def __str__(self):
        return '@{first_name} {last_name}: "{post}"\n\t{timestamp}'.format(first_name=self.user.first_name, 
        last_name=self.user.last_name, post=self.text,timestamp=self.timestamp)


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost,self).__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return '@{first_name} {last_name}: "{post}"\n\t{link}\n\t{timestamp}'.format(first_name=self.user.first_name, 
        last_name=self.user.last_name, 
        post=self.text,link=self.image_url, timestamp=self.timestamp)


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost,self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude
        self.user = None
        
    def __str__(self):
        return '@{first_name} Checked In: "{post}"\n\t{lat}, {long}\n\t{timestamp}'.format(
            first_name=self.user.first_name, last_name=self.user.last_name, 
        post=self.text,lat=self.latitude,long=self.longitude,timestamp=self.timestamp)