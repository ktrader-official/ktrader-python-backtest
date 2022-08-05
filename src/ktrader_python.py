'''
KTrader Python 数据结构定义以及API
'''
from typing import List
from enum import Enum

class tick:
    '行情数据'
    instrument_id: str
    '合约ID'
    timestamp: int
    '时间戳(Unix纳秒)'
    last_price: float
    '最新价格'
    highest_price: float
    '最高价格'
    lowest_price: float
    '最低价格'
    volume_delta: int
    '新增成交'
    open_interest_delta: int
    '新增仓位'
    turnover_delta: int
    '新增成交量'
    bid_price: List[float]
    '买价'
    ask_price: List[float]
    '卖价'
    bid_volume: List[int]
    '买量'
    ask_volume: List[int]
    '卖量'

class product_class_enum(Enum):
    '产品类型'
    undefined = 'undefined', '未定义'
    futures = 'futures', '期货'
    options = 'options', '期货期权'
    combination = 'combination', '组合'
    spot = 'spot', '即期'
    EFP = 'EFP', '期转现'
    spot_option = 'spot_option', '现货期权'
    TAS = 'TAS', 'TAS合约'
    MI = 'MI', '金属指数'

class position_type_enum(Enum):
    '持仓类型'
    undefined = 'undefined', '未定义'
    net = 'net', '净持仓'
    gross = 'gross', '综合持仓'

class position_date_type_enum(Enum):
    '持仓日期类型'
    undefined = 'undefined', '未定义'
    use_history = 'use_history', '使用历史持仓'
    no_use_history = 'no_use_history', '不使用历史持仓'

class options_type_enum(Enum):
    '期权类型'
    undefined = 'undefined', '未定义'
    call = 'call', '看涨'
    put = 'put', '看跌'

class combination_type_enum(Enum):
    '组合类型'
    undefined = 'undefined', '未定义'
    future = 'future', '期货组合'
    BUL = 'BUL', '垂直价差BUL'
    BER = 'BER', '垂直价差BER'
    STD = 'STD', '跨式组合'
    STG = 'STG', '宽跨式组合'
    PRT = 'PRT', '备兑组合'
    CAS = 'CAS', '时间价差组合'
    OPL = 'OPL', '期权对锁组合'
    BFO = 'BFO', '买备兑组合'
    BLS = 'BLS', '买入期权垂直价差组合'
    BES = 'BES', '卖出期权垂直价差组合'

class margin_algo_enum(Enum):
    '保证金算法'
    undefined = 'undefined', '未定义'
    no_use_max_margin_side_algo = 'no_use_max_margin_side_algo', '不使用大额单边保证金算法'
    use_max_margin_side_algo = 'use_max_margin_side_algo', '使用大额单边保证金算法'

class direction_enum(Enum):
    '买卖方向'
    buy = 'buy', '买'
    sell = 'sell', '卖'
    undefined = 'undefined', '未定义'

class offset_flag_enum(Enum):
    '开平标志'
    undefined = 'undefined', '未定义'
    open = 'open', '开仓'
    close = 'close', '平仓'
    force_close = 'force_close', '强平'
    close_today = 'close_today', '平今'
    close_yesterday = 'close_yesterday', '平昨'
    force_off = 'force_off', '强减'
    local_force_close = 'local_force_close', '本地强平'

class time_condition_enum(Enum):
    '时间条件'
    undefined = 'undefined', '未定义'
    instant_or_cancel = 'instant_or_cancel', '立即完成或者撤销'
    good_for_session = 'good_for_session', '本节有效'
    good_for_day = 'good_for_day', '当日有效'
    good_till_date = 'good_till_date', '指定日期前有效'
    good_till_cancel = 'good_till_cancel', '撤销前有效'
    good_for_aggr = 'good_for_aggr', '集合竞价有效'

class volume_condition_enum(Enum):
    '成交条件'
    undefined = 'undefined', '未定义'
    any_volume = 'any_volume', '任何数量'
    minimum_volume = 'minimum_volume', '最小数量'
    all_volume = 'all_volume', '全部数量'

class order_status_enum(Enum):
    '报单状态'
    undefined = 'undefined', '未定义'
    all_traded = 'all_traded', '全部成交'
    partial_traded_queueing = 'partial_traded_queueing', '部分成交还在队列中'
    partial_traded_not_queueing = 'partial_traded_not_queueing', '部分成交不在队列中'
    no_trade_queueing = 'no_trade_queueing', '未成交还在队列中'
    no_trade_not_queueing = 'no_trade_not_queueing', '未成交不在队列中'
    canceled = 'canceled', '已撤单'
    unknown = 'unknown', '未知'
    not_touched = 'not_touched', '尚未触发'
    touched = 'touched', '已触发'

class order_submit_status_enum(Enum):
    '报单提交状态'
    undefined = 'undefined', '未定义'
    insert_submitted = 'insert_submitted', '已经提交'
    cancel_submitted = 'cancel_submitted', '撤单已经提交'
    modify_submitted = 'modify_submitted', '修改已经提交'
    accepted = 'accepted', '已经接受'
    insert_rejected = 'insert_rejected', '报单已经被拒绝'
    cancel_rejected = 'cancel_rejected', '撤单已经被拒绝'
    modify_rejected = 'modify_rejected', '改单已经被拒绝'

class position_direction_enum(Enum):
    '持仓多空方向'
    undefined = 'undefined', '未定义'
    pd_net = 'pd_net', '净'
    pd_long = 'pd_long', '多头'
    pd_short = 'pd_short', '空头'

class position_date_enum(Enum):
    '持仓日期'
    undefined = 'undefined', '未定义'
    today = 'today', '今日持仓'
    history = 'history', '历史持仓'


class trading_status_enum(Enum):
    '交易状态'
    undefined = 'undefined', '未定义'
    before_trading = 'before_trading', '开盘前'
    no_trading = 'no_trading', '非交易'
    continous = 'continous', '连续交易'
    auction_ordering = 'auction_ordering', '集合竞价报单'
    auction_balance = 'auction_balance', '集合竞价价格平衡'
    auction_match = 'auction_match', '集合竞价撮合'
    closed = 'closed', '收盘'

class exchange_trading_status:
    '交易所交易状态'
    exchange_id: str
    '交易所ID'
    status: trading_status_enum
    '交易状态'

class trade_info:
    '成交信息'
    timestamp: int
    '(Unix纳秒)'
    instrument_id: str
    '合约ID'
    broker_id: str
    '券商ID'
    investor_id: str
    '投资者ID'
    exchange_id: str
    '交易所ID'
    order_ref: int
    '报单号'
    trade_id: int
    '成交号'
    direction: direction_enum
    '成交方向'
    offset: offset_flag_enum
    '开平仓'
    price: float
    '成交价格'
    volume: int
    '成交量'

class instrument_order_info:
    '合约信息'
    id: str
    '合约ID'
    name: str
    '合约名称'
    product_id: str
    '品种ID'
    exchange_id: str
    '交易所ID'
    is_trading: bool
    '是否正在交易'
    price_tick: float
    '最小价格单位'
    volume_multiple: int
    '合约乘数'
    expire_date: int
    '合约到期日(如20220222)'
    default_last_price: float
    '默认最新价(启动时最新价)'
    last_settlement_price: float
    '昨结算价'
    upper_limit_price: float
    '涨停价'
    lower_limit_price: float
    '跌停价'
    min_market_volume: int
    '市价单最小报单量'
    max_market_volume: int
    '市价单最大报单量'
    min_limit_volume: int
    '限价单最小报单量'
    max_limit_volume: int
    '限价单最大报单量'
    long_margin_ratio_by_money: float
    '多头保证金率'
    long_margin_ratio_by_volume: float
    '多头每手保证金'
    short_margin_ratio_by_money: float
    '空头保证金率'
    short_margin_ratio_by_volume: float
    '空头每手保证金'
    open_commission_ratio_by_money: float
    '开仓手续费率'
    open_commission_ratio_by_volume: float
    '开仓每手手续费'
    close_commission_ratio_by_money: float
    '平仓手续费率'
    close_commission_ratio_by_volume: float
    '平仓每手手续费'
    close_today_commission_ratio_by_money: float
    '平今手续费率'
    close_today_commission_ratio_by_volume: float
    '平今每手手续费'
    order_commission_by_volume: float
    '报单手续费'
    order_action_commission_by_volume: float
    '撤单手续费'
    margin_algorithm: margin_algo_enum
    '保证金算法'
    position_type: position_type_enum
    '持仓类型'
    position_date_type: position_date_type_enum
    '持仓日期类型'
    product_class: product_class_enum
    '品种类型'
    option_type: options_type_enum
    '期权类型'
    combination_type: combination_type_enum
    '组合类型'
    strike_price: float
    '行权价格'

class order_status:
    '报单状态'
    instrument_id: str
    '合约ID'
    front_id: int
    '前置ID'
    session_id: int
    '会话ID'
    order_ref: int
    '报单号'
    order_sys_id: int
    '交易所报单号'
    exchange_id: str
    '交易所ID'
    status: order_status_enum
    '报单状态'
    submit_status: order_submit_status_enum
    '报单提交状态'
    direction: direction_enum
    '报单方向'
    offset: offset_flag_enum
    '开平仓'
    time_condition: time_condition_enum
    '时间条件'
    volume_condition: volume_condition_enum
    '成交条件'
    limit_price: float
    '限定价格'
    volume_pending: int
    '未成交量'
    volume_traded: int
    '已成交量'
    frozen_margin: float
    '冻结保证金'
    frozen_commission: float
    '冻结手续费'
    order_commission: float
    '订单手续费'
    cancel_requested: bool
    '是否已请求撤单'
    error_code: int
    '错误码'
    error_msg: str
    '错误信息'

class instrument_trading_risk:
    '风险信息'
    instrument_id: str
    '合约ID'
    self_trade_count: int
    '自成交次数'
    cancel_count: int
    '撤单数'

class bar:
    'K线数据'
    instrument_id: str
    '合约ID'
    start: int
    '开始时间(Unix Nano)'
    end: int
    '结束时间(Unix Nano)'
    open: float
    '开盘价'
    high: float
    '最高价'
    low: float
    '最低价'
    close: float
    '收盘价'
    turnover: float
    '成交额'
    volume: int
    '成交量'
    oi: int
    '开仓量'

class trade_key:
    '成交主键, 用来唯一标志一笔成交'
    instrument_id: str
    '合约ID'
    trade_id: int
    '成交号'
    direction: direction_enum
    '方向'

class order_update:
    '订单更新信息'
    order: order_status
    '订单信息'
    has_trade: bool
    '是否包含成交'
    trade: trade_info
    '成交信息'

class target_position_algorithm(Enum):
    '调仓算法'
    undefined = 'undefined', '未定义'
    basic = 'basic', '基本'
    market_on_open = 'market_on_open', '开盘抢单'
    manual = 'manual', '手动'
    force_manual = 'force_manual', '强制手动'
    time_weighted = 'time_weighted', '时间加权'
    volume_weighted = 'volume_weighted', '成交量加权'

class position_target:
    '目标仓位'
    instrument_id: str
    '合约ID'
    algorithm: target_position_algorithm
    '调仓算法'
    target_pos: int
    '目标仓位'
    desired_price: float
    '目标价格'

class direction_entry:
    '持仓数据'
    direction: direction_enum
    '持仓方向'
    total: int
    '总持仓'
    today: int
    '今日持仓'
    history: int
    '历史持仓'
    total_cost: float
    '逐日总成本'
    total_margin: float
    '总保证金'
    frozen_open: int
    '冻结开仓手数'
    frozen_close_today: int
    '冻结平今手数'
    frozen_close_history: int
    '冻结平昨手数'
    frozen_margin: float
    '冻结保证金'

class instrument_summary:
    '合约持仓总结'
    instrument_id: str
    '合约ID'
    exchange_id: str
    '交易所ID'
    position_profit: float
    '逐日持仓利润'
    long_position: direction_entry
    '多仓数据'
    short_position: direction_entry
    '空仓数据'
    close_profit: float
    '逐日平仓利润'
    total_margin: float
    '总保证金'
    total_commission: float
    '总手续费'
    total_order_commission: float
    '总报单手续费'
    frozen_margin: float
    '冻结保证金'
    frozen_commission: float
    '冻结手续费'
    frozen_order_commission: float
    '冻结报单手续费'
    net_pnl: float
    '净利润'
    net_pos: int
    '净持仓'

class position_entry(trade_info):
    '逐笔持仓信息'
    position_date: position_date_enum
    '持仓日期'
    position_cost: float
    '仓位成本'
    use_margin: float
    '占用保证金'

class instrument_position(instrument_summary):
    '合约持仓详细'
    long_position_detail: List[position_entry]
    '逐笔多仓详情'
    short_position_detail: List[position_entry]
    '逐笔空仓详情'

class position_summary:
    '总持仓总结'
    position_profit: float
    '逐日持仓利润'
    close_profit: float
    '逐日平仓利润'
    total_margin: float
    '总保证金'
    total_commission: float
    '总手续费'
    total_order_commission: float
    '总报单手续费'
    frozen_margin: float
    '冻结保证金'
    frozen_commission: float
    '冻结手续费'
    frozen_order_commission: float
    '冻结报单手续费'
    net_pnl: float
    '净利润'
    num_trades: int
    '成交手数'
    num_win_trades: int
    '盈利成交手数'
    num_loss_trades: int
    '亏损成交手数'
    gain_per_trade: float
    '平均每手盈利(逐笔)'
    loss_per_trade: float
    '平均每手亏损(逐笔)'
    gain_loss_ratio: float
    '盈亏比例'
    win_ratio: float
    '盈利比例'
    gross_profit_per_trade: float
    '平均每手毛利润(逐笔)'
    net_profit_per_trade: float
    '平均每手净利润(逐笔)'
    fees_per_trade: float
    '平均每手费用'

class account_summary:
    '账户总结'
    broker_id: str
    '券商ID'
    investor_id: str
    '用户ID'
    pre_balance: float
    '账户昨日权益'
    balance: float
    '账户当前权益'
    close_profit: float
    '逐日平仓利润'
    position_profit: float
    '逐日持仓利润'
    margin_used: float
    '总保证金'
    total_commission: float
    '总手续费'
    net_pnl: float
    '净盈亏'
    net_pnl_high: float
    '最高净盈亏(当前交易日)'
    net_pnl_low: float
    '最低净盈亏(当前交易日)'
    frozen_cash: float
    '冻结现金'
    frozen_margin: float
    '冻结保证金'
    frozen_commission: float
    '冻结手续费'
    available_cash: float
    '可用现金'
    risk_level: float
    '风险度 (权益-可用现金)/权益'

class trigger_decision:
    '触发器决策'
    should_close: bool
    '是否平仓'
    opt_price: float
    '可选平仓价格, 若为零则采用对价'

class position_trigger:
    def update_tick(self, t: tick) -> trigger_decision:
        '''更新行情

        Parameters
        ----------
        t : tick
            最新行情

        Returns
        -------
        trigger_decision
            平仓与否及可选平仓价格
        '''
        return trigger_decision()

class ktrader_api:
    'KTrader API定义'
    def identifier(self) -> int:
        '''获得策略的编号

        Returns
        -------
        int
            该策略对应的编号
        '''
        return 0

    def create_order(self,
                     instrument_id: str,
                     direction: direction_enum,
                     offset: offset_flag_enum,
                     time_condition: time_condition_enum,
                     volume_condition: volume_condition_enum,
                     limit_price: float,
                     volume: int,
                     retriable: bool) -> order_status:
        '''下单功能, 用户可通过该方法指定KTrader API下任意订单

        Parameters
        ----------
        instrument_id : str
           合约ID
        direction : direction_enum
            订单方向
        offset : offset_flag_enum
           开平仓
        time_condition : time_condition_enum
           时间条件
        volume_condition : volume_condition_enum
           成交量条件
        limit_price : float
           限定价格
        volume : int
           成交量

        Returns
        -------
        order_status
            订单状态, 用户需检查error_code是否为0')
        '''
        return order_status(self)

    def cancel_order(order: order_status) -> str:
        ''' 撤单功能, 撤销一未成交订单

        Parameters
        ----------
        order : order_status
            订单状态, 需要合法, 如下单函数返回的状态

        Returns
        -------
        str
            撤单错误, 如非空则代表撤单失败返回的错误信息)
        '''
        return ''

    def close_position(self, key: trade_key, price: float) -> order_status:
        '''平掉一指定仓位

        Parameters
        ----------
        key : trade_key
            仓位对应成交主键, 可用key_of得到
        price : float
            平仓价格

        Returns
        -------
        order_status
            订单状态, 用户需检查error_code是否为0)
        '''
        return order_status()

    def set_target_position(self, target: position_target, force_override: bool = False) -> str:
        '''获取目标仓位

        Parameters
        ----------
        target : position_target
            仓位目标
        force_override : bool
            用户只能使用默认值False

        Returns
        -------
        str
            如仓位目标无效则返回错误信息)
        '''
        return ''

    def get_target_position(self, instrument_id: str) -> position_target:
        '''获取目标仓位

        Parameters
        ----------
        instrument_id : str
            合约ID

        Returns
        -------
        position_target
            合约当前仓位目标, 如未设置则调仓算法为manual
        '''
        return position_target()

    def target_position_reached(self, instrument_id: str) -> bool:
        '''询问是否已达到目标仓位

        Note
        ----
        对于basic调仓算法, 净持仓达到目标仓位且无未成交订单则认为达到目标仓位,
        对于manual调仓算法, 始终认为达到目标仓位,
        对于market_on_open调仓算法, 收到开盘成交回报则认为达到目标仓位

        Parameters
        ----------
        instrument_id : str
            合约ID

        Returns
        -------
        bool
            该合约是否已达到目标
        '''
        return False

    def register_trigger(self, pos: position_entry, trigger: position_trigger) -> bool:
        '''注册平仓条件触发器

        Parameters
        ----------
        pos : position_entry
            要平仓的仓位
        trigger : position_trigger
            触发器

        Returns
        -------
        bool
            是否成功注册触发器, 如参数中仓位不存在或该合约采用主动调仓算法则无法注册触发器
        '''
        return False

    def cancel_triggers(self, pos: position_entry):
        '''取消条件触发器

        Parameters
        ----------
        pos : position_entry
            要平仓的仓位
        '''
        pass

    def cancel_all_triggers(self, instrument_id: str):
        '''取消指定合约所有仓位已注册的全部触发器

        Parameters
        ----------
        instrument_id : str
            合约ID
        '''
        pass

    def get_last_tick(self, instrument_id: str) -> tick:
        '''获取最新行情tick

        Parameters
        ----------
        instrument_id : str
            合约ID

        Returns
        -------
        tick
            该合约最新行情信息
        '''
        return tick()

    def get_last_k_ticks(self, instrument_id: str, num_tick: int) -> List[tick]:
        '''获取最新k个tick

        Parameters
        ----------
        instrument_id : str
            合约ID
        num_tick : int
            最多获得的tick数量

        Returns
        -------
        List[tick]
            该合约最新至多num_tick个tick信息
        '''
        return []

    def subscribe_instrument(self, instrument_id: str):
        '''调用该函数可订阅合约行情

        Parameters
        ----------
        instrument_id : str
            合约ID
        '''
        pass

    def get_instrument_position_detail(self, instrument_id: str) -> instrument_position:
        '''获得指定合约逐笔持仓信息, 调用该函数将订阅合约行情

        Parameters
        ----------
        instrument_id : str
            合约ID

        Returns
        -------
        instrument_position
            该合约对应详细持仓信息
        '''
        return instrument_position()

    def get_instrument_summary(self, instrument_id: str) -> instrument_summary:
        '''获得指定合约持仓总结, 调用该函数将订阅合约行情

        Parameters
        ----------
        instrument_id : str
            合约ID

        Returns
        -------
        instrument_summary
            该合约对应持仓总结
        '''
        return instrument_summary()

    def get_position_summary(self) -> position_summary:
        '''获取本策略全部仓位总结

        Parameters
        ----------
        instrument_id : str
            合约ID

        Returns
        -------
        position_summary
            本策略持仓总结
        '''
        return position_summary()

    def get_position_entry(self, key: trade_key) -> position_entry:
        '''获取一笔具体持仓

        Parameters
        ----------
        key : trade_key
            成交主键

        Returns
        -------
        position_entry
            具体逐笔持仓信息
        '''
        return position_entry()

    def get_all_position_summary(self) -> List[instrument_summary]:
        '''获取全部合约持仓总结

        Returns
        -------
        List[instrument_summary]
            全部已订阅订单的持仓总结
        '''
        return []

    def get_all_position_detail(self) -> List[instrument_position]:
        '''获取全部合约持仓详情

        Returns
        -------
        List[instrument_position]
            全部已订阅合约的持仓详细信息
        '''
        return []

    def get_inflight_orders(self) -> List[order_status]:
        '''获取全部未完成订单

        Returns
        -------
        List[order_status]
            全部未完成订单的订单状态
        '''
        return []

    def get_account_summary(self) -> account_summary:
        '''获取账户信息

        Returns
        -------
        account_summary
            本账户资金信息
        '''
        return account_summary(self)

    def subscribe_bars(self, instrument_id: str, freq: int = 1):
        '''订阅指定合约K线, 新K线闭合时会调用策略的on_bar回调

        Parameters
        ----------
        instrument_id : str
            合约ID
        freq : int
            指定分钟线频率(freq=1, 1分钟K线; freq=5, 5分钟K线)
        '''
        pass

    def get_last_k_bars(self, instrument_id: str, window_size: int, freq: int = 1) -> List[bar]:
        '''获取指定合约K线

        Parameters
        ----------
        instrument_id : str
            合约ID
        window_size : int
            获取K线数据窗口大小(window_size = 10, freq=5, 表示每次拿到10个5分钟K线)
        freq : int
            指定分钟线频率(freq=1, 1分钟K线; freq=5, 5分钟K线)

        Returns
        -------
        List[bar]
            该合约至多window_size个K线数据
        '''
        return []

    def get_instrument_info(self, instrument_id: str) -> instrument_order_info:
        '''获取合约交易信息

        Parameters
        ----------
        instrument_id : str
            合约ID

        Returns
        -------
        instrument_order_info
            该合约交易参数
        '''
        return instrument_order_info()

    def get_instrument_trading_risk(self, instrument_id: str) -> instrument_trading_risk:
        '''获取合约风险信息

        Parameters
        ----------
        instrument_id : str
            合约ID

        Returns
        -------
        instrument_trading_risk
            该合约风险信息
        '''
        return instrument_trading_risk()

class python_strategy:
    '''策略核心

    KTrader策略核心接口定义, 用户的量化策略需实现该接口
    '''
    def __init__(self):
        self.api = ktrader_api()
        '当init被调用时, 系统会配置好api'

    def update_config(self, config: str) -> str:
        '''更新策略配置

        strategy_config/global_config.json中配置的'config'项目将会成为
        策略初始化时的参数

        Parameters
        ----------
        config: str
            config 策略配置参数, 例如配置文件名

        Returns
        -------
        str
            如配置参数无效则返回错误信息
        '''
        return ''

    def on_tick(self, t: tick):
        '''行情回调

        用户需调用KTrader API的get_instrument_summary方法订阅合约行情,
        当KTrader收到订阅的合约行情更新时, 会调用该方法

        Parameters
        ----------
        t: tick
            最新行情更新
        '''
        pass

    def on_bar(self, b: bar):
        '''K线回调

        用户需调用KTrader API的subscribe_bars方法订阅合约K线行情,
        当KTrader产生新的K线行情更新时, 会调用该方法

        Parameters
        ----------
        b: bar
            最新K线更新
        '''
        pass

    def on_order_update(self, update: order_update):
        '''订单更新回调

        当该策略所下订单有新成交或被撤单时会调用该方法

        Parameters
        ----------
        update : order_update
            订单更新
        '''
        pass

    def init(self):
        '''初始化

        策略初始化时KTrader API可用且update_config已被调用
        '''
        pass

    def shutdown(self):
        '''系统结束

        KTrader系统结束前会调用该方法, 用户可以进行资源释放等操作
        '''
        pass

    api: ktrader_api
    '当init被调用时, 系统会配置好api'

def serialize(param) -> str:
    '''序列化
    Parameters
    ----------
    param
        KTrader数据类型

    Returns
    -------
    str
        序列化字符串
    '''
    return ''

def key_of(param: trade_info) -> trade_key:
    '''获得成交主键

    Parameters
    ----------
    param : trade_info
        成交信息

    Returns
    -------
    trade_key
        对应成交主键
    '''
    return trade_key()

def get_time_now() -> int:
    '''获取当前时间, Unix纳秒

    Returns
    -------
    int
        当前时间戳
    '''
    return 0

def get_trading_day() -> int:
    '''获取当前交易日

    Returns
    -------
    int
        当前交易日, 如20220222
    '''
    return 0

def next_trading_day(cur: int) -> int:
    '''计算下一交易日

    Parameters
    ----------
    cur : int
        当前交易日

    Returns
    -------
    int
        下一交易日
    '''
    return 0

def next_k_trading_day(cur: int, k: int) -> int:
    '''计算之后第k个交易日

    Parameters
    ----------
    cur : int
        当前交易日
    k : int
        计算的天数

    Returns
    -------
    int
        之后第k个交易日
    '''
    return 0

def next_day(cur: int) -> int:
    '''计算下一日期

    Parameters
    ----------
    cur : int
        当前日期

    Returns
    -------
    int
        下一日期
    '''
    return 0

def prev_trading_day(cur: int) -> int:
    '''计算上一交易日

    Parameters
    ----------
    cur : int
        当前交易日

    Returns
    -------
    int
        上一交易日
    '''
    return 0

def prev_k_trading_day(cur: int, k: int) -> int:
    '''计算之前第k个交易日

    Parameters
    ----------
    cur : int
        当前交易日
    k : int
        计算的天数

    Returns
    -------
    int
        之前第k个交易日
    '''
    return 0

def prev_day(cur: int) -> int:
    '''计算上一日期

    Parameters
    ----------
    cur : int
        当前日期

    Returns
    -------
    int
        上一日期
    '''
    return 0

def parse_time(date: int, t: str) -> int:
    '''解析时间，转为Unix纳秒

    Parameters
    ----------
    date : int
        日期
    t : str
        时间(如12:34:56)

    Returns
    -------
    int
        解析后时间(Unix纳秒)
    '''
    return 0

def parse_time_format(fmt: str, t: str) -> int:
    '''解析时间，转为Unix纳秒

    Parameters
    ----------
    fmt : str
        strftime格式(https://zh.cppreference.com/w/c/chrono/strftime)
    t : str
        要解析的时间字符串

    Returns
    -------
    int
        解析后时间(Unix纳秒)
    '''
    return 0

def format_time(timestamp_nano: int, fmt: str = '') -> str:
    '''格式化时间

    Parameters
    ----------
    timestamp_nano : int
        时间(Unix纳秒)
    fmt : str
        strftime格式(https://zh.cppreference.com/w/c/chrono/strftime), 空字符串则为默认格式(如20210625-09:30:00.535)

    Returns
    -------
    str
        时间字符串
    '''
    return ''

def date_from_timestamp(t: int) -> int:
    '''获取时间戳对应日期

    Parameters
    ----------
    timestamp_nano : int
        时间(Unix纳秒)

    Returns
    -------
    int
        时间戳对应8位数字日期(如20220202)
    '''
    return 0

def kt_info(log: str):
    '''打印info日志

    Note
    ----
    日志出现在KTrader系统日志中

    Parameters
    ----------
    log : str
        log内容
    '''
    pass

def kt_error(log: str):
    '''打印error日志

    Note
    ----
    日志出现在KTrader系统日志中

    Parameters
    ----------
    log : str
        log内容
    '''
    pass

def kt_critical(log: str):
    '''打印critical日志

    Note
    ----
    日志出现在KTrader系统日志中

    Parameters
    ----------
    log : str
        log内容
    '''
    pass
