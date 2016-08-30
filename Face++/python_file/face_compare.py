# -*- coding: utf-8 -*-
import facepp
from pprint import pformat
import types
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
face1 = api.detection.detect(img =facepp.File('image/jack_cheng/5.jpg'))
face1_id=face1['face'][0]['face_id']
face2 = api.detection.detect(img =facepp.File('image/jack_cheng/3.jpg'))
face2_id=face2['face'][0]['face_id']
##print face['face'][0]['face_id']
#res = api.recognition.compare(api_key =API_KEY, api_secret = API_SECRET, face_id1 = face1_id, face_id2 = face2_id)
##print_result("compare_result",res)
#print int(res['similarity'])
## print type(res['similarity'])
res1=api.person.get_info(api_key =API_KEY, api_secret = API_SECRET,person_name = "成龙")
print_result("info",res1)
print type(res1['face'])
# print res1['face'][0]['face_id'] + res1['face'][1]['face_id']
print len(res1['face'])
i = 0
while(i<len(res1['face'])):
    res = api.recognition.compare(api_key=API_KEY, api_secret=API_SECRET, face_id1=face1_id, face_id2=res1[
    'face'][i]['face_id'])
    print res['similarity']
    i=i+1




