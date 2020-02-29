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
        result[key] = MarkerResult(max_value, min_value, average)
    return result

if __name__ == '__main__':
    markers = ['tidii.something1']
    data = parse_log('./file.txt', markers)
    print(data)
    for marker in markers:
        result = data[marker]
        print(result.average)
        print(result.max_value)
        print(result.min_value)