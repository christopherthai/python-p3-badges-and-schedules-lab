def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]


def assign_rooms(names):
    rooms = range(1, 9)

    return [
        f"Hello, {name}! You'll be assigned to room {room}!"
        for name, room in zip(names, rooms)
    ]


def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)

    for room in assign_rooms(names):
        print(room)
