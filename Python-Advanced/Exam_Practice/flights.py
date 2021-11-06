def flights(*args):
    flight_dictionary = {}
    for i in range(0, len(args), 2):
        if args[i] == 'Finish':
            break
        if not args[i] in flight_dictionary:
            flight_dictionary[args[i]] = args[args.index(args[i]) + 1]
        else:
            flight_dictionary[args[i]] += args[i + 1]

    return flight_dictionary

#Variant 2
# def flights(*args, flights_dictionary=dict()):
#     flight = [*args]
#     if flight[0] == 'Finish':
#         return flights_dictionary
#     if flight[0] not in flights_dictionary:
#         flights_dictionary[flight[0]] = int(flight[1])
#     else:
#         flights_dictionary[flight[0]] += int(flight[1])
#
#     return flights(*flight[2:], flights_dictionary=flights_dictionary)

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
