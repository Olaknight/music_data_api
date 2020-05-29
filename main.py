import csv
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.music_data
music_metadata = db.music_metadata

def parse_row(row):
    titles, iswc = [], row[0]

    if row[1] != '':
        titles.append({"title": row[1], "type": "OriginalTitle"})

    for title in {row[2], row[3], row[4]}:
        if title != '':
            titles.append({"title": title, "type": "AlternativeTitle"})

    return {
        "_id": int(row[8]),
        "iswc": ''.join((iswc[0], iswc[2:-2], iswc[-1])),
        "titles": titles,
        "right_owners": [{ "name": row[5], "role": row[6], "ipi": str(row[7]).rjust(11, '0') }]
    }



with open('db_works_test.csv', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)
    seen_header = False

    for row in csv_reader:
        if bool(seen_header):
            music = music_metadata.find_one({"_id": int(row[8])})
            if bool(music):
                music_metadata.update_one(
                    music, {'$push':
                                { "right_owners":
                                      { "name": row[5], "role": row[6], "ipi": str(row[7]).rjust(11, '0') }
                                }
                            })

            else:
                new_entry = parse_row(row)
                music_metadata.insert_one(new_entry)
        seen_header = True


