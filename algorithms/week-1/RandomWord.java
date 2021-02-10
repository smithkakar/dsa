/* Written by Smith Kakar */
/* Write a program RandomWord.java that reads a sequence of words from
standard input and prints one of those words uniformly at random.
Do not store the words in an array or list. Instead, use Knuth’s method:
when reading the ith word, select it with probability 1/i to be the champion,
replacing the previous champion. After reading all of the words,
print the final champion. */
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
    public static void main(String[] args) {
        int i = 1;
        String randomString = "";
        while (!StdIn.isEmpty()) {
            String item = StdIn.readString();
            boolean bool = StdRandom.bernoulli((double) 1 / i);
            if (bool) {
                randomString = item;
            }
            i++;
        }
        StdOut.println(randomString);
    }
}
