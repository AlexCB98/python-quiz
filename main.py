from random import choice
from data import questions

def format_data(question):
    data_q = question['question']
    data_a = question['a']
    data_b = question['b']

    return f'{data_q}\n Answer is: {data_a} or {data_b} ?'

