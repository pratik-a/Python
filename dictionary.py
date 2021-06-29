data = {1: "pratik", 2: "awasthi", 3: "tata", 4: "ambani"}

print(data[2])

print(data.get(4))

print(data.get(5, "not found"))

keys = ["apple", "cabbage", "rose"]
values = ["fruit", "vegetable", "fllower"]
amerge = dict(zip(keys, values))

print(amerge)

data["tulsi"] = "plant"

print(data)
