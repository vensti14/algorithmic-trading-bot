def risk_management(capital, position_size, max_drawdown=0.1):
    if position_size > capital * max_drawdown:
        position_size = capital * max_drawdown
    return position_size
