from operator import itemgetter
import json
import re, operator
import csv


def save_to_file_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split('(\d+)', text)]


with open('old_test.json', 'r') as f:
    distros_dict = json.load(f)


    def Extract(distros_dict):

        first_elem_list = [item[0] for item in distros_dict]
        # first_elem_list.sort(key=natural_keys)
        distros_dict = sorted(distros_dict, key=lambda x: int(x[0].replace(".jpg", "")))

        # print(distros_dict)

        save_to_file_json(distros_dict, "sorted.json")

        with open('csvout.csv', 'w') as ff:
            csvwriter = csv.DictWriter(ff, ['fname', 'w1', 'w2', 'ratio'], delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            csvwriter.writeheader()

            for item in distros_dict:
                if item[1] is not None:
                    csvwriter.writerow({
                        'fname': item[0],
                        'w1': item[1][0],
                        "w2": item[1][1],
                        "ratio": str(item[1][2]).replace(".", ",")
                    })
                else:
                    csvwriter.writerow({
                        'fname': item[0],
                        'w1': '',
                        "w2": '',
                        "ratio": ''
                    })

        return distros_dict

    print(Extract(distros_dict))

