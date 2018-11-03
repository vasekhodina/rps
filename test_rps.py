import rps
import pytest
import subprocess
import sys

def test_rock_is_valid_input():
    assert rps.is_valid_input('rock') is True

def test_paper_is_valid_input():
    assert rps.is_valid_input('paper') is True

def test_scissors_is_valid_input():
    assert rps.is_valid_input('scissors') is True

def test_blabla_not_valid_input():
    assert rps.is_valid_input('blabla') is False

def test_one_not_valid_input():
    assert rps.is_valid_input('1') is False

def test_generate_computer_play_is_valid():
    for _ in range(5000):
        assert rps.is_valid_input(rps.generate_computer_play())
    
def test_generate_is_random_enough():
    plays = [rps.generate_computer_play() for _ in range(6000)]
    rocks = plays.count('rock')
    papers = plays.count('paper')
    scissors = plays.count('scissors')
    print(rocks, papers, scissors)
    assert rocks > (6000/3 - 100)
    assert papers > (6000/3 - 100)
    assert scissors > (6000/3 - 100)

def test_is_rock_rock_tie():
    assert rps.evaluate('rock', 'rock') == 'tie'

def test_is_paper_paper_tie():
    assert rps.evaluate('paper', 'paper') == 'tie'

def test_is_scissors_scissors_tie():
    assert rps.evaluate('scissors', 'scissors') == 'tie'

def test_paper_beats_rock():
    assert rps.evaluate('paper', 'rock') == 'human'

def test_rock_beats_scissors():
    assert rps.evaluate('rock', 'scissors') == 'human'

def test_scissors_beats_paper():
    assert rps.evaluate('scissors', 'paper') == 'human'

def test_rock_computer_wins():
    assert rps.evaluate('scissors', 'rock') == 'computer'

def test_paper_computer_wins():
    assert rps.evaluate('rock', 'paper') == 'computer'

def test_scissors_computer_wins():
    assert rps.evaluate('paper', 'scissors') == 'computer'

def test_evaluate_wrong_input():
    assert rps.evaluate('lizard', 'paper') is None


def input_faked_paper(prompt):
    print(prompt)
    return 'paper'

def test_full_game_paper(capsys):
    rps.main(input_faked_paper)
    captured = capsys.readouterr()
    assert 'rock, paper or scissors? ' in captured.out

def test_wrong_play_results_in_repeated_question():
    cp = subprocess.run([sys.executable, 'rps.py'], encoding='utf-8', stdout=subprocess.PIPE,
                        check=True, input='fake\nrock\n')
    assert cp.stdout.count('rock, paper or scissors? ') == 2

def test_fail():
    assert False

#@pytest.fixture
#def fake_input_scissors(monkeypatch):
#    monkeypatch.setattr('builtins.input', input_faked_scissors)

#def test_full_game_scissors(capsys, fake_input_scissors):
#    rps.main()
#    captured = capsys.readouterr()
#    assert 'rock, paper or scissors? ' in captured.out
