"""User model"""
from sqlalchemy import Column, Integer, BigInteger, ForeignKey, Float, VARCHAR
from models.db import Model
from models.base_object import BaseObject
import numpy


class GameBlocks(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    game_id             = Column(Integer,nullable=False)
    block_number        = Column(Integer,nullable=False)
    block_type          = Column(VARCHAR(length=100),nullable=False)
    block_feedback      = Column(Integer,nullable=False)
    reward_1            = Column(VARCHAR(length=1000),nullable=False)
    reward_2            = Column(VARCHAR(length=1000),nullable=False)
    reward_3            = Column(VARCHAR(length=1000))
    reward_4            = Column(VARCHAR(length=1000))

    th_reward_1         = Column(VARCHAR(length=1000),nullable=False)
    th_reward_2         = Column(VARCHAR(length=1000),nullable=False)
    th_reward_3         = Column(VARCHAR(length=1000))
    th_reward_4         = Column(VARCHAR(length=1000))


    position1            = Column(VARCHAR(length=1000),nullable=False)
    position2            = Column(VARCHAR(length=1000),nullable=False)
    position3            = Column(VARCHAR(length=1000))
    position4            = Column(VARCHAR(length=1000))


    reward_upleft         = Column(VARCHAR(length=1000),nullable=False)
    reward_upright        = Column(VARCHAR(length=1000),nullable=False)
    reward_lowleft        = Column(VARCHAR(length=1000))
    reward_lowright       = Column(VARCHAR(length=1000))

    maxreward           = Column(Float(23),nullable=False)
    chance              = Column(Float(23),nullable=False)
    
    def get_id(self):
        return str(self.id)

    def get_game_id(self):
        return str(self.game_id)

    def get_block_number(self):
        return str(self.block_number)

    def get_block_type(self):
        return str(self.block_type)

    def get_reward_1(self):
        return str(self.reward_1)

    def get_reward_2(self):
        return str(self.reward_2)

    def get_reward_3(self):
        return str(self.reward_3)

    def get_reward_4(self):
        return str(self.reward_4)

    def get_reward_1_th(self):
        return str(self.th_reward_1)

    def get_reward_2_th(self):
        return str(self.th_reward_2)

    def get_reward_3_th(self):
        return str(self.th_reward_3)

    def get_reward_4_th(self):
        return str(self.th_reward_4)


    def get_reward_upleft(self):
        return str(self.reward_upleft)

    def get_reward_upright(self):
        return str(self.reward_upright)

    def get_reward_lowleft(self):
        return str(self.reward_lowleft)

    def get_reward_lowright(self):
        return str(self.reward_lowright)

    def get_position1(self):
        return str(self.position1)

    def get_position2(self):
        return str(self.position2)

    def get_position3(self):
        return str(self.position3)

    def get_position4(self):
        return str(self.position4)

    def get_block_feedback(self):
        return str(self.block_feedback)

    def get_maxreward(self):
        return str(self.maxreward)

    def get_chance(self):
        return str(self.chance)


    def errors(self):
        errors = super(GameBlocks, self).errors()
        return errors


