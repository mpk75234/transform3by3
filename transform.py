'''
this small module will transform a 3 x 3 matrix
'''

data = [[1,2,3], [4,5,6],[7,8,9]]
nuData = []

def build_array(data):
    x = iter(data)
    while True:
        try:
            y = next(x)
            nuData.append([])
        except StopIteration:
            print('STAPH!')
            break

def transform():
    build_array(data)
    w = iter(data)
    while w:
        try:
            v=next(w)
            u=iter(v)
            for item in nuData:
              thing=next(u)
              item.append(thing) 
              print(nuData)
        except StopIteration:
            print(nuData)
            break
if __name__=="__main__":
    transform()
