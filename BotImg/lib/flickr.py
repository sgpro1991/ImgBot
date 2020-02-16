from config import FLICKR_PUBLIC, FLICKR_SECRET
from flickrapi import FlickrAPI
import random


class FlackrImage(object):
    def __init__(self):
        self.flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
        self.extras = 'url_l'

    def search_img(self, tag):
        return self.flickr.photos.search(tags=tag, extras=self.extras)

    def get_random_image(self, tag):
        photo = random.choice(self.search_img(tag)['photos']['photo'])
        return photo

