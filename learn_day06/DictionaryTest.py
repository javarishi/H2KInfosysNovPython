sampleDictionary = {
    "company": "Toyota",
    "model": "Camry",
    "Year": 2019,
    "mpg": 20,
    100: 200
}
print(sampleDictionary)
sampleDictionary["owners"] = ["Rishi", "Laxman", "Gopal", "Lucky", "Madhav"]
print(sampleDictionary)
print(sampleDictionary["model"])
print(sampleDictionary.get("model"))
sampleDictionary["Year"] = 2020
print(sampleDictionary)

# complete Entry iteration
for key, value in sampleDictionary.items():
    print(key, value)

# Iteration thru Keys
for eachKey in sampleDictionary:
    print(eachKey, sampleDictionary.get(eachKey))

# Iteration thru values
for eachValue in sampleDictionary.values():
    print(eachValue)

if "Year" in sampleDictionary:
    print("Key Year exists")

if "Camry" in sampleDictionary.values():
    print("Camry exists")

sampleDictionary.popitem() # Last Inserted Value
print(sampleDictionary)
sampleDictionary.pop(100) # Key
print(sampleDictionary)

# del sampleDictionary["model"]

print(len(sampleDictionary))

sampleDictionary.clear()

print(sampleDictionary)