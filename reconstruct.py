import requests
import json



featurecollection= '{"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-66.96399527778121,0.08480498968637591,-1.041251881730811e-9]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-50.26742644744623,-9.131305457215065,-4.012530655510278e-9]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-86.4606199362609,35.87971530053026,-1.3183746082831785e-9]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-66.3889696082647,-1.7006566507389476,4.166627807583027e-9]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-76.26884029698192,23.81019827148597,-8.34300781934006e-9]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[-78.03146874799945,-2.8310182489749685,0]}}]}'

formdata = {
    "feature_collection" : featurecollection,
    "time" : "250",
    "model" : 'SCOTESE&WRIGHT2018'
}

r = requests.post(url="https://deep-time.org/reconstruct/reconstruct_feature_collection", data=formdata)
print(r.text)