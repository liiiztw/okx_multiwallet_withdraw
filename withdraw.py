# 載入設定
import json
config_filepath = 'config.json'
address_filepath = 'wallets.txt'
with open(config_filepath) as f:
    config_dict = json.load(f)

with open(address_filepath) as f:
    address_list = f.read().split()
    
if config_dict['random_amount']:
    max_amount_range = 5
else:
    max_amount_range = 0

try:
    import pandas as pd
    
    import okex.Funding_api as Funding
    fundingAPI = Funding.FundingAPI(config_dict['key'], config_dict['secret'], config_dict['passphrase'],False,flag='0')
    
    # 檢查餘額
    df_bal = pd.DataFrame(fundingAPI.get_balances()['data'])
    df_bal['availBal'] = df_bal['availBal'].astype(float)
    bal = float(df_bal.loc[df_bal['ccy']==config_dict['token'],'availBal'])
    print(f"初始餘額: {bal}")
    
    # 提幣訊息
    df_coin = pd.DataFrame(fundingAPI.get_currency()['data'])
    minfee = float(df_coin.loc[(df_coin['ccy']==config_dict['token'])&(df_coin['chain']==config_dict['network']),'minFee'])
    print(f"手續費: {minfee}\n")

    import time
    import random
    if bal>=(len(address_list)*(config_dict['amount']*(1+max_amount_range/1000)+minfee)):
        for address in address_list:
        
            ratio = (1+random.randint(0,max_amount_range)/1000)
            res = fundingAPI.coin_withdraw(ccy=config_dict['token'],chain=config_dict['network'] , amt=config_dict['amount']*ratio, dest="4", toAddr=address, pwd="pwd", fee=minfee)
            
            if res['msg']:
                print(f"!!{res['msg']}!!")
            else:
                try:
                    pd.read_csv('log.csv')
                except:
                    with open('log.csv', 'w') as f: f.write("time,targetAddress,network,amount,token,fee\n")
                    pass
                with open('log.csv', 'a') as f: f.write(f"{pd.Timestamp('now').ceil(freq='s')},{address},{config_dict['network']},{config_dict['amount']},{config_dict['token']},{minfee}\n")
                print(f"[{pd.Timestamp('now').ceil(freq='s')}] {address} {config_dict['network']}:{config_dict['amount']}{config_dict['token']} fee:{minfee}")
                
                delay = random.randint(config_dict['delay']['min'],config_dict['delay']['max'])
                for t in range(delay):
                    print(f'waiting - {delay-t}s', end="\r")
                    time.sleep(1)
                
        # 檢查餘額
        df_bal = pd.DataFrame(fundingAPI.get_balances()['data'])
        df_bal['availBal'] = df_bal['availBal'].astype(float)
        bal = float(df_bal.loc[df_bal['ccy']==config_dict['token'],'availBal'])
        print(f"\n現在餘額: {bal}")

    else:
        print(f"\n餘額不足: {bal-(len(address_list)*(config_dict['amount']+minfee))}")

except Exception as msg:
    print(msg)
    pass
    
input('\npress "ENTER" to close.')