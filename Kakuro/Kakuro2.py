import time
import copy
# Kakuro CSP solver
# Python 3.10.0
# Author: Isaiah Jarvis A00439675
# this program takes a kakuro puzzle as input and outputs the solved puzzle
# by making it a CSP and solving it with backtracking search
# run the program with run() 


# constraint variable
class Constraint():
    def __init__(self, row, col, num, direction):
        self.row = row
        self.col = col
        self.num = num
        self.direction = direction
        self.nodes = []

# node variable
class Var():
    def __init__(self, pos, num):
        self.pos = pos
        self.num = num
        self.constH = Constraint(0, 0, 0, 'a')
        self.constV = Constraint(0, 0, 0, 'a')
        self.domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.rollBack = []

# finds the next var to execute on whether MRV or not
def find(grid, bools):
    if bools[4]:
        return MRV(grid)
    else:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j].num == '0':
                    pos = i, j
                    return pos
    return None

# finds the range of the constraint (from the constraints initial block to next #)
def find_rect(grid, const):
    for x in const:
        # if horizontal
        if x.direction == 'h':
            i = x.row-1
            for j in range(x.col, len(grid[0])):
                if grid[i][j].num != '#':
                    x.nodes.append((i, j))
        #if vertical
        elif x.direction == 'v':
            j = x.col-1
            for i in range(x.row, len(grid)):
                if grid[i][j].num != '#':
                    x.nodes.append((i, j))
    return 0
            
# creates the CSP
def get_csp():
    f = open(input("Enter file name: "))

    #initialize bools
    FC = False
    AC3 = False
    MAC = False
    NC = False
    MRV = False
    LCV = False

    # get bools
    if 'True' in f.readline():
        FC = True
        print(f'FC: {FC}')
    if 'True' in f.readline():
        AC3 = True
        print(f'AC3: {AC3}')
    if 'True' in f.readline():
        MAC = True
        print(f'MAC: {MAC}')
    if 'True' in f.readline():
        NC = True
        print(f'NC: {NC}')
    if 'True' in f.readline():
        MRV = True
        print(f'MRV: {MRV}')
    if 'True' in f.readline():
        LCV = True
        print(f'LCV: {LCV}')
    bools = [FC, AC3, MAC, NC, MRV, LCV]

    # get rows and cols
    temp = f.readline()
    rows = int(temp[temp.index('=') + 1:])
    temp = f.readline()
    cols = int(temp[temp.index('=') + 1:])

    # create grid for storing variables
    grid = [[Var for i in range(rows)] for j in range(cols)]

    # read in and place variables
    for i in range(rows):
        temp = f.readline()
        temp = temp.replace(',', '')
        for j in range(cols):
            grid[i][j] = Var((i, j), temp[j])

    # print initial trees
    for i in range(rows):
        for j in range(cols):
            print(grid[i][j].num, end='')
        print()

    # read in constraints and place them in list
    const = list()
    f.readline()
    temp = f.readline()
    while (temp != ''):
        trow = temp[:temp.index(',')]
        temp = temp[temp.index(',')+1:]
        tcol = temp[:temp.index(',')]
        temp = temp[temp.index(',')+1:]
        tnum = temp[:temp.index(',')]
        temp = temp[temp.index(',')+1:temp.index(',')+2]
        tlet = temp
        temp_const = Constraint(int(trow), int(tcol), int(tnum), str(tlet))
        const.append(temp_const)
        temp  = f.readline()

    # create row and col groups
    find_rect(grid, const)

    # give vars constraints
    for i in range(1, rows):
        for j in range(1, cols):
            for x in const:
                if x.direction == 'h' and grid[i][j].pos in x.nodes:
                    grid[i][j].constH = x
                if x.direction == 'v' and grid[i][j].pos in x.nodes:
                    grid[i][j].constV = x
    # close file and return grid and bools as a tuple
    f.close
    return grid, bools

# begins backtracking search
def backtracking_search(grid, bools):
    return backtrack(grid, bools)

# recursive backtracking call
def backtrack(grid, bools):
    # finds next var
    found = find(grid, bools)
    bruh = []
    if found == None:
        print('complete')
        return True
    else:
        row, col = found

    # if not using LCV do normal backtracking
    if bools[5]:
        lcv = LCV(grid, (row, col))
        for x in lcv:
            bruh.append(x[0])
        dom = bruh
    else:
        dom = grid[row][col].domain
    for i in dom:
        # if check violations returns true there are no constraints being violated
        grid[row][col].num = i
        if check_violations(grid, i,(row, col)):
            if bools[2]:
                if not (MAC(grid, (row, col))):
                    rollbackMAC(grid, (row, col))
                    grid[row][col].num = '0'
                    continue
            # if using forward checking
            elif bools[0]:
                # if forward checking reduces the domain of another var to 0 rollback and backtrack
                if not (forward_check(grid, i, (row, col))):
                    rollback(grid, i, (row, col))
                    grid[row][col].num = '0'
                    continue 
            # call backtrack and if the succeeds return true
            if backtrack(grid, bools):
                return True
            #if backtrack fails roll back inferences
            if bools[0] and not bools[2]:
                rollback(grid, i, (row, col))
            elif bools[2]:
                rollbackMAC(grid, (row, col))
        # if theres a violation reset num
        grid[row][col].num = '0'
    return False

# tries to prune domains of neighbors and if the domain is pruned to 0 returns a fail
def forward_check(grid, num, pos):
    # variables 
    row, col = pos
    enterH = False
    enterV = False
    totalH = 0
    totalV = 0
    count = 0

    # checks if there is just 1 remaining spot open in horizontal and/or vertical groups
    # aswell as saving anything that is likely to get changed (=='0' means unassigned)
    # horizontal
    for var in grid[row][col].constH.nodes:
        x, y = var
        if grid[x][y].num == '0' and (x, y) != (row, col):
            grid[x][y].rollBack.insert(0, copy.copy(grid[x][y].domain))
            count += 1
    if count == 1:
        enterH = True

    # vertical
    count = 0
    for var in grid[row][col].constV.nodes:
        x, y = var
        if grid[x][y].num == '0' and (x, y) != (row, col):
            grid[x][y].rollBack.insert(0, copy.copy(grid[x][y].domain))
            count += 1
    if count == 1:
        enterV = True
        
    # for each direction check and remove inconsistent vals
    # horizontal
    for var in grid[row][col].constH.nodes:
        x, y = var
        # for checking if the last unassigned var's domain fits constraint
        if grid[x][y].num == '0' and enterH:
            for number in grid[x][y].constH.nodes:
                i, j = number
                if grid[i][j].num != '0':
                    totalH += grid[i][j].num
            for number in copy.copy(grid[x][y].domain):
                if number + totalH != grid[x][y].constH.num:
                    grid[x][y].domain.remove(number)
            if num in grid[x][y].domain:
                    grid[x][y].domain.remove(num)
        # if row has more than 1 unassigned just prune for alldiff
        elif grid[x][y].num == '0':
            if num in grid[x][y].domain:
                grid[x][y].domain.remove(num)
        # if a vars domain is pruned too far return false
        if len(grid[x][y].domain) == 0:
            return False           

    # vertical
    for var in grid[row][col].constV.nodes:
        x, y = var
        # for checking if the last unassigned var's domain fits constraint
        if grid[x][y].num == '0' and enterV:
            for number in grid[x][y].constV.nodes:
                i, j = number
                if grid[i][j].num != '0':
                    totalV += grid[i][j].num
            for number in copy.copy(grid[x][y].domain):
                if number + totalV != grid[x][y].constV.num:
                    grid[x][y].domain.remove(number)
            if num in grid[x][y].domain:
                    grid[x][y].domain.remove(num)
        # if row has more than 1 unassigned just prune for alldiff
        elif grid[x][y].num == '0':
            if num in grid[x][y].domain:
                grid[x][y].domain.remove(num)
        # if a vars domain is pruned too far return false
        if len(grid[x][y].domain) == 0:
            return False
    return True

def rollback(grid, num, pos):
    # variables
    row, col = pos

    # if var is unassigned its domain may have been pruned so rollback
    # horizontal
    for var in grid[row][col].constH.nodes:
        x, y = var
        if grid[x][y].num == '0' and (x, y) != (row, col):
            grid[x][y].domain = grid[x][y].rollBack.pop(0)
            

    # veritcal 
    for var in grid[row][col].constV.nodes:
        x, y = var
        if grid[x][y].num == '0' and (x, y) != (row, col):
            grid[x][y].domain = grid[x][y].rollBack.pop(0)

def AC3(grid):
    # arc to store vals
    arcs = set()

    # makes arcs
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            # if not an edge piece/constraint square
            if grid[i][j].num != '#':
                # make arcs for each pair in groups
                for x in grid[i][j].constH.nodes:
                    if x != (i, j):
                        arcs.add((grid[i][j].pos, x, 'h'))
                for x in grid[i][j].constV.nodes:
                    if x != (i, j):
                        arcs.add((grid[i][j].pos, x, 'v'))

    #
    while len(arcs) != 0:
        x = arcs.pop()
        if RIV(grid, x):
            i, j = x[0]
            for z in grid[i][j].constH.nodes:
                if z != (i, j):
                    arcs.add((grid[i][j].pos, z, 'h'))
            for z in grid[i][j].constV.nodes:
                if z != (i, j):
                    arcs.add((grid[i][j].pos, z, 'v'))
        


# checks sum constraint by assuming any other node is at the highest possible
# values and seeing what the smallest option is and reducing the domain by anything smaller
def RIV(grid, arc):
    # intialize variables
    removed = False
    i, j = arc[0]
    x, y = arc[1]
    rowTotal = 0
    count = 9
    total = 0
    consistent = False
    diff = True

    # counts how many variables that arent the given var are in the group
    # this function works by assuming any other varaibles in the row are at the
    # highest they could be other than the given edges (for every var in the
    # group that isnt in the arc add count then decrement)
    # if horizontal
    if arc[2] == 'h':
        total = grid[i][j].constH.num
        for var in grid[i][j].constH.nodes:
            if var not in arc:
                # count total excluding the pairs in arc
                rowTotal += count
                count -= 1
    # if vertical
    if arc[2] == 'v':
        total = grid[i][j].constV.num
        for var in grid[i][j].constV.nodes:
            if var not in arc:
                # count total excluding the pairs in arc
                rowTotal += count
                count -= 1

    # checks for inconsistencies for each number in grid[i][j] by using the count
    # to determine the range of valid numbers are left then checks if any of the
    # lower numbers added with the total is >= to total
    # anything larger than count is consistent using just this constraint because
    # this just considers the range of numbers that are large enough to add up to
    # or exceed the total, the first number that fits can = total is the smallest
    # allowable value so the rest of the domain is consistent with the sum constraint
    for num in grid[i][j].domain:
        consistent = False
        # for each number in grid[x][y] domain if num + z + rowtotal
        for z in grid[x][y].domain:
            if num + z + rowTotal >= total and z < 10 - (9 - count):
                consistent = True
                break

        # if the number is in grid[x][y] domain and the length is 1 than it is
        # the only thing in that domain and should be pruned from grid[i][j]
        if num in grid[x][y].domain and len(grid[x][y].domain) == 1:
            diff = False
        # remove number if inconsistent 
        if consistent == False or diff == False:
            grid[i][j].domain.remove(num)
            removed = True

    return removed
        
def MAC(grid, pos):
    # arc to store vals and unpack position
    arcs = set()
    i, j = pos
    # add each arc from grid[i][j] constraint groups to arcs
    # horizontal
    for x in grid[i][j].constH.nodes:
        z, y = x
        if x != (i, j) and grid[z][y].num == '0':
            # save in grid[z][y] for rollback
            grid[z][y].rollBack.insert(0, copy.copy(grid[z][y].domain))
            arcs.add((x, grid[i][j].pos,'h'))
    # vertical
    for x in grid[i][j].constV.nodes:
        z, y = x
        if x != (i, j) and grid[z][y].num == '0':
            # save in grid[z][y] for rollback
            grid[z][y].rollBack.insert(0, copy.copy(grid[z][y].domain))
            arcs.add((x, grid[i][j].pos, 'v'))

    # while arcs isnt empty keep callin RIV() and adding the changed arcs to arcs
    while len(arcs) != 0:
        # retrieve arc
        x = arcs.pop()
        # call RIV with grid and the arc
        if RIV(grid, x):
            # unpack first var and check whether its empty after RIV()
            i, j = x[0]
            # if empty return false
            if grid[i][j].domain == '0':
                return False
            # add arcs for x[0] as it was changed
            for z in grid[i][j].constH.nodes:
                if z != (i, j):
                    arcs.add((grid[i][j].pos, z, 'h'))
            for z in grid[i][j].constV.nodes:
                if z != (i, j):
                    arcs.add((grid[i][j].pos, z, 'v'))
    return True

def rollbackMAC(grid, pos):
    i, j = pos
    # loops through all the values that MAC changed and rollsback the saved domain
    # horizontal
    for x in grid[i][j].constH.nodes:
        z, y = x
        if x != (i, j) and grid[z][y].num == '0':
            grid[z][y].domain = grid[z][y].rollBack.pop(0)
    # vertical
    for x in grid[i][j].constV.nodes:
        z, y = x
        if x != (i, j) and grid[z][y].num == '0':
            grid[z][y].domain = grid[z][y].rollBack.pop(0)

def MRV(grid):
    # initialize minVal and smallest domain
    minVal = 10
    smallestDom = None
    # for each variable check if its domain is the smallest then return it if yes
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            if len(grid[i][j].domain) < minVal and grid[i][j].num == '0':
                minVal = len(grid[i][j].domain)
                smallestDom = i, j
    return smallestDom
                

def LCV(grid, pos):
    # initialize position variables and domain list
    i, j = pos
    dom = list()
    # for each number in the domain of grid[i][j] check what will reduce neighbor
    # domains the least and return a sorted list in that order
    for num in grid[i][j].domain:
        count = 0
        # check horizontal groups
        for z in grid[i][j].constH.nodes:
            x, y = z
            if num in grid[x][y].domain:
                count += 1

        # check vertical groups
        for z in grid[i][j].constV.nodes:
            x, y = z
            if num in grid[x][y].domain:
                count += 1
        # append num and count to dom
        dom.append((num, count))
    # sort and return list
    return sorted(dom, key=lambda x: x[1])
    

def check_violations(grid, num, pos):
    # variables
    row, col = pos
    totalH = 0
    totalV = 0
    notfullH = False
    notfullV = False

    # check if there are any unassigned vars
    # horizontal
    for x in grid[row][col].constH.nodes:
        z, y = x
        if grid[z][y].num == '0':
            notfullH = True

    # vertical
    for x in grid[row][col].constV.nodes:
        z, y = x
        if grid[z][y].num == '0':
            notfullV = True

    # if no var in row or col groups is unassigned check that row/col adds up
    # to the total
    # horizontal
    if notfullH == False:
        for x in grid[row][col].constH.nodes:
            z, y = x
            totalH += int(grid[z][y].num)
        if totalH != int(grid[row][col].constH.num):
            return False

    # vertical
    if notfullV == False:
        for x in grid[row][col].constV.nodes:
            z, y = x
            totalV += int(grid[z][y].num)
        if totalV != int(grid[row][col].constV.num):
            return False
            
    # check all diff horizontally

    for x in grid[row][col].constH.nodes:
        rowx, colx = x
        if grid[row][col].pos != grid[rowx][colx].pos and grid[row][col].num == grid[rowx][colx].num:
            return False

    # check all diff vertically
    
    for x in grid[row][col].constV.nodes:
        rowx, colx = x
        if grid[row][col].pos != grid[rowx][colx].pos and grid[row][col].num == grid[rowx][colx].num:
            return False
        
    return True

def run():
    # set start time
    st = time.process_time()

    # make grid and do preprocessing step if selected
    grid, bools = get_csp()
    if bools[1]:
        AC3(grid)
    # run backtracking search
    backtracking_search(grid, bools)

    # print finished tree
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j].num, end='')
        print()

    # record execution time
    et = time.process_time()
    print(f'processing time is: {et-st}')

run()
input('Press enter to end')
