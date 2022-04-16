import os
import sys
from datetime import datetime


def get_center(typeStr, file):
    if typeStr == "file-creation-year":
        tick = os.path.getctime(file)
        return datetime.fromtimestamp(tick).strftime('%Y')

    elif typeStr == "file-creation-month":
        tick = os.path.getctime(file)
        return datetime.fromtimestamp(tick).strftime('%m')

    elif typeStr == "file-creation-day":
        tick = os.path.getctime(file)
        return datetime.fromtimestamp(tick).strftime('%d')

    elif typeStr == "file-modified-year":
        tick = os.path.getmtime(file)
        return datetime.fromtimestamp(tick).strftime('%Y')

    elif typeStr == "file-modified-month":
        tick = os.path.getmtime(file)
        return datetime.fromtimestamp(tick).strftime('%m')

    elif typeStr == "file-modified-day":
        tick = os.path.getmtime(file)
        return datetime.fromtimestamp(tick).strftime('%d')

    elif typeStr == "digit":
        return "#digit#"

    else:
        return "#type-failed#"


def simulate_replace(files, pattern, typeStr, formatStr):
    """置換のシミュレーション"""
    print("""
    Simulation
    ----------""")

    countOfSimulation = 0

    for i, file in enumerate(files):
        center = get_center(typeStr, file)
        basename = os.path.basename(file)
        result = pattern.match(basename)
        if result:
            # Matched

            # グループ数は２
            groupCount = len(result.groups())
            buf = f"({i+1}) {basename}"
            isUnmatched = False

            left = result.group(1)
            right = result.group(2)
            replaced = formatStr.format(left, right, center)

            print(f"({i+1}) {basename} --> {replaced}")
            countOfSimulation += 1

        else:
            # Unmatched
            pass

    print(f"""
    Count of simulation = {countOfSimulation}""")


def replace_file_names(files, pattern, typeStr, formatStr):
    """置換実行"""
    print("""
    Result
    ------""")

    # 置換実行
    for i, file in enumerate(files):
        center = get_center(typeStr, file)
        basename = os.path.basename(file)
        result = pattern.match(basename)
        if result:
            # Matched

            left = result.group(1)
            right = result.group(2)
            replaced = formatStr.format(left, right, center)

            oldPath = os.path.join(os.getcwd(), basename)
            newPath = os.path.join(os.getcwd(), replaced)
            print(f"({i})Rename {oldPath} --> {newPath}")
            os.rename(oldPath, newPath)
