from abc import ABC, abstractmethod
from mimetypes import init
from operator import mod
import numpy as np


class AlgoClass:
    def __init__(self, goal_sales_per_block, initial_price, number_of_blocks, update_freq, profit=0):
        self.goal_sales_per_block = goal_sales_per_block
        self.number_of_blocks = number_of_blocks
        self.price = initial_price
        self.block_arr = []
        self.profit = profit
        self.update_freq = update_freq
        self.current_wts = 0
        self.initial_price = initial_price
        self.current_ema = 0
        self.ema_index = 1
        
    def get_price(self):
        return self.price

    def calc_wts(self, most_recent_sales):
        ema = 0.2 * most_recent_sales + self.current_ema * (1 - 0.2)
        self.ema_index += 1
        self.current_ema = ema
        self.self_monitor()
        return ema
    
    def calc_wts_no_call(self, most_recent_sales):
        return self.current_ema

    def check_rate(self):
        return self.calc_wts_no_call(self.block_arr[len(self.block_arr) - 1].sales)/self.goal_sales_per_block

    def change_price(self):
        if (self.check_rate() > 1):
            self.price = self.price * \
                (1 + self.calc_wts_no_call(self.block_arr[len(self.block_arr) - 1].sales) / self.goal_sales_per_block)
        elif (self.check_rate() < 1):
            self.price = self.price * \
                (1 - self.calc_wts_no_call(self.block_arr[len(self.block_arr) - 1].sales) / self.goal_sales_per_block)
        else:
            pass

    def self_monitor(self):
        for i in range(len(self.block_arr)):
            if i % self.update_freq == 0:
                self.change_price()
            else:
                pass

    def reset(self):
        self.__init__


class block:
    def __init__(self, index, sales=0):
        self.sales = sales
        self.index = index

    def get_sales(self):
        return self.sales

    def set_sales(self, num):
        self.sales = num
    
    def to_dict(self):
        return {
            'sales': self.sales,
        }

