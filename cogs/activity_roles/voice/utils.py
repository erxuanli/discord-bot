import time
import json

def user_all_time(serverid: str, userid: str) -> float: # returns all time vc stats of user in seconds
        with open("user_voice_stats.json", "r") as file:
            stats = json.loads(json.load(file))
            if serverid not in stats:
                return 0.0
            elif userid not in stats[serverid]:
                return 0.0
            elif len(stats[serverid][userid]["jlvc"]) == 0:
                return 0.0
            else:
                res = 0.0
                for i in stats[serverid][userid]["jlvc"]:
                    if len(i) != 2:
                        pass
                    else:
                        res += i[1] - i[0]
                return res

def user(serverid: str, userid: str, lookback_days: int) -> float: # returns the stats of the last lookback_days days of an user in seconds
    diff = time.time() - (lookback_days * 24 * 60 * 60)
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if serverid not in stats:
            return 0.0
        elif userid not in stats[serverid]:
            return 0.0
        elif len(stats[serverid][userid]["jlvc"]) == 0:
            return 0.0
        else:
            res = 0.0
            for i in reversed(stats[serverid][userid]["jlvc"]):
                if len(i) != 2:
                    pass
                else:
                    if i[1] <= diff:
                        return res
                    elif i[0] < diff:
                        res += i[1] - diff
                        return res
                    else:
                        res += i[1] - i[0]
            return res

def user_all_time_global(userid: str) -> float: # returns the sum of all time vc stats of user in all servers in seconds
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if not stats: # no servers
            return 0.0
        else:
            res = 0.0
            for server in stats: 
                if len(stats[server]) == 0: # no members in server
                    pass
                else:
                    for user in stats[server]:
                        if user == userid:
                            if len(stats[server][user]["jlvc"]) == 0: # user has no stats
                                break
                            else:
                                for i in stats[server][user]["jlvc"]:
                                    if len(i) != 2:
                                        pass
                                    else:
                                        res += i[1] - i[0]
            return res

def user_global(userid: str, lookback_days: int) -> float: # returns the sum of all user vc stats in all servers of the last lookback_days days in seconds
    diff = time.time() - (lookback_days * 24 * 60 * 60)
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if not stats: # no servers
            return 0.0
        else:
            res = 0.0
            for server in stats: 
                if len(stats[server]) == 0: # no members in server
                    pass
                else:
                    for user in stats[server]:
                        if user == userid:
                            if len(stats[server][user]["jlvc"]) == 0: # user has no stats
                                break
                            else:
                                for i in reversed(stats[server][user]["jlvc"]):
                                    if len(i) != 2:
                                        pass
                                    else:
                                        if i[1] <= diff:
                                            break
                                        elif i[0] < diff:
                                            res += i[1] - diff
                                            break
                                        else:
                                            res += i[1] - i[0]
            return res

def user_all_time_top(serverid: str, quan: int = 0) -> list: # returns top quan vc stats users of a specific server
    res = list()
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if serverid not in stats: # no servers
            return []
        elif not stats[serverid]: # no members in server
            return []
        else:
            for member in stats[serverid]:
                res.append([self.user_all_time(serverid, member), member])
    if quan == 0:
        return sorted(res, reverse=True)
    return sorted(res, reverse=True)[:quan]

def user_top(serverid: str, quan: int = 0, lookback_days: int = 14) -> list: # returns top quan vc stats users of a specific server of the last lookback_days days
    res = list()
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if serverid not in stats: # no servers
            return []
        elif not stats[serverid]: # no members in server
            return []
        else:
            for member in stats[serverid]:
                res.append([self.user(serverid, member, lookback_days), member])
    if quan == 0:
        return sorted(res, reverse=True)
    return sorted(res, reverse=True)[:quan]

def user_all_time_global_top(quan: int = 0) -> list: # returns top quan vc stats users (global) (bots included)
    users = list()
    res = list()

    # collect all users
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if not stats: # no servers
            return []
        else:
            for server in stats:
                if len(stats[server]) == 0: # no members in server
                    pass
                else:
                    for user in stats[server]:
                        users.append(user)

    for user in set(users):
        res.append([self.user_all_time_global(user), user])

    if quan == 0:
        return sorted(res, reverse=True)
    return sorted(res, reverse=True)[:quan]

def user_global_top(quan: int = 0, lookback_days: int = 14) -> list: # returns top quan vc stats users (global) (bots included) of the last lookback_days days
    users = list()
    res = list()

    # collect all users
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if not stats: # no servers
            return []
        else:
            for server in stats:
                if len(stats[server]) == 0: # no members in server
                    pass
                else:
                    for user in stats[server]:
                        users.append(user)

    for user in set(users):
        res.append([self.user_global(user, lookback_days), user])

    if quan == 0:
        return sorted(res, reverse=True)
    return sorted(res, reverse=True)[:quan]

def server_all_time_top(quan: int = 0) -> list: # returns top quan vc stats servers (global) (bots included in calculation)
    res = list()
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if not stats: # no servers
            return []
        for server in stats:
            res.append([self.sum_user_all_time(server), server])
    if quan == 0:
        return sorted(res, reverse=True)
    return sorted(res, reverse=True)[:quan]

def server_top(quan: int = 0, lookback_days: int = 14) -> list: # returns top quan vc stats servers (global) (bots inclued in calculation) of the last lookback_days days
    res = list()
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if not stats: # no servers
            return []
        for server in stats:
            res.append([self.sum_user(server, lookback_days), server])
    if quan == 0:
        return sorted(res, reverse=True)
    return sorted(res, reverse=True)[:quan]

def sum_user_all_time(serverid: str) -> float: # returns the sum of vc stats of all user of a specific server
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if not stats: # no servers
            return 0.0
        elif serverid not in stats:
            return 0.0
        elif not stats[serverid]: # no members in server
            return 0.0
        else:
            res = 0.0
            for member in stats[serverid]:
                res += self.user_all_time(serverid, member)
            return res

def sum_user(serverid: str, lookback_days: int = 14) -> float: # returns the sum of vc stats of all user of a specific server of the last lookback_days days
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if not stats: # no servers
            return 0.0
        elif serverid not in stats:
            return 0.0
        elif not stats[serverid]: # no members in server
            return 0.0
        else:
            res = 0.0
            for member in stats[serverid]:
                res += self.user(serverid, member, lookback_days)
            return res
                

def user_all_time_joins(serverid: str, userid: str) -> int: # returns all time vc user joins
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if serverid not in stats:
            return 0
        elif userid not in stats[serverid]:
            return 0
        elif len(stats[serverid][userid]["jlvc"]) == 0:
            return 0
        else:
            res = 0
            for i in stats[serverid][userid]["jlvc"]:
                if len(i) == 1 or len(i) == 2:
                    res += 1
            return res

def user_joins(serverid: str, userid: str, lookback_days: int = 14) -> int: # returns vc user joins of the last lookback_days days
    diff = time.time() - (lookback_days * 24 * 60 * 60)
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if serverid not in stats:
            return 0
        elif userid not in stats[serverid]:
            return 0
        elif len(stats[serverid][userid]["jlvc"]) == 0:
            return 0
        else:
            res = 0
            for i in reversed(stats[serverid][userid]["jlvc"]):
                if len(i) == 1 or len(i) == 2:
                    if i[0] < diff:
                        return res
                    res += 1
            return res

def user_all_time_joins_global(userid: str) -> int: # returns all time vc user joins global (all servers)
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if not stats: # no servers
            return 0
        else:
            res = 0
            for server in stats: 
                if len(stats[server]) == 0: # no members in server
                    pass
                else:
                    for user in stats[server]:
                        if user == userid:
                            if len(stats[server][user]["jlvc"]) == 0: # user has no stats
                                break
                            else:
                                for i in stats[server][user]["jlvc"]:
                                    if len(i) == 1 or len(i) == 2:
                                        res += 1
            return res

def user_joins_global(userid: str, lookback_days: int = 14) -> int: # returns all time vc user joins global (all servers) of the last lookback_days days
    diff = time.time() - (lookback_days * 24 * 60 * 60)
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if not stats: # no servers
            return 0
        else:
            res = 0
            for server in stats: 
                if len(stats[server]) == 0: # no members in server
                    pass
                else:
                    for user in stats[server]:
                        if user == userid:
                            if len(stats[server][user]["jlvc"]) == 0: # user has no stats
                                break
                            else:
                                for i in reversed(stats[server][user]["jlvc"]):
                                    if len(i) == 1 or len(i) == 2:
                                        if i[0] < diff:
                                            break
                                        res += 1
            return res

def user_all_time_leaves(serverid: str, userid: str) -> int: # returns all time vc user leaves
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if serverid not in stats:
            return 0
        elif userid not in stats[serverid]:
            return 0
        elif len(stats[serverid][userid]["jlvc"]) == 0:
            return 0
        else:
            res = 0
            for i in stats[serverid][userid]["jlvc"]:
                if len(i) == 2:
                    res += 1
            return res

def user_leaves(serverid: str, userid: str, lookback_days: int = 14) -> int: # returns vc user leaves of the last lookback_days days
    diff = time.time() - (lookback_days * 24 * 60 * 60)
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if serverid not in stats:
            return 0
        elif userid not in stats[serverid]:
            return 0
        elif len(stats[serverid][userid]["jlvc"]) == 0:
            return 0
        else:
            res = 0
            for i in reversed(stats[serverid][userid]["jlvc"]):
                if len(i) == 2:
                    if i[1] < diff:
                        return res
                    res += 1
            return res

def user_all_time_leaves_global(userid: str) -> int: # returns all time vc user leaves global (all servers)
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if not stats: # no servers
            return 0
        else:
            res = 0
            for server in stats: 
                if len(stats[server]) == 0: # no members in server
                    pass
                else:
                    for user in stats[server]:
                        if user == userid:
                            if len(stats[server][user]["jlvc"]) == 0: # user has no stats
                                break
                            else:
                                for i in stats[server][user]["jlvc"]:
                                    if len(i) == 2:
                                        res += 1
            return res

def user_leaves_global(userid: str, lookback_days: int = 14) -> int: # returns vc user leaves global (all servers) of the last lookback_days days
    diff = time.time() - (lookback_days * 24 * 60 * 60)
    with open("user_voice_stats.json", "r") as file:
        stats = json.loads(json.load(file))
        if not stats: # no servers
            return 0
        else:
            res = 0
            for server in stats: 
                if len(stats[server]) == 0: # no members in server
                    pass
                else:
                    for user in stats[server]:
                        if user == userid:
                            if len(stats[server][user]["jlvc"]) == 0: # user has no stats
                                break
                            else:
                                for i in reversed(stats[server][user]["jlvc"]):
                                    if len(i) == 2:
                                        if i[1] < diff:
                                            break
                                        res += 1
            return res

def seconds_to_hours_minutes_seconds(seconds: float):
    ti = seconds
    hours = int(seconds // (60**2))
    ti -= hours*60**2
    minutes = int(ti // 60)
    ti -= minutes*60
    c_seconds = int(ti)
    return hours, minutes, c_seconds