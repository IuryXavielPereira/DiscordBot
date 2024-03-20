if screen -ls | grep -q '\.bot\s'; then
    echo "A seção screen 'bot' já está ativa"
else
    screen -d -S bot -m python3 bot.py
    echo "Nova seção screen 'bot' criada."
fi