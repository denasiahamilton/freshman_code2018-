import java.util.Scanner;

public class PerfectNum  {
  public static void main(String [ ] args) {
  int limit;
  int perfect_num;
  int i;
  int factorsum;
  Scanner in;

  in = new Scanner(System.in);
  System.out.println("Enter the upper limit: ");
  limit = in.nextInt();
  perfect_num = 0;

  while (perfect_num <= limit) {
    i = 1;
    factorsum = 0;

    while (i < perfect_num){
      if (perfect_num % i == 0){
        factorsum += 1; }
      i += 1; }

    if (factorsum == perfect_num) {
      System.out.print(perfect_num);
      System.out.println ("is a perfect number!"); }

    perfect_num += 1;
  }
  System.exit(0);
  }
}
