import click
import numpy as np
import re
from pathlib import Path
import pytest

"""Solve advent of code puzzles in Python."""

def solve_puzzle_one(filename):

    result = 0
    return result


def solve_puzzle_two(filename):

    result = 0
    return result

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
    


    
