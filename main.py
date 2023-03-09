import requests
import json

if __name__ == '__main__':
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

    print(ttreports)
