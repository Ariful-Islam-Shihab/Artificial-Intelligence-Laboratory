nodes = [
    "A", "B", "C", "D", "E", 
    "F", "G", "H", "I", "J"
]

edges = {
    "A": ["B", "C", "D", "E"],
    "B": ["A", "C", "F", "G"],
    "C": ["A", "B", "H", "I"],
    "D": ["A", "E", "F", "H"],
    "E": ["A", "D", "G", "I"],
    "F": ["B", "D", "J"],
    "G": ["B", "E", "J"],
    "H": ["C", "D", "J"],
    "I": ["C", "E", "J"],
    "J": ["F", "G", "H", "I"]
}

available_colours = ["R", "G", "B"]


def reached(color_list):
    return all(len(colors) == 1 for colors in color_list.values())



def CSP(color_list):
    if reached(color_list):
        return color_list
    cur = min(
        (k for k in color_list if len(color_list[k]) > 1),
        key=lambda k: len(color_list[k])
    )
    for i in color_list[cur]:
        copied={k:v.copy() for k,v in color_list.items()}
        copied[cur]=[i]
        for j in edges[cur]:
            if i in copied[j]:
                copied[j].remove(i)
            if len(copied[j])==0:
                return False
        next=CSP(copied)
        if next:
            return next
        
    return False

color_list={
    i:[j for j in available_colours] for i in nodes
}


print(CSP(color_list))
