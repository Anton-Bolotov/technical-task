from flask import Flask, request, jsonify


app = Flask(__name__)

message_json = {
    "message": "Для получения время общего присутствия ученика и учителя на уроке (в секундах),"
               " отправьте POST запрос с телом из body",
    "body": {
        "lesson": [1594663200, 1594666800],
        "pupil": [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
        "tutor": [1594663290, 1594663430, 1594663443, 1594666473]
    }
}


def appearance(intervals):
    result, count_pupil, count_tutor = 0, 0, 0
    while True:
        try:
            pupil_start,  pupil_end = intervals['pupil'][count_pupil], intervals['pupil'][count_pupil + 1]
            count_pupil += 2
            while True:
                try:
                    tutor_start, tutor_end = intervals['tutor'][count_tutor], intervals['tutor'][count_tutor + 1]
                    count_tutor += 2
                    min_max_difference = min(pupil_end, tutor_end) - max(pupil_start, tutor_start)
                    min_max_comparison = min(pupil_end, tutor_end) != max(pupil_start, tutor_start)
                    if min_max_comparison and min_max_difference > 0:
                        result += min_max_difference
                except IndexError:
                    count_tutor = 0
                    break
        except IndexError:
            break
    return result


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify(message_json)
    if request.method == 'POST':
        result = appearance(intervals=request.get_json())
        return jsonify({'result': result})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
