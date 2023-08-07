def solution(players, callings):

    cur_players = {player : rank for rank, player in enumerate(players)}
    cur_rank = {rank : player for player, rank in cur_players.items()}   

    for i in callings:
        former = cur_rank[cur_players[i] - 1]
        cur_rank[cur_players[i] - 1] , cur_rank[cur_players[i]] = cur_rank[cur_players[i]] , cur_rank[cur_players[i] -1]
        cur_players[former], cur_players[i] = cur_players[i], cur_players[former]



    return list(dict(sorted(cur_rank.items())).values())

   
