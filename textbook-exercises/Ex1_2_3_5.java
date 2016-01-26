// solution to Exercise 1.2.3 problem #5 from "Competitive Programming 3"

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Date;
import java.util.Collections;
import java.util.Comparator;
import java.util.GregorianCalendar;
import java.util.Calendar;
import java.lang.String;
import java.text.SimpleDateFormat;
import java.text.ParseException;

class Ex1_2_3_5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        SimpleDateFormat sdf = new SimpleDateFormat("dd MM yyyy");
        ArrayList arr = new ArrayList();
        while (true) {
            String s = sc.nextLine();
            try {
                arr.add(sdf.parse(s));
            } catch (ParseException p) {
                break;
            }
        }
        // sort by month, ascending
        Collections.sort(arr, new Comparator<Date>() {
            public int compare(final Date d1, final Date d2) {
                GregorianCalendar c1 = new GregorianCalendar() {{ setTime(d1); }};
                GregorianCalendar c2 = new GregorianCalendar() {{ setTime(d2); }};
                return c1.get(Calendar.MONTH) - c2.get(Calendar.MONTH);
            }
        });
        System.out.println("Sorted by month:\n" + arr.toString());
        // sort by day, ascending
        Collections.sort(arr, new Comparator<Date>() {
            public int compare(final Date d1, final Date d2) {
                GregorianCalendar c1 = new GregorianCalendar() {{ setTime(d1); }};
                GregorianCalendar c2 = new GregorianCalendar() {{ setTime(d2); }};
                return c1.get(Calendar.DAY_OF_MONTH) - c2.get(Calendar.DAY_OF_MONTH);
            }
        });
        System.out.println("Sorted by day:\n" + arr.toString());
        // sort by age, ascending
        Collections.sort(arr);
        System.out.println("Sorted by age:\n" + arr.toString());
    }
}
