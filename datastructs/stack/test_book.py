import pytest
import stack

def test_push():
    colors = stack.Stack()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2

def test_pop():
    colors = stack.Stack()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None

def test_top():
    colors = stack.Stack()
    colors.push("Cadmium Red Light")
    assert colors.top() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.top() == "Hansa Yellow"
    colors.push("Pthalo Green")
    assert colors.top() == "Pthalo Green"

