def all(fp):
    """
    Retorna toda la coleccion de objetos (dict)
    :param fp:
    :type fp:
    :return:Lista iterable de objetos (dict)
    :rtype:list
    """
    import json

    try:
        stream = []

        with open(fp, "r") as streamReader:
            stream.extend(json.load(streamReader))

        return stream
    except IOError as error:
        print(error)
    finally:
        streamReader.close()


def get(key, fp):
    import json

    try:
        stream = []

        with open(fp, "r") as streamReader:
            stream.extend(json.load(streamReader))
            result = [item for item in stream if item.get("itemName") == key]

        return result
    except IOError as error:
        print(error)
    finally:
        streamReader.close()


def new(fp, dic=None):
    import json
    import os

    try:
        if not os.path.exists(os.path.dirname(fp)):
            os.makedirs(os.path.dirname(fp))

        with open(fp, "w+") as streamWriter:
            stream = []

            if not (dic is None or dic == ""):
                stream.append(dic)

            json.dump(stream, streamWriter, indent=2)
    except PermissionError as error:
        print(error)
    else:
        streamWriter.close()


def put(dic, fp):
    import os
    import json

    try:
        if not os.path.exists(fp):
            new(fp, dic)
        else:
            stream = []

            with open(fp, "r") as streamReader:
                stream.extend(json.load(streamReader))
                stream.append(dic)

                streamReader.close()

            try:
                with open(fp, "r+") as streamWriter:
                    json.dump(stream, streamWriter, indent=2)
                streamWriter.close()

            except PermissionError as error:
                print(error)
            except IOError as error:
                print(error)
    except IOError as error:
        print(error)


def delete(key, fp):
    import json

    try:
        stream = []

        with open(fp, "r") as streamReader:
            stream.extend(json.load(streamReader))

            for r in [s for s in stream if s == key]:
                stream.pop(stream.index(r))

            try:
                with open(fp, "w") as streamWriter:
                    json.dump(stream, streamWriter, indent=2)
            except IOError as error:
                print(error)
    except IOError as error:
        print(error)
    finally:
        streamReader.close()
        streamWriter.close()
