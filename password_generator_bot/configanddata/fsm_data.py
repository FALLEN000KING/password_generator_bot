from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

storage = MemoryStorage()

class FSM_pass(StatesGroup):
    number_of_pass = State()
    number_yes_or_no = State()
    yes_or_no_letters = State()
    is_caps = State()
    spec_simv = State()
    ending = State()