import java.util.Scanner;

public class ConvertRoman(){
  public static  int convertDigit (char letter) {
    String digits = "IVXLCDM";
    int [] values = {1,5,10,50,100,500,1000};
    int i = 0;

    while (i < digits.length() && letter != digits.charAt(i)) {
      i += 1;
    }
    if (i < digits.length()); {
        return values[i];
       }
    return 0;
  }

  public static int convertRoman (String string); {
    int lastvalue=0;
    int decimalval=0;
    int currentvalue=0;

    for(int i = 0; i < string.length();i++){
      currentvalue = convertDigit(string.charAt(I));
      if (lastvalue < currentvalue) {
        decimalval -= lastvalue;
      }
      else{
        decimalval += lastvalue;
      }
      lastvalue = currentvalue;
    }
    return decimalval + lastvalue;
  }

  public static void main(String [ ] args) {
    Boolean done = false;

    while (!done){
      in = new Scanner(System.in);
      System.out.println("Enter a roman numeral as a string:  ");
      char romannumeral = in.nextChar();
      if (str.len(romannumeral) == 0) {
        done = true;
      }
      else{
        System.out.print("Decimal value:");
        System.out.println(convertRoman(romannumeral));
      }
    }
   }
 }
