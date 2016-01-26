// solution to Exercise 1.2.3 problem #4 from "Competitive Programming 3"

import java.util.Scanner;
import java.util.TreeSet;
import java.lang.String;

class Ex1_2_3_4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        TreeSet set = new TreeSet();
        while (true) {
            String s = sc.nextLine();
            try {
                set.add(Integer.parseInt(s));
            } catch (NumberFormatException n) {
                break;
            }
        }
        System.out.println(set.toString());
    }
}
