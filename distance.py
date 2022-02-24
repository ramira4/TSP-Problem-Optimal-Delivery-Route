import csv
# read distance csv file
with open('distance.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    distance_list = list(reader)

    # get_distance_between return distance between two location nodes
    def get_distance_between(row, column):
        distance = distance_list[row][column]
        if distance == "":
            distance = distance_list[column][row]
        return float(distance)

    # add_distances given a list of total distances traveled by a truck, return the sum of all distances
    def add_distances(list_):
        total = 0
        for x in list_:
            total = total + float(x)
        return total
