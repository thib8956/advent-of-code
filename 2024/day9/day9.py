from dataclasses import dataclass
from typing import Literal


@dataclass()
class Item:
    kind: Literal["file", "free"]
    size: int
    id_: int = 0


def parse_disk(data):
    disk = {}
    disk2 = []
    id_cnt = 0
    offset = 0
    for pos, size in enumerate(data):
        if pos % 2 == 0:  # file
            id = id_cnt
            for i in range(int(size)):
                disk[offset + i] = id
            disk2.append(Item("file", int(size), id))
            id_cnt += 1
            offset += int(size)
        else:  # free space
            if int(size) > 0:
                disk2.append(Item("free", int(size)))
                offset += int(size)
    return disk, disk2


def part1(disk):
    max_file_location = max(disk.keys())
    write_ptr = 0
    read_ptr = max_file_location
    while True:
        while write_ptr in disk:
            write_ptr += 1

        while read_ptr not in disk:
            read_ptr -= 1
        
        if write_ptr >= read_ptr:
            break

        disk[write_ptr] = disk[read_ptr]
        del disk[read_ptr]
    checksum = sum(i * disk.get(i, 0) for i in range(max_file_location))
    return checksum


def part2(disk):
    max_id = max(f.id_ for f in disk)
    for i in range(max_id, -1, -1):
        file, file_index = next((file, index) for index, file in enumerate(disk) if file.id_ == i)

        # find index of the first gap large enough
        free_index, free_space = next(((i, b) for i, b in enumerate(disk) if b.kind == "free" and b.size >= file.size), (None, None))
        if free_index is None:
            continue
        if free_index >= file_index:  # always move file to the left
            continue

        # decrease free space by file size (in case free space is larger)
        disk[free_index].size -= file.size
        # add a free space in place of the file
        disk[file_index] = Item("free", file.size)
        # insert file just before free space
        disk.insert(free_index, file)

        #debug = debug_print(disk)
        #print(debug)

    # calculate checksum for part2
    total_checksum = 0
    offset = 0
    #print(disk)
    debug_print(disk)
    #print(len(disk))
    for f in disk:
        if f.kind != "file":
            offset += f.size
            continue
        # S(n) = n*(n+1) // 2
        #print(f"checksum = {f.id_} * ({offset} * {f.size} + ({f.size} * ({f.size - 1})) // 2")
        checksum = f.id_ * (offset * f.size + (f.size * (f.size - 1)) // 2)
        #print(f, checksum, total_checksum)

        offset += f.size
        total_checksum += checksum
    return total_checksum


def main(inp):
    disk, disk2 = parse_disk(inp)
    print("Part 1: ", part1(disk))
    print("Part 2: ", part2(disk2))


def debug_print(disk):
    res = []
    for item in disk:
        if item.kind == "free" and item.size > 0:
            res.extend(["."] * item.size)
        else:
            res.extend([str(item.id_)] * item.size)
    return "".join(res)
        



if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if len(sys.argv) > 1 else None
    content = "2333133121414131402"
    if infile is not None:
        with open(infile) as f:
            content = f.read().rstrip()
    main(content)

