class AlgoClass:
    """
    Initializes the Algorithm with given values. goal_sales_per_block represents our target for sales/block.
    initial_price is the initial minting price of the NFT. update_freq is how often the Algorithm updates itself. A value of 1
    means it updates during every new block.
    """
    def __init__(self, goal_sales_per_block, initial_price, update_freq):
        self.goal_sales_per_block = goal_sales_per_block
        self.price = initial_price
        self.block_arr = []
        self.profit = 0
        self.update_freq = update_freq
        self.initial_price = initial_price
        self.current_ema = 0
        self.ema_array = []
        self.current_wts = 0
    
    """
    Getter function for the price. I don't think this is necessary but my Java background is coming through.
    """
    def get_price(self):
        return self.price


    """
    Calculates our Weighted Total Sales. This algorithm is loosely based off of the exponential moving average algorithm. However,
    it also takes the additional step of taking the EMA of the EMA, thus giving us a far more responsive and accurate rate.
    """
    def calc_wts(self, most_recent_sales):
        if (len(self.block_arr) <= self.update_freq):
            ema = 0
            wts = 0
        else:
            ema = 0.2 * most_recent_sales + self.current_ema * (1 - 0.2)
            wts = 2 * ema - (0.2 * self.ema_array[-1] + self.current_wts * (1 - 0.2))
        self.current_ema = ema
        self.current_wts = wts
        self.ema_array.append(ema)
        self.profit += self.price * most_recent_sales
        self.self_monitor()
        return wts
    
    def calc_wts_no_call(self):
        return self.current_ema

    """
    Compares current Weighted Total Sales to our target sale rate.
    """
    def check_rate(self):
        ratio = self.calc_wts_no_call()/self.goal_sales_per_block
        return ratio

    """
    If below target sale rate, decreases price by 5% every update period. If above target sale rate, increases price
    by a factor relative to the difference in rates.
    """
    def change_price(self):
        ratio = self.check_rate()
        if (ratio > 1):
            self.price = self.price * \
                (self.calc_wts_no_call() / self.goal_sales_per_block)
        elif (ratio < 1):
            self.price = self.price * 0.95
        else:
            pass
    
    """
    Function that checks to see if the current block index is one we should update on given our block frequency.
    """
    def self_monitor(self):
        if (len(self.block_arr) % self.update_freq == 0):
            self.change_price()
        else:
            pass
    
    def get_profit(self):
        return self.profit

    def reset(self):
        self.__init__

"""
block class, represents our blocks. Backbone of our simulations.
"""
class block:
    def __init__(self, index, sales=0):
        self.sales = sales
        self.index = index

    """
    Getter function for sales.
    """
    def get_sales(self):
        return self.sales
    """
    Increments sales.
    """
    def add_sales(self):
        self.sales += 1
