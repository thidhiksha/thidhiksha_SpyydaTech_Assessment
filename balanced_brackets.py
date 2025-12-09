#balanced brackets
def check_brackets(s):
  stack = []
  for ch in s:
    if ch in ['(','{','[']:
      stack.append(ch)
    elif ch in [')','}',']']:
        if not stack:
          return False
        
        last = stack.pop()
        if ch==')'and last !='(':
            return False
        if ch=='}'and last !='{':
            return False
        if ch==']'and last!='[':
            return False
  #after checking,empty the stack
  return len(stack)==0
if __name__=="__main__":
    print(check_brackets("{[()]}"))
    print(check_brackets("([)]"))
