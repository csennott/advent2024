import click
import numpy as np
import re
from pathlib import Path
import pytest

"""Solve advent of code puzzles in Python."""

def line_is_safe(line):
    allowed = {1,2,3,-1,-2,-3}
    diffs = np.diff(np.fromstring(line,sep=' ',dtype=int))
    print(diffs)
    if not (np.all(diffs > 0) or np.all(diffs < 0)):
        return False
    if set(diffs).issubset(allowed):
        return True
    else: 
        return False


def solve_puzzle_one(filename):

    safe_reports = 0
    with open(filename) as f:
        for line in f:
            if line_is_safe(line):
                safe_reports += 1
            
    return safe_reports

def solve_puzzle_two(filename):
    safe_reports = 0
    allowed = {1,2,3,-1,-2,-3}

    with open(filename) as f:
        for line in f:
            for i,item in enumerate(line):
                #bullshit to avoid double-removing duplicates in line
                sublist = ' '.join([x for j, x in enumerate(line.split(' ')) if j != i])
                if line_is_safe(sublist):
                    safe_reports +=1
                    break #if any sublist is safe then the line is safe
            
    return safe_reports

@click.command()
@click.argument('filename')
@click.option('--a',
              type=click.Choice(['fp', 'sp'], case_sensitive=False),required=True)
def cli_function(filename,a):
    """Solve the puzzle."""

    if a == 'fp':
        result = solve_puzzle_one(filename)
        print(f'Puzzle one result: {result}')

    if a == 'sp':
        result = solve_puzzle_two(filename)
        print(f'Puzzle two result: {result}')

if __name__ == '__main__':
    cli_function()

## Tests
def test_puzzle_one():
    test_file = Path(__file__).with_name('test.txt').absolute()
    test_solution_file = Path(__file__).with_name('test_result_one.txt').absolute()

    result = solve_puzzle_one(test_file)
    with open(test_solution_file) as sol: 
        for i in sol:
            test_result = int(i) # fragile to poorly formed test results

    assert result == pytest.approx(test_result)

def test_puzzle_two():
    test_file = Path(__file__).with_name('test.txt').absolute()
    test_solution_file = Path(__file__).with_name('test_result_two.txt').absolute()

    result = solve_puzzle_two(test_file)
    with open(test_solution_file) as sol: 
        for i in sol:
            test_result = int(i) # fragile to poorly formed test results

    assert result == pytest.approx(test_result)
    


    
