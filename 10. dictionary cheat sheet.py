# ===========================
# PYTHON DICTS: 1-PAGE CHEATSHEET
# ===========================

# 1) CREATE
person = {"name": "Abhi", "age": 25}
empty  = dict()

# 2) SAFE ACCESS (master this)
# Never crash on missing keys: ALWAYS prefer .get(key, default)
print(person.get("name", "Unknown"))     # -> "Abhi"
print(person.get("city", "Unknown"))     # -> "Unknown"

# Nested safe access pattern
user = {
    "asingh": {"first": "Abhi", "last": "Singh", "location": "India"}
}
info = user.get("asingh", {})            # {} avoids KeyError below
print(info.get("first", "N/A"))          # -> "Abhi"
print(info.get("salary", "N/A"))         # -> "N/A"

# 3) EXISTENCE CHECKS
if "name" in person:
    print("Name exists")

# 4) ADD / UPDATE
person["city"] = "Delhi"                 # add new key
person["age"]  = 26                      # update existing key

# Merge/extend (3.9+)
extra = {"role": "Engineer"}
person = person | extra                  # new dict (non-destructive)
# Or in-place:
person.update({"dept": "Security"})

# 5) INSERT-IF-MISSING (useful defaulting)
# setdefault returns the value if present, otherwise inserts default and returns it
prefs = {}
theme = prefs.setdefault("theme", "dark")  # now prefs = {"theme": "dark"}

# 6) DELETE
tmp = {"a": 1, "b": 2, "c": 3}
val = tmp.pop("b", None)                 # remove key & get value (or None if absent)
# del tmp["x"]  # would crash if "x" missing; avoid unless certain
k, v = tmp.popitem()                     # remove & return an arbitrary (last) item (3.7+ insertion-ordered)
tmp.clear()                              # empty dict

# 7) ITERATION
guys = {"john": "python", "cal": "java", "sofi": "python"}
for k, v in guys.items():                # key + value
    print(k, "->", v)
for k in guys.keys():                    # keys
    print(k)
for v in guys.values():                  # values
    print(v)

# 8) COPYING
a = {"x": [1, 2]}
shallow = a.copy()                       # shallow copy (inner lists shared)
import copy
deep = copy.deepcopy(a)                  # deep copy (fully independent)

# 9) COMPREHENSIONS (build dicts fast)
squares = {n: n*n for n in range(5)}     # {0:0, 1:1, ...}
filtered = {k: v for k, v in guys.items() if v == "python"}

# 10) SORTING FOR DISPLAY
by_key   = dict(sorted(guys.items(), key=lambda kv: kv[0]))
by_value = dict(sorted(guys.items(), key=lambda kv: kv[1]))

# 11) COUNTING (common mini-pattern without extra libs)
items = ["apple", "banana", "apple", "orange", "banana", "apple"]
counts = {}
for it in items:
    counts[it] = counts.get(it, 0) + 1   # safe increment
# counts -> {"apple": 3, "banana": 2, "orange": 1}

# 12) NEVER-FAIL FETCH PATTERN (commit to memory)
# value = d.get(key, DEFAULT)
# nested_value = d.get(outer, {}).get(inner, DEFAULT)
