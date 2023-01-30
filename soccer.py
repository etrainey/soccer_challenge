import sys
import json

CONFIG_FILE = "config.json"


def get_config(config: str = "default") -> str:
    if len(sys.argv) > 2:
        return sys.argv[2]
    else:
        return config
    
def load_configs(config: str) -> str:
    with open(CONFIG_FILE, "r") as f:
        return json.load(f).get(config)


def get_input(file: str = None):
    if file or len(sys.argv) > 1:
        if file:
            source = file
        if len(sys.argv) > 1:
            source = sys.argv[1]
        data = []
        with open(source) as f:
            for line in f:
                data.append(line.rstrip())
    else:
        data = sys.stdin
    return data


def evaluate_results(data: list) -> dict:
    results = {}
    # Sample line format: [TeamA scoreA, Team B scoreB]
    for line in data:
        teams = line.split(",")
        team1 = teams[0].split()
        team2 = teams[1].split()
        score1 = int(team1.pop())
        score2 = int(team2.pop())
        name1 = " ".join(team1)
        name2 = " ".join(team2)
        team1_pts, team2_pts = get_pts(score1, score2)
        team1_diff, team2_diff = get_diff(score1, score2)
    
        append_results(results, name1, score1, team1_pts, team1_diff)
        append_results(results, name2, score2, team2_pts, team2_diff)
    return results


def get_pts(score1: int, score2: int) -> list:
    if score1 > score2:
        return [3, 0]
    if score1 < score2:
        return [0, 3]
    if score1 == score2:
        return [1, 1]


def get_diff(score1: int, score2: int) -> list:
    diff = score1 - score2
    return [diff, -diff]


def append_results(results: dict, team: str, score: int, pts: int, diff: int) -> None:
    if team not in results:
        create_empty_dict(results, team)
    results[team]["scores"].append(score)
    results[team]["points"].append(pts)
    results[team]["scores_diff"].append(diff)
    results[team]["scores_total"] += score
    results[team]["points_total"] += pts
    results[team]["scores_diff_total"] += diff


def create_empty_dict(results: dict, team: str) -> None:
    results[team] = {
            "id" : team,
            "scores" : [],
            "points" : [],
            "scores_diff" : [],
            "scores_total" : 0,
            "points_total" : 0,
            "scores_diff_total" : 0,
            "rank" : 0
        }


def sort(data: dict, config: list) -> dict:
    sorted_dict = data
    for item in config:
        style, reverse = item
        sorted_dict = sort_iteration(sorted_dict, data, style, reverse)
    return sorted_dict


def sort_iteration(sorted_dict: dict, data: dict, key: str, reverse: bool) -> dict:
    return sorted(sorted_dict, key=lambda x: data[x][key], reverse=reverse)


def assign_rank(sorted: list, results: dict, config: str) -> None:
    previous_points = 0
    previous_rank = 1
    for i, team in enumerate(sorted):
        score = results[team]["points_total"]
        if score == previous_points:
            results[team]["rank"] = previous_rank
        else:
            results[team]["rank"] = i + 1
            previous_rank = i + 1
            previous_points = results[team]["points_total"]


def write_results(results: dict, sorted: list) -> None:
    for team in sorted:
        id = results[team]["id"]
        rank = results[team]["rank"]
        pts_total = results[team]["points_total"]
        if pts_total == 1:
            point = "pt"
        else:
            point = "pts"
        print(f'{rank}. {id}, {pts_total} {point}')


def main():
    results = evaluate_results(get_input())
    config_name = get_config()
    configs = load_configs(config_name)
    sorted = sort(results, configs)
    assign_rank(sorted, results, config_name)
    write_results(results, sorted)


if __name__ == '__main__':
    main()