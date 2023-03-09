import requests
import json


def get_teachers():
    url2 = "https://vikoeif.edupage.org/timetable/server/currenttt.js?__func=curentttGetData"

    payload2 = json.dumps({
        "__args": [
            None,
            {
                "year": 2022,
                "datefrom": "2023-03-06",
                "dateto": "2023-03-12",
                "table": "teachers",
                "id": "-1007",
                "showColors": True,
                "showIgroupsInClasses": False,
                "showOrig": True,
                "log_module": "CurrentTTView"
            }
        ],
        "__gsh": "00000000"
    })
    return requests.request("POST", url2, data=payload2).json()


if __name__ == '__main__':

    print(get_teachers()['r']['ttitems'])

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

    print(teachers)

    # cards
    # 'id': '*36',
    # 'subjectid': '-2488'     => Informacinių sistemų auditas,
    # 'teacherids': ['-1083'],   => Lekt. V. Valukonis
    # 'groupids': ['*24'], 'classids': ['-732']    => IS20A,
    # 'count': 1, 'durationperiods': 1, 'classroomidss': [['-430']] => 414,
    # 'termsdefid': '*3', 'weeksdefid': '*4', 'daysdefid': '*7', 'terms': '1',
    # 'seminargroup': None, 'bell': '', 'studentids': [], 'groupnames': ['']

    # -430 = 414

    # print(lessons)
    print(groups[46]['id'])
    print(groups[46]['classid'])

    for group in groups:
        for cl in classes:
            if cl['id'] == group['classid']:
                print(cl['name'], cl['id'])

# a = groups[46]['classid'] in classes[0]['id']
# print(a)
# print(classes[0]['id'])
# 'classid': '-728'
