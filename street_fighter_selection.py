def street_fighter_Selection(fighters,pos,moves):
    r,row,col,m = [], pos[0], pos[1], {"up":(-1,0),"down":(1,0),"right":(0,1), "left":(0,-1)}
    for move in moves:
        row, col = min(max(row + m[move][0], 0), 1), (col + m[move][1]) % 6
        r.append(fighters[row][col])
    return r
