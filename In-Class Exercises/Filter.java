import java.util.Scanner;
import java.io.File;
import java.io.IOException;
import java.io.BufferedWriter;
import java.io.FileOutputStream;
import java.io.OutputStreamWriter;
import java.io.Writer;

public class Filter {
  public void filterlines(String inputfilename, String outputfilename){
    Scanner lines = null;
    String filtered = "";
    String ln = "";

    try {
          lines = new Scanner(new File(inputfilename));
          while(lines.hasNextLine()) {
            ln = lines.nexLine();
            if (ln.charAt(0) == "I") {
              filtered = filtered + ln + "\n";
            }
          }
          File statText = new File(outputfilename);
          FileOutputStream is = new FileOutputStream(statText);
          OutputStreamWriter osw = new OutputStreamWriter(is);
          Writer w = new BufferedWriter(osw);
          w.write(filtered);
          w.close();
    }

  catch ( IOException e) {
    System.out.println("Sorry but I was unable to open your input file or write to the outputfile");
  }
}

  public static void main(String[] args) {
    Filter filter = new Filter();
    filter.filterlines("input.dat", "javaoutput.txt")
  }
}
