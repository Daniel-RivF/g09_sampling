



def get_coord(filename,index):
    with open(filename, 'r') as f:
        l = [map(float,i.split()) for i in f.readlines()]
    a = [item for sublist in l for item in sublist]
    return a[index+1]

def get_interval(listcoord, divisions):
    length = (max(listcoord) - min(listcoord)) / divisions



    return
