#导入函数库
import jqdata

#初始化函数 设定基准等等
def initialize(context):
    #g.security ='601318.XSHG'
    g.security = get_index_stocks('000300.XSHG')
    print(g.security)
    #模拟盘使用真实价格成交
    set_option('use_real_price', True)
    #设置佣金/印花税
    set_order_cost(OrderCost(close_tax=0.001, open_commission=0.0003, close_commission=0.0003,
                            min_commission=5), type='stock')
                            
def handle_data(context,data):
    #print(get_current_data()['601318.XSHG'].day_open)
    #print(attribute_history('601318.XSHG',5))
    #order('601318.XSHG',100)#一天买了100股
    #order_value('601318.XSHG',10000)
    for stock in g.security:
        p = get_current_data()[stock].day_open
        amount = context.portfolio.positions[stock].total_amount
        
        
        #一般情况下先卖后买
        
        
       
        #买
        tobuy = []
        for stock in g.security:
            p = get_current_data()[stock].day_open
            amount = context.portfolio.positions[stock].total_amount
            cost = context.portfolio.positions[stock].avg_cost
            if amount>0 and p >= cost*1.25:
                order_target(stock,0) #止盈
            if amount>0 and p<= cost*0.9:
                order_target(stock,0) #止损
                
        
        if p <= 10.0 and amount == 0:
            tobuy.append(stock)
        cash_per_stock = context.portfolio.available_cash/len(tobuy)
        for stock in tobuy:
            order_value(stock,cash_per_stock)
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    