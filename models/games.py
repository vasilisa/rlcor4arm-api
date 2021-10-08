"""User model"""
from sqlalchemy import Column, Integer, BigInteger, ForeignKey, DateTime, Float, VARCHAR

from models.db import Model
from models.base_object import BaseObject


class Games(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    game_id            = Column(Integer, nullable=False)
    block_number       = Column(Integer, nullable=False)
    block_feedback     = Column(Integer, nullable=False)
    symbol_1           = Column(VARCHAR(length=500), nullable=False) 
    symbol_2           = Column(VARCHAR(length=500), nullable=False)
    symbol_3           = Column(VARCHAR(length=500)) 
    symbol_4           = Column(VARCHAR(length=500))
    
    

    def get_id(self):
        return str(self.id)

    def get_game_id(self):
        return str(self.game_id)
    
    def get_block_number(self):
        return str(self.block_number)

    # sanity check not really used here 
    def get_block_feedback(self):
        return str(self.block_feedback)

    def get_symbol_1(self):
        return str(self.symbol_1)

    def get_symbol_2(self):
        return str(self.symbol_2)

    def get_symbol_3(self):
        return str(self.symbol_3)

    def get_symbol_4(self):
        return str(self.symbol_4)


    def errors(self):
        errors = super(Games, self).errors()
        return errors
 
     

