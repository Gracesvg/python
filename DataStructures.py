#list datastructures,its ordered and changeable
cars=["Mercedes","Nissan","Toyota","Range"]
cars[1]="Subaru"
cars.append("mitsubishi")
cars.insert(2,"BMW")
cars.pop(1)
print(cars)

#this is a tuple,ordered, its unchangeable
fruits=("Mangoes","Oranges","Pineapples","Avocado")

#sets datastructures
countries={"Kenya","Tanzania","Burundi","Ethiopia"}
print(countries)

#dictionaries

matunda={
    "amount":40,
    "jina":"Ndizi",
    "rangi":"yellow",

}
matunda["size"]="large"
print(matunda)