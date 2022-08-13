
![logo](assets/mihate-logo.png)
# mihate

> A multifunction discord bot written in python.

## Requirements
1. Discord Bot Token
2. AbuseIPDB API Key
3. TheCatAPI API Key

## 🚀 Getting Started
🐋 Docker
```sh
docker volume create mihatedb
docker run -v mihatedb:/home/mihate/db -e "TOKEN=<DISCORD_BOT_TOKEN>" -e "ABUSEIPDB_KEY=<ABUSEIPDB_APIKEY>" -e "CATAPI_KEY=<THECATAPI_APIKEY>" -e "PREFIX=<BOT_PREFIX>" ghcr.io/rinlabs/mihate:latest
```

## 🪄 Features & Commands
> Note: Using % as example prefix
 - 🔎 Link & IP scanning
   1. AbuseIPDB
   2. URLHaus
   3. Hyperphish
 - ℹ️ Custom help command
 `%help`
 - 😀 Greets user
 `%greet`
 - 🎲 Hiura Picture Gacha Minigame
 `%hiuraroll`
 - ✨ Sends random one-line ASCII art
 `%lineart`
 - 🪙 Coinflip
 `%coinflip`
 - 😺 Random Cat Image
 `%neko`
 
