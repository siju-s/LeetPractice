class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> result = new ArrayList<>();
        
        for (int i = 1; i <= n; i++) {
             int num = i;
             if (num % 3 == 0 && num % 5 == 0) {
                result.add("FizzBuzz");
             }
             else if (num % 3 == 0) {
                result.add("Fizz");
             }
             else if (num % 5 == 0) {
                result.add("Buzz");
             }
             else {
                result.add(String.valueOf(num));
             }
        }

        return result;
    }
}