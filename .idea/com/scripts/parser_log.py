from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class MarkerResult:
    max_value: int
    min_value: int
    average: int

def parse_log(file_path: str, markers: List[str]):
    tmp_result = {}
    for marker in markers:
        tmp_result[marker] = []
    with Path(file_path) .open('r') as file:
        for line in file:
            for marker in markers:
                if marker in line:
                    value = line.rsplit(':', 1)[-1]
                    tmp_result[marker].append(float(value))

    result = {}
    for key in tmp_result:
        values = tmp_result[key]
        max_value = None if not values else max(values)
        min_value = None if not values else min(values)
        average = None if not values else sum(values)/len(values)
        average = round(average,2)
        result[key] = MarkerResult(max_value, min_value, average)
    return result

def get_unique_task_names(path):
    names = []
    log_file = path
    with open(log_file, "r") as file:
        for line in file:
            names.append(line.rstrip('\n').split('.')[0])
    uniq = set(names)
    return uniq

def get_values(uniq, log_file):
    calc_values = []
    str_calc = ''
    for x in uniq:
        markers = [x, 'cpp']
        #markers = [x]
        data = parse_log(log_file, markers)
        for marker in markers:
            result = data[marker]
            print(result.average)
            print(result.max_value)
            print(result.min_value)
            str_calc = "task name: "+x+ " average: "+str(result.average)+" max: "+ str(result.max_value)+" min: "+str(result.min_value)
            calc_values.append(str_calc)
    return calc_values

if __name__ == '__main__':

    line = "CClientProfile for Task duration :425ms (0h 0min 0sec)"
    value = line.rsplit(':', 1)[-1]  #'425ms (0h 0min 0sec)'
    value2 = value.rsplit('ms', 1)[0]  #'425'

    names = []
    log_file = r'C:\Users\fitim\IdeaProjects\PythonProject\RobotFramework\.idea\com\scripts\Parser Output 2020-02-29 20-53-59.txt'
    with open(log_file, "r") as file:
        for line in file:
            names.append(line.rstrip('\n').split('.')[0])
    uniq = set(names)
    for x in uniq:
        markers = [x, 'cpp']
        #markers = [x]
        data = parse_log(log_file, markers)
        #print(type(data))
        print(data)
        #list_of_unique_dicts=list(np.unique(np.array(data).astype(str)))
        #print(list_of_unique_dicts)

        for marker in markers:
            result = data[marker]
            print(result.average)
            print(result.max_value)
            print(result.min_value)
