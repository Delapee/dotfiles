# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# User info
export USERNAME="Delape"
export NICKNAME="delape"

source ~/.shell/alias

. "$HOME/.cargo/env"

PS1='[\u@\h \W]\$ '

eval "$(starship init bash)"
