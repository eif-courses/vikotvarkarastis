import requests
import json
from fastapi import FastAPI

app = FastAPI()


def get_teachers(id, datefrom='2023-03-13', dateto='2023-03-17'):
    url2 = "https://vikoeif.edupage.org/timetable/server/currenttt.js?__func=curentttGetData"

    payload2 = json.dumps({
        "__args": [
            None,
            {
                "year": 2022,
                "datefrom": str(datefrom),
                "dateto": str(dateto),
                "table": "teachers",
                "id": str(id),
                "showColors": True,
                "showIgroupsInClasses": False,
                "showOrig": True,
                "log_module": "CurrentTTView"
            }
        ],
        "__gsh": "00000000"
    })
    return requests.request("POST", url2, data=payload2).json()


url = "https://vikoeif.edupage.org/timetable/server/regulartt.js?__func=regularttGetData"

payload = json.dumps({
    "__args": [
        None,
        "310"
    ],
    "__gsh": "00000000"
})
response = requests.request("POST", url, data=payload)

result = response.json()

periods = result['r']['dbiAccessorRes']['tables'][1]['data_rows']
daydefs = result['r']['dbiAccessorRes']['tables'][4]['data_rows']
weekdefs = result['r']['dbiAccessorRes']['tables'][5]['data_rows']
days = result['r']['dbiAccessorRes']['tables'][7]['data_rows']
weeks = result['r']['dbiAccessorRes']['tables'][8]['data_rows']

classrooms = result['r']['dbiAccessorRes']['tables'][11]['data_rows']
classes = result['r']['dbiAccessorRes']['tables'][12]['data_rows']
subjects = result['r']['dbiAccessorRes']['tables'][13]['data_rows']
teachers = result['r']['dbiAccessorRes']['tables'][14]['data_rows']
groups = result['r']['dbiAccessorRes']['tables'][15]['data_rows']

divisions = result['r']['dbiAccessorRes']['tables'][16]['data_rows']
lessons = result['r']['dbiAccessorRes']['tables'][18]['data_rows']
cards = result['r']['dbiAccessorRes']['tables'][20]['data_rows']
ttreports = result['r']['dbiAccessorRes']['tables'][21]['data_rows']


@app.get("/teachers")
def get_teachers():
    return json.dumps(teachers)


@app.get("/")
def start():
    return {'hello world'}

@app.get("/teacher/{idd}/{datefrom}/{dateto}")
def hello(idd, datefrom, dateto):
    current_teacher = get_teachers(idd, datefrom, dateto)['r']['ttitems']

    new_list = []

    for item in current_teacher:
        for teacher in teachers:
            if teacher['id'] in item['teacherids']:
                item['teacher'] = teacher['short']
                break
        for subject in subjects:
            if subject['id'] in item['subjectid']:
                item['subject'] = subject['name']
                break
        for group in classes:
            if group['id'] in item['classids']:
                item['group'] = group['name']
                break
        for classroom in classrooms:
            if classroom['id'] in item['classroomids']:
                item['classroom'] = classroom['name']
                break
        new_list.append(item)

    return new_list
