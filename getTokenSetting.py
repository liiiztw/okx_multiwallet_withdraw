# 載入設定
import json
config_filepath = 'config.json'
address_filepath = 'wallets.txt'
with open(config_filepath) as f:
    config_dict = json.load(f)

with open(address_filepath) as f:
    address_list = f.read().split()    

try:
    import pandas as pd
    import okex.Funding_api as Funding
    fundingAPI = Funding.FundingAPI(config_dict['key'], config_dict['secret'], config_dict['passphrase'],False,flag='0')

    # 檢查餘額
    df_bal = pd.DataFrame(fundingAPI.get_balances()['data'])
    df_bal['availBal'] = df_bal['availBal'].astype(float)
    bal = float(df_bal.loc[df_bal['ccy']==config_dict['token'],'availBal'])
    print(f"餘額: {bal}")

    import pandas as pd
    df_coin = pd.DataFrame(fundingAPI.get_currency()['data'])
    df_coin = df_coin.loc[df_coin['ccy']==config_dict['token'],['ccy','chain','minWd','minFee']].rename(columns={
        "ccy":"token",
        "chain":"network",
        "minWd":"minAmount",
        "minFee":"minFee"
    })
    print(df_coin)
except Exception as msg:
    print(msg)
    pass
    
input('\npress "ENTER" to close')