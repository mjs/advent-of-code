import re
import sys

def valid_year(low, high):
    def v(raw):
        assert len(raw) == 4
        assert low <= int(raw) <= high
    return v


def valid_height(raw):
    m = re.match("^(\d+)(cm|in)$", raw)
    assert m
    h = int(m.group(1))
    if m.group(2) == "cm":
        assert 150 <= int(h) <= 193
    else:
        assert 59 <= int(h) <= 76


def valid_hair(raw):
    assert re.match("^#[0-9a-f]{6}$", raw)


EYE_COLORS = set('amb blu brn gry grn hzl oth'.split())

def valid_eye(raw):
    assert raw in EYE_COLORS


def valid_pid(raw):
    assert re.match("^\d{9}$", raw)


FIELDS = {
    'byr': valid_year(1920, 2002),
    'iyr': valid_year(2010, 2020),
    'eyr': valid_year(2020, 2030),
    'hgt': valid_height,
    'hcl': valid_hair,
    'ecl': valid_eye,
    'pid': valid_pid,
}


def is_valid(passport):
    required = set(FIELDS.keys())
    for f in passport.split():
        code, raw = f.split(":", 1)
        if code == 'cid':
            continue

        required.discard(code)
        try:
            FIELDS[code](raw)
        except AssertionError:
            return False

    return not required


def main():
    print(sum(1 for p in sys.stdin.read().strip().split("\n\n") if is_valid(p)))


if __name__ == '__main__':
    main()
