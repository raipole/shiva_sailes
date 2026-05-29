# import csv
#
# # write to a csv file from a list of lists
# players = [
#     ['Rohit', 'Sharma'],
#     ['Shubham', 'Gill'],
#     ['Virat', 'Kohli'],
#     ['Rahul', 'K L'],
#     ['Hardik', 'Pandya']
# ]
# with open("players.txt", 'wt') as fout:
#     csvout = csv.writer(fout)
#     csvout.writerows(players)
#
# with open('players.txt','rt') as fin:
#     players=csv.reader(fin)
#     line=[i for i in players]
#     print(line)

import json
menu= \
    {
        "breakfast": {
            "hours": "7-11",
            "items": {
                "breakfast burritos": "$6.00",
                "pancakes": "$4.00"
            }
        },
        "lunch": {
            "hours": "11-3",
            "items": {
                "hamburger": "$5.00"
            }
        },
        "dinner": {
            "hours": "3-10",
            "items": {
                "spaghetti": "$8.00"
            }
        }
    }

with open('time_table.txt','wt') as file:

    # json_time=json.dumps(menu)
    # # dump key word gives dictunary to str
    #
    # print(json_time)
    # print(type(json_time))
    # menu2 = json.loads(json_time) # dump key word gives str to dictunary .
    # print(menu2)
    # print(type(menu2))
    menu_json = json.dumps(menu)
    print(menu_json)
    with open("menu_json.txt", 'wt') as fout:
        fout.write(menu_json)


    # let’s turn the JSON string menu_json back into a Python data structure (menu2) by using loads()
    menu2 = json.loads(menu_json)

    # with open('dict_time.txt','wt') as fin:
    #
    #     fin.writelines(menu2)
    #     print(menu2)

    with open("menu_json.txt",'rt') as fin:
        d=json.load(fin)
        print(d)
