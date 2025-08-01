from itertools import zip_longest


def grouper(n, iterable):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args)


def main(inp):
    data = inp.readline().rstrip()
    width, height = 25, 6
    layers = [x for x in grouper(width*height, data)]
    layer_i, _ = min(((i, x.count("0")) for i, x in enumerate(layers)), key=lambda x: x[1])
    ones = layers[layer_i].count("1")
    twos = layers[layer_i].count("2")
    print("Part 1: ", ones * twos)

    image = ["2"] * width * height
    layers = [x for x in grouper(width*height, data)]
    layer_i, _ = min(((i, x.count("0")) for i, x in enumerate(layers)), key=lambda x: x[1])
    for l in layers[::-1]:
        #  0 is black, 1 is white, and 2 is transparent.
        for i, x in enumerate(l):
            if x == "2":
                continue
            image[i] = x

    print("Part 2:")
    for i in range(height):
        b, w = " ", "\u2588"
        im = [b if x == "0" else w for x in image[width*i:width*(i+1)]]
        print("".join(im))


if __name__ == "__main__":
    import fileinput
    main(fileinput.input())

