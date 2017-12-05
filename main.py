class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.color = None

    def __str__(self):
        return self.name

def degree(node):
    return len(node.neighbors)

def m_print(obj):
    if type(obj) is Node:
        foo = str(obj) + ":"
        for neighbor in obj.neighbors:
            foo = foo + " " + str(neighbor.name)
        print(foo)
    if type(obj) is list:   # when obj is graph
        for node in obj:
            m_print(node)

# removes node from graph with deg < degree
def remove_less_than(graph, degree):
    copy = []
    for node in graph:
        length = len(node.neighbors)
        if length >= degree:
            node_copy = Node(node.name)
            for neighbor in node.neighbors:
                length_b = len(neighbor.neighbors)
                if length_b >= degree:
                    node_copy.neighbors.append(neighbor)
            copy.append(node_copy)
    return copy

def remove(graph, node_a):
    copy = []
    for node_b in graph:
        if node_b.name != node_a.name:
            node_copy = Node(node_b.name)
            for neighbor in node_b.neighbors:
                if neighbor.name != node_a.name:
                    node_copy.neighbors.append(neighbor)
            copy.append(node_copy)
    return copy

def find_maxVertex(graph):
    maxVertex = Node('TEST')
    for node in graph:
        if degree(node) > degree(maxVertex):
            maxVertex = node
    return maxVertex

def greedy(graph):
    F = []

    graph = remove_less_than(graph, 2)

    while True:
        v = find_maxVertex(graph)
        F.append(v)
        graph = remove(graph, v)
        graph = remove_less_than(graph, 2)
        length = len(graph)
        if length == 0:
            break
    return F

def test1():
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    a.neighbors = [b, c, e]
    b.neighbors = [a, e, f]
    c.neighbors = [a, e, f]
    d.neighbors = [f]
    e.neighbors = [a, b, c, f]
    f.neighbors = [b, c, d, e]

    graph = [a, b, c, d, e, f]
    result = greedy(graph)
    for stuff in result:
        print(stuff)

def test2():
    AL = Node('AL')
    MO = Node('MO')
    AK = Node('AK')
    MT = Node('MT')
    AZ = Node('AZ')
    NE = Node('NE')
    AR = Node('AR')
    NV = Node('NV')
    CA = Node('CA')
    NH = Node('NH')
    CO = Node('CO')
    NJ = Node('NJ')
    CT = Node('CT')
    NM = Node('NM')
    DE = Node('DE')
    NY = Node('NY')
    DC = Node('DC')
    NC = Node('NC')
    FL = Node('FL')
    ND = Node('ND')
    GA = Node('GA')
    OH = Node('OH')
    HI = Node('HI')
    OK = Node('OK')
    ID = Node('ID')
    OR = Node('OR')
    IL = Node('IL')
    PA = Node('PA')
    IN = Node('IN')
    RI = Node('RI')
    IA = Node('IA')
    SC = Node('SC')
    KS = Node('KS')
    SD = Node('SD')
    KY = Node('KY')
    TN = Node('TN')
    LA = Node('LA')
    TX = Node('TX')
    ME = Node('ME')
    UT = Node('UT')
    MD = Node('MD')
    VT = Node('VT')
    MA = Node('MA')
    VA = Node('VA')
    MI = Node('MI')
    WA = Node('WA')
    MN = Node('MN')
    WV = Node('WV')
    MS = Node('MS')
    WI = Node('WI')
    WY = Node('WY')

    AL.neighbors = [GA, FL, MS, TN]
    AK.neighbors = []
    AZ.neighbors = [CA, NV, UT, CO, NM]
    AR.neighbors = [TX, OK, MO, TN, MS, LA]
    CA.neighbors = [OR, NV, AZ]
    CO.neighbors = [NM, AZ, UT, WY, NE, KS, OK]
    CT.neighbors = [RI, NY, MA]
    DE.neighbors = [MD, PA, NJ]
    DC.neighbors = [MD, VA]
    FL.neighbors = [GA, AL]
    GA.neighbors = [SC, NC, TN, AL, FL]
    HI.neighbors = []
    ID.neighbors = [WA, OR, NV, UT, WY, MT]
    IL.neighbors = [WI, IA, MO, KY, IN]
    IN.neighbors = [IL, KY, OH, MI]
    IA.neighbors = [MN, SD, NE, MO, IL, WI]
    KS.neighbors = [CO, OK, MO, NE]
    KY.neighbors = [MO, TN, VA, WV, OH, IN, IL]
    LA.neighbors = [TX, AR, MS]
    ME.neighbors = [NH]
    MD.neighbors = [DE, PA, WV, DC, VA]
    MA.neighbors = [RI, CT, NY, VT, NH]
    MI.neighbors = [OH, IN, WI]
    MN.neighbors = [WI, IA, SD, ND]
    MS.neighbors = [LA, AR, TN, AL]
    MO.neighbors = [KS, NE, IA, IL, KY, TN, AR, OK]
    MT.neighbors = [ID, WY, SD, ND]
    NE.neighbors = [WY, SD, IA, MO, KS, CO]
    NV.neighbors = [CA, OR, ID, UT, AZ]
    NH.neighbors = [ME, MA, VT]
    NJ.neighbors = [NY, PA, DE]
    NM.neighbors = [AZ, UT, CO, OK, TX]
    NY.neighbors = [PA, NJ, CT, MA, VT]
    NC.neighbors = [VA, TN, GA, SC]
    ND.neighbors = [MT, SD, MN]
    OH.neighbors = [PA, WV, KY, IN, MI]
    OK.neighbors = [TX, NM, CO, KS, MO, AR]
    OR.neighbors = [WA, ID, NV, CA]
    PA.neighbors = [NY, NJ, DE, MD, WV, OH]
    RI.neighbors = [CT, MA]
    SC.neighbors = [GA, NC]
    SD.neighbors = [WY, MT, ND, MN, IA, NE]
    TN.neighbors = [AR, MO, KY, VA, NC, GA, AL, MS]
    TX.neighbors = [NM, OK, AR, LA]
    UT.neighbors = [CO, NM, AZ, NV, ID, WY]
    VT.neighbors = [NY, MA, NH]
    VA.neighbors = [NC, TN, KY, WV, MD, DC]
    WA.neighbors = [ID, OR]
    WV.neighbors = [KY, OH, PA, MD, VA]
    WI.neighbors = [MN, IA, IL, MI]
    WY.neighbors = [ID, MT, SD, NE, CO, UT]

    graph = [AK, AL, AZ, AR, CA, CO, CT, DE,
            DC, FL, GA, HI, ID, IL, IN, IA, KS,
            KY, LA, ME, MD, MA, MI, MN, MS, MO,
            MT, NE, NV, NH, NJ, NM, NY, NC, ND,
            OH, OK, OR, PA, RI, SC, SD, TN, TX,
            UT, VT, VA, WA, WV, WI, WY]

    result = greedy(graph)
    for stuff in result:
        print(stuff)

if __name__ == "__main__":
    print("Test 1")
    test1()
    print("Test 2")
    test2()
