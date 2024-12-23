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


def main(inp):
    disk, disk2 = parse_disk(inp)
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
    print("Part 1: ", checksum)

    print(len(disk2))
    write_ptr = 0
    read_ptr = len(disk2) - 1
    for file_index in range(len(disk2) - 1, 0, -1):
        file = disk2[file_index]
        if file.kind != "file":
            continue

        # find index of the first gap large enough
        free_index, free_space = next(((i, b) for i, b in enumerate(disk2) if b.kind == "free" and b.size >= file.size), (None, None))
        if free_index is None:
            continue
        # add a free space in place of the file
        disk2[file_index] = Item("free", file.size)
        # insert file just before free space
        disk2.insert(free_index, file)
        # decrease free space by file size (in case free space is larger)
        free_space.size -= file.size
    total_checksum = 0
    offset = 0
    print(disk2)
    print(len(disk2))
    for f in disk2:
        if f.kind != "file":
            offset += f.size
            continue
        # S(n) = n*(n+1) // 2
        print(f"checksum = {f.id_} * ({offset} * {f.size} + ({f.size} * ({f.size - 1})) // 2")
        checksum = f.id_ * (offset * f.size + (f.size * (f.size - 1)) // 2)
        print(f, checksum)

        offset += f.size
        total_checksum += checksum
    print(total_checksum)



        



if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if len(sys.argv) > 1 else None
    content = "2333133121414131402"
    if infile is not None:
        with open(infile) as f:
            content = f.read().rstrip()
    main(content)

