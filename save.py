import csv


def save_to_file(videos):
    file = open(f"{videos}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["title", "latitude", "longitude"])
    for v in videos:
        writer.writerow(list(v.values()))
    return
