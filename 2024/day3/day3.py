import click
import numpy as np
import re
from pathlib import Path
import pytest
from math import prod

"""Solve advent of code puzzles in Python."""

def solve_puzzle_one(filename):

    with open(filename) as f:
        final_sum = 0
        for line in f:
            matches = re.findall(r'(mul\(\d+,\d+\))',line)
            for match in matches:
                final_sum += prod([int(x) for x in re.findall(r'\d+',match)])
    return final_sum

def solve_puzzle_two(filename):
    
    with open(filename) as f:
        final_sum = 0
        enabled = True
        for line in f:
            matches = re.findall(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', line)
            for match in matches:
                if re.search(r'do\(\)',match):
                    enabled = True
                elif re.search(r'don\'t\(\)',match):
                    enabled = False
                elif re.findall(r'(mul\(\d+,\d+\))',line) and enabled:
                    final_sum += prod([int(x) for x in re.findall(r'\d+',match)])

    return final_sum

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
    test_file = Path(__file__).with_name('test_2.txt').absolute()
    test_solution_file = Path(__file__).with_name('test_result_two.txt').absolute()

    result = solve_puzzle_two(test_file)
    with open(test_solution_file) as sol: 
        for i in sol:
            test_result = int(i) # fragile to poorly formed test results

    assert result == pytest.approx(test_result)
    


    
