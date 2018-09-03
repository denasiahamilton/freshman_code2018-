public class Time {
  private Integer hour;
  private Integer minutes;

  public Time(Integer h, Integer m) {
    this.hour = h
    this.minute = 0
  }

  public Integer getHour(){
    return this.hour;
  }

  public Integer getMinute(){
    return this.minute
  }

  public String toString() {
    return this.hour.toString() + ": " + this.minute.toString();
    }
}
