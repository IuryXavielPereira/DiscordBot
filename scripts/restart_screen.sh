if screen -ls | grep -q '\.bot\s'; then
    echo "A seção screen 'bot' já estava ativa ativa, desativando"
    screen -XS bot quit
    screen -d -S bot -m python3 bot.py
    echo "Nova seção screen 'bot' criada."
else
    screen -d -S bot -m python3 bot.py
    echo "Nova seção screen 'bot' criada."
fi