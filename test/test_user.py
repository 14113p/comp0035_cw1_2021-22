import pytest
from conftest import personal_data
from user import User
import datetime


def test_string_representation():
    '''
    GIVEN a new user
    WHEN the user class is used in a string
    THEN it returns a correct string, listing all of its elements that are not password
    '''
    valid_user = User('John', 'Brown', 'example@email.com', 'abc123', datetime.date(2020, 1, 1))
    assert str(valid_user) == ' John Brown example@email.com 2020-01-01'

def test_full_name_creation():
    '''
    GIVEN a new user
    WHEN create_full_name function is called
    THEN return a single string consisting of first name and surname
    '''
    valid_user = User('John', 'Brown', 'example@email.com', 'abc123', datetime.date(2020, 1, 1))
    assert valid_user.create_full_name() == 'John Brown'

    
def test_age_calculation_when_no_dob():
    '''
    GIVEN a call of calculate_age function
    WHEN the date of birth is not given
    THEN the function should return 'Age not calculated, date of birth unknown'
    '''
    valid_user = User('John', 'Brown', 'example@email.com', 'abc123')
    assert valid_user.calculate_age() == 'Age not calculated, date of birth unknown'

def test_password_hashing():
    '''
    GIVEN a new user with hashed password
    WHEN is_correct_function is called to check it against the unhashed password
    THEN return True if the passowrds match and False otherwise
    '''
    valid_user = User('John', 'Brown', 'example@email.com', 'abc123', datetime.date(2020, 1, 1))
    assert valid_user.is_correct_password( 'abc123' ) == True
    assert valid_user.is_correct_password( '123abc' ) == False