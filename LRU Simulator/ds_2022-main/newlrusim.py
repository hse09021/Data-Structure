def do_sim(cache_slots):
    
    cache_hit = 0
    tot_cnt = 0

    data_file = open("linkbench_short.trc")

    cache = dict()

    for line in data_file.readlines():
        lpn = line.split()[0]
        tot_cnt += 1

        if lpn in cache:
            del cache[lpn]
            cache_hit += 1
        cache[lpn] = lpn
        if len(cache) > cache_slots:
            del cache[next(iter(cache))]
        

    print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)

if __name__ == "__main__":
    for cache_slots in range(100, 1000, 100):
        do_sim(cache_slots)