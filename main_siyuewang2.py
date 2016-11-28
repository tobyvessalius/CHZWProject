import os, re
from multiprocessing import Pool
from rebuild_siyuewang2 import rebuild

def main(cur):
    for fname in os.listdir(cur):
        if os.path.isfile(os.path.join(cur, fname)) and re.search('csv$',fname):
            rebuild(cur, fname)

if __name__ == '__main__':
    cur = os.getcwd()
    if not os.path.exists(os.path.join(cur, 'data/')):
        os.makedirs(os.path.join(cur, 'data/'))

    directory = []
    for x in os.listdir('./'):
        if os.path.isdir(os.path.join(cur, x)) and re.search('set', x):
            directory.append(x)
    pool = Pool(processes=len(directory))
    pool.map(main, directory)
    pool.close()
    pool.join()
    print('Finished!')
