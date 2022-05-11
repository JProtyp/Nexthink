# Q1.a: A program to find users that match a provided filter received in the [1] argument
  w= `who | grep $1`
  if [ -z "$w" ]; then
    echo "$1 is not find in user list";
# Q1.b ------------
  else
    echo "$1 is found in user list: $w";
# ------------------
  fi