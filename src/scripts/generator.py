import adddeps
from argparse import ArgumentParser

from yaml_parser.writer import write_yaml


def parse_args(*argument_array):
    parser = ArgumentParser()
    parser.add_argument('--path', type=str, required=True)
    args = parser.parse_args(*argument_array)
    return args


def is_end():
    end = input("End? ")
    if end.lower() in ['y', 'yes']:
        return True
    if end:
        return is_end()


def nonempty_input(txt):
    ret = ""
    while not ret:
        ret = input(txt)
    return ret


def main(args):
    obj = {
        "url": input("url: "),
        "name": input("name: "),
        "script": []
    }
    
    characters = []
    default_start_time = "00:00:00"
    while True:
        if is_end():
            break

        character = nonempty_input(f"character {characters}: ")
        if character in map(str, range(len(characters))):
            character = characters[int(character)]
        elif character not in characters:
            characters.append(character)

        start_time = (input(f"start_time [default {default_start_time}]: ")
                      or default_start_time)
        end_time = nonempty_input("end_time: ")
        default_start_time = end_time
        text = nonempty_input("text: ")
        obj["script"].append({
            "character": character,
            "start_time": start_time,
            "end_time": end_time,
            "text": text})
        print()
    
    obj["characters"] = []
    for character in characters:
        d = {"character": character}
        d["actor"] = input(f"actor of {character}:") or "[Unknown]"
        aka = []
        while True:
            aka_name = input(f"aka {character}")
            if aka_name:
                aka.append(aka_name)
            else:
                break
        if aka:
            d["aka"] = aka
        obj["characters"].append(d)
    
    background = ""
    while background.lower() not in ["y", "yes", "n", "no"]:
        background = input("background? ")
    
    if background.lower() in ["y", "yes"]:
        background = []
        while True:
            if is_end():
                break
            url = nonempty_input("url: ")
            start_time = nonempty_input("start_time")
            end_time = nonempty_input("end_time")
            type_ = input("type [default = song]:") or "song"
            background.append({
                "url": url,
                "start_time": start_time,
                "end_time": end_time,
                "type": type_})
        if background:
            obj["background"] = background

    write_yaml(obj, args.path)


if __name__ == '__main__':
    main(parse_args())
