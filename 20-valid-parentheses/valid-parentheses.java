class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> chPairMap = new HashMap<>();
        chPairMap.put(')', '(');
         chPairMap.put('}', '{');
          chPairMap.put(']', '[');


        Stack<Character> stack = new Stack<>();

        for (char ch: s.toCharArray()) {
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            }
            else if (!stack.isEmpty() && stack.peek() == chPairMap.get(ch)) {
                stack.pop();
            }
            else {
                return false;
            }
        }

        return stack.isEmpty();

    }
}