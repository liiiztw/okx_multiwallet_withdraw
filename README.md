# Okx multi-wallet withdraw
Just for 阿彬168

## Give me a coffe 

metamask wallet
```
0x9FedBBC14302838837284595504Ff15487A5ac85
```

## Description

Okx 多地址提幣功能

## Getting Started
Go to okx.com and get the api key, set multi-wallet addresses to whitelist.

### config.json
```
{
    "token": "USDC",
    "network": "USDC-Optimism",
    "amount": 1,
    "random_amount":true,
    "delay": { "min": 3, "max": 5 },
    "key":"",
    "secret":"",
    "passphrase":"$RFV"
}
```
1. edit token which you wana withdraw
2. run getTokenSetting.exe to check "network" and "minAmount"
3. edit "network" and "amount"(minAmount)
4. random_amount true or false

### wallets.txt
```
0x9FedBBC14302838837284595504Ff15487A5ac85
0x3728814d34c3C271B276F7528A3370b2015C6C9E
```

## run withdraw.exe

## contact info

[tlelgram](https://t.me/liiiztw)
[twitter](https://twitter.com/game_liiiz)

## Version History

* 1.0
    * Initial Release

## License

GPL ( GNU General Public License )

## Acknowledgments

* [okex-api-v5 - marzwu ](https://github.com/coinrising/okex-api-v5)
