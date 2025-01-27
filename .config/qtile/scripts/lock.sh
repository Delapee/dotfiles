fg="#D9E0EE"
unlocker="#000000"
ring="#CC00CC"
wrong="#FF0000"
highlight="#B5E8E0"
date="#FFFFFF"
verify="#DDB6F2"
ring_out="#0000FF"

i3lock \
    -n \
    --force-clock \
    -i ~/.config/qtile/wallpapers/cosmere-logo.jpeg \
    -e \
    --indicator \
    --radius=40 \
    --ring-width=8 \
    --inside-color=$unlocker \
    --ring-color=$fg \
    --insidever-color=$verify \
    --ringver-color=$verify \
    --insidewrong-color=$wrong \
    --ringwrong-color=$wrong \
    --line-uses-inside \
    --keyhl-color=$ring \
    --separator-color=$verify \
    --bshl-color=$ring \
    --time-str="%H:%M" \
    --time-size=120 \
    --date-str="%a, %d %b" \
    --date-size=42 \
    --verif-text="Verifying Password..." \
    --wrong-text="Wrong Password!" \
    --noinput-text="" \
    --greeter-text="Type the password to unlock" \
    --time-font="JetBrainsMono Nerd Font" \
    --date-font="JetBrainsMono Nerd Font" \
    --verif-font="JetBrainsMono Nerd Font" \
    --greeter-font="JetBrainsMono Nerd Font" \
    --wrong-font="JetBrainsMono Nerd Font" \
    --verif-size=23 \
    --greeter-size=23 \
    --wrong-size=23 \
    --time-pos="200:560" \
    --date-pos="205:630" \
    --ind-pos="1700:520" \
    --greeter-pos="1700:630" \
    --wrong-pos="1700:670" \
    --verif-pos="1700:670" \
    --date-color=$date \
    --time-color=$date \
    --greeter-color=$fg \
    --wrong-color=$wrong \
    --verif-color=$verify \
    --pointer=default \
    --refresh-rate=0 \
    --pass-media-keys \
    --pass-volume-keys