# _*_ encoding: utf-8 _*_
import pytest


def test_parse_class():
    """Test correct tuple is returned when parsing a css target."""
    from arg_parser import parse
    assert parse('.target') == ('class', 'target')


def test_parse_class_small():
    """Test correct tuple is returned when parsing a small word."""
    from arg_parser import parse
    assert parse('.t') == ('class', 't')


def test_parse_class_empty():
    """Test error is thrown when the 'word'
    is only the lenght of the css targeter."""
    from arg_parser import parse
    with pytest.raises(TypeError):
        parse('.')


def test_parse_single_letter():
    """Test error is thrown when the 'word'
    is only a singular character and is not a css targeter."""
    from arg_parser import parse
    with pytest.raises(TypeError):
        parse('k')


def test_parse_id():
    """Test correct tuple is returned when parsing a class css target."""
    from arg_parser import parse
    assert parse('#target') == ('id', 'target')


def test_error():
    """Test correct error is raised when targets are not defined correctly."""
    from arg_parser import parse
    with pytest.raises(TypeError):
        parse('target')


def test_parse_id_empty():
    """Test error is thrown when the 'word'
    is only the lenght of the css targeter."""
    from arg_parser import parse
    with pytest.raises(TypeError):
        parse('#')
