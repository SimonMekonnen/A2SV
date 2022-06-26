class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> fizz = new ArrayList<>();
        for (int k = 1; k <= n; k++) {
            String s = Integer.toString(k);
             if (k % 15 == 0) {
                s = "FizzBuzz";
            }
            else if (k % 3 == 0) {
                s = "Fizz";
            } else if (k % 5 == 0) {
                 s = "Buzz";
             }
            fizz.add(s);


        }
        return fizz;
    }
}