// solution to Exercise 1.2.3 problem #6 from "Competitive Programming 3"

import java.util.Scanner;
import java.util.ArrayList;
import java.lang.Integer;
import java.lang.NumberFormatException;

class Ex1_2_3_6 {
    private ArrayList<Integer> arr;
    public Ex1_2_3_6() { this.arr = new ArrayList<Integer>(); }
    public static void main(String[] args) {
        Ex1_2_3_6 instance = new Ex1_2_3_6();
        Scanner sc = new Scanner(System.in);
        while (true) {
            String s = sc.nextLine();
            try {
               instance.arr.add(Integer.parseInt(s));
            } catch (NumberFormatException n) {
                break;
            } 
        }
        int target = sc.nextInt();
        System.out.println(instance.binary_search(target, 0, instance.arr.size() - 1));
    }
    private int binary_search(int target, int left, int right) {
        if (left > right) return -1;
        int mid = (left + right) / 2;
        if (this.arr.get(mid) < target) return binary_search(target, mid + 1, right);
        if (this.arr.get(mid) > target) return binary_search(target, left, mid - 1);
        return mid;
    }
}
