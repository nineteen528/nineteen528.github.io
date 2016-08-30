# -*- coding: utf-8 -*-
import facepp
from pprint import pformat
import time

API_KEY = '7289d584a41fe3b679183ffca51cb03d'
API_SECRET = '3LFK6iO2_O7Q_3Vxo7eEFOqeRzoFfCxu'


def print_result(hint, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(k): encode(v) for (k, v) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    print hint
    result = encode(result)
    print '\n'.join(['  ' + i for i in pformat(result, width = 75).split('\n')])

api = facepp.API(API_KEY, API_SECRET)
face = api.detection.detect(img =facepp.File('image/jack_cheng/11.jpg'))
face_id=face['face'][0]['face_id']
##print face['face'][0]['face_id']
res1 = api.train.verify(api_key = API_KEY,api_secret = API_SECRET,person_name ="成龙")
res= api.recognition.verify(api_key =API_KEY, api_secret = API_SECRET,face_id = face_id,person_name="成龙")
print_result(" ",res)





