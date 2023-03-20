def sub_idx(haystack: str, needle: str) -> int:
    return haystack.find(needle)


if __name__ == '__main__':
    print(sub_idx(haystack="sadbutsad", needle="sad"))