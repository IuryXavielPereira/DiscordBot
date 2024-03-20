if screen -ls | grep -q '\.bot\s'; then
    echo "A sessão screen 'bot' já estava ativa, desativando"
    screen -XS bot quit
else
    echo "A sessão 'bot' não existe"
fi