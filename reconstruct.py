import requests
import json

global FILE_TYPE
global FILE_PATHd

FILE_TYPE = "csv"
FILE_PATH = ""

def reconstructPoint(featureCollection,time,model):
    formdata = {
        "feature_collection" : featureCollection,
        "time" : time,
        "model" : model
    }
    r = requests.post(url="https://deep-time.org/reconstruct/reconstruct_feature_collection", data=formdata)
    return r.json()
f = '{"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-66.96399527778121,0.08480498968637591,-1.041251881730811e-9]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-50.26742644744623,-9.131305457215065,-4.012530655510278e-9]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-86.4606199362609,35.87971530053026,-1.3183746082831785e-9]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-66.3889696082647,-1.7006566507389476,4.166627807583027e-9]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-76.26884029698192,23.81019827148597,-8.34300781934006e-9]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-78.03146874799945,-2.8310182489749685,0]}}]}'
t = '250'
m = 'SCOTESE&WRIGHT2018'

x=[-66.96399527778121,-78.03146874799945]
y=[0.08480498968637591,-2.8310182489749685]
z=[-1.041251881730811e-9,0]

features=list()
for i in range(0,len(x)):
    feature_template = {
        "type" : "Feature",
        "properties" : {},
        "geometry" : {
            "type" : "Point",
            "coordinates" : [x[i],y[i],z[i]]
        }
    }
    features.append(feature_template)

feature_collection={
    "type" : "FeatureCollection",
    "features" : features
}

s = json.dumps(feature_collection)
print(reconstructPoint(s,t,m))
