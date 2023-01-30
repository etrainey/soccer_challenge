# soccer_challenge

## Use
To run this script, use any of the following:
`cat <filename> | python3 soccer.py`
`python3 soccer.py < <filename>`
`python3 soccer.py <filename> <sort_style>`

### Args
Accepts args are defined in `config.json` and define how a result is sorted (and subsequently ranked).
Sorting can have primary, secondary, tertiary, etc priority.  Each sorting technique can be ascending (`false`) or descending (`true`)
In the `default` example, scores are sorted primarily on `points_total` in reverse order `true` and secondarily on `id` in reverse order `true`
"default" : [
        ["id", true],
        ["points_total", true]
    ]


## Improvements
- Testing
- Refactor some methods (`evaluate_results(), assign_rank(), write_results()`)
- Add method to easily configure output.  Would need to change config file format


## Things learned
- Basic testing
- Input from pipe (rather than defined in script or args)


## Time Spent
- 8 hours