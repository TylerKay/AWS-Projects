import json

def loggenerator():
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)


def lambda_handler(event, context):
    # TODO implement
    print(event)
    loggenerator()

    return "Testtt"

