ON *:TEXT:!read *:#: {
  if ($readini(memo.ini, $nick, $2) == $null) {
    msg $chan Memo not found.
  }
  else {
    msg $chan $readini(memo.ini, $nick, $2)
  }
}
ON *:TEXT:!write *:#: {
  if ($2 == $null) || ($3 == $null) {
    msg $chan Use !write <nick> <text>
  }
  else {
    if ($ini(memo.ini, $2, 0) == $null) {
      writeini -n memo.ini $2 1 $3-
      msg $chan Memo stored as memo nr. 1
    }
    else {
      var %last = $calc($ini(memo.ini, $2, 0) +1) 
      writeini -n memo.ini $2 %last $3-
      msg $chan Memo stored as memo nr. %last 
    }
  }
}
ON *:TEXT:!read:#: {
  msg $chan Use !read <nr>
}
ON *:TEXT:!write:#: {
  msg $chan Use !write <nick> <text>
}
