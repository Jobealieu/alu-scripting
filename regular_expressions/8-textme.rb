#!/usr/bin/env ruby
# 8-textme.rb
# Usage: ./8-textme.rb 'log line'
# Output: sender,receiver,flags

input = ARGV[0] || ''

# We look for patterns like: [from:...], [to:...], [flags:...]
# Regex explanation (Oniguruma-compatible):
# \[from:([^\]]+)\]    captures sender (anything except closing bracket)
# \s+\[to:([^\]]+)\]   captures receiver
# \s+\[flags:([^\]]+)\] captures flags
if input =~ /\[from:([^\]]+)\]\s+\[to:([^\]]+)\]\s+\[flags:([^\]]+)\]/
  sender  = $1
  receiver = $2
  flags   = $3
  puts "#{sender},#{receiver},#{flags}"
end
