#Dictionaries
monthconversions = {
"jan" : "january",
"feb" : "febrary",
"mar" : "march",
}
print(monthconversions["mar"])
print(monthconversions.get("feb"))
print(monthconversions.get("dec" , "not a valid month"))
print(monthconversions.keys())