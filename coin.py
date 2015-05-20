import random
from collections import Counter

def flip_coin_ntimes(n = 100):
    flips = []
    flip_dict = {}
    for i in range(n):
        flip = random.choice([0,1])
        flips.append(flip)
    flip_dict = Counter(flips)
    return flip_dict

hundred_flips_list = [flip_coin_ntimes(100) for i in range(10000)]
ratios2 = []

for sim in hundred_flips_list:
    ratio = sim[0] / 100
    ratios2.append(ratio)

sorted_ratios = sorted(ratios2)

def sort_bins(ratios, num_of_bins=20):
    bins = {}
    for num in range(num_of_bins):
        bins[num]=[]
    for ratio in ratios:
        if ratio <= 0.1:
            bins[0].append(ratio)
        elif 0.05 < ratio <= 0.1:
            bins[1].append(ratio)
        elif 0.1 < ratio <= 0.15:
            bins[2].append(ratio)
        elif 0.15 < ratio <= 0.2:
            bins[3].append(ratio)
        elif 0.2 < ratio <= 0.25:
            bins[4].append(ratio)
        elif 0.25 < ratio <= 0.3:
            bins[5].append(ratio)
        elif 0.3 < ratio <= 0.35:
            bins[6].append(ratio)
        elif 0.35 < ratio <= 0.4:
            bins[7].append(ratio)
        elif 0.4 < ratio <= 0.45:
            bins[8].append(ratio)
        elif 0.45 < ratio <= 0.5:
            bins[9].append(ratio)
        elif 0.5 < ratio <= 0.55:
            bins[10].append(ratio)
        elif 0.55 < ratio <= 0.6:
            bins[11].append(ratio)
        elif 0.6 < ratio <= 0.65:
            bins[12].append(ratio)
        elif 0.65 < ratio <= 0.7:
            bins[13].append(ratio)
        elif 0.7 < ratio <= 0.75:
            bins[14].append(ratio)
        elif 0.75 < ratio <= 0.8:
            bins[15].append(ratio)
        elif 0.8 < ratio <= 0.85:
            bins[16].append(ratio)
        elif 0.85 < ratio <= 0.9:
            bins[17].append(ratio)
        elif 0.9 < ratio <= 0.95:
            bins[18].append(ratio)
        elif 0.95 < ratio <= 1.0:
            bins[19].append(ratio)
    return[len(pair[1]) for pair in bins.items()]

bin_counts = sort_bins(sorted_ratios)

print(bin_counts)
