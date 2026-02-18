import pytest
from app.calculator import calculator

ERROR_MSG = "Invalid input. Please follow the format: <operation> <num1> <num2>"


def run_calculator_with_inputs(inputs, monkeypatch, capsys):
    it = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(it))

    with pytest.raises(SystemExit):
        calculator()

    return capsys.readouterr().out


# positive test cases
def test_add(monkeypatch, capsys):
    out = run_calculator_with_inputs(["add 2 3", "exit"], monkeypatch, capsys)
    assert "Result:" in out
    assert "AddCalculation" in out
    assert "= 5.0" in out


def test_subtract(monkeypatch, capsys):
    out = run_calculator_with_inputs(["subtract 9 4", "exit"], monkeypatch, capsys)
    assert "Result:" in out
    assert "SubtractCalculation" in out
    assert "= 5.0" in out


def test_multiply(monkeypatch, capsys):
    out = run_calculator_with_inputs(["multiply 4 5", "exit"], monkeypatch, capsys)
    assert "Result:" in out
    assert "MultiplyCalculation" in out
    assert "= 20.0" in out


def test_divide(monkeypatch, capsys):
    out = run_calculator_with_inputs(["divide 10 2", "exit"], monkeypatch, capsys)
    assert "Result:" in out
    assert "DivideCalculation" in out
    assert "= 5.0" in out


# negative test cases
def test_divide_by_zero(monkeypatch, capsys):
    out = run_calculator_with_inputs(["divide 5 0", "exit"], monkeypatch, capsys)
    assert "Cannot divide by zero" in out or "Division by zero" in out


def test_invalid_input(monkeypatch, capsys):
    out = run_calculator_with_inputs(["add two three", "exit"], monkeypatch, capsys)
    assert "Invalid input" in out


def test_invalid_arg_count(monkeypatch, capsys):
    out = run_calculator_with_inputs(["add 5", "exit"], monkeypatch, capsys)
    assert "Invalid input" in out


def test_calculator_invalid_operation(monkeypatch, capsys):
    out = run_calculator_with_inputs(["modulus 5 3", "exit"], monkeypatch, capsys)
    assert "Unsupported" in out or "Invalid operation" in out


def test_calculator_blank_input(monkeypatch, capsys):
    out = run_calculator_with_inputs(["", "exit"], monkeypatch, capsys)
    assert "Welcome" in out


def test_calculator_help_command(monkeypatch, capsys):
    out = run_calculator_with_inputs(["help", "exit"], monkeypatch, capsys)
    assert "Help" in out or "Usage" in out or "Commands" in out
