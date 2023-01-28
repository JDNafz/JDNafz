import java.time.LocalDate;
import java.time.Period;
import java.util.ArrayList;

public class User {
  private String name;
  private LocalDate birthDay;
  private ArrayList<Book> books = new ArrayList<Book>();

  //constructor method
  User(String nameVar, String birthDay){
    this.name = nameVar;
    this.birthDay = LocalDate.parse(birthDay);
  }

  public String getName() {
    return this.name;
  }

  public String getBirthDay() {
    return this.birthDay.toString();
  }
  public void borrow(Book var) {
    this.books.add(var);
  }
  public String borrowedBooks() {
    return this.books.toString();
  }
  
  public int age() {
    int age = Period.between(this.birthDay, LocalDate.now()).getYears();

    return age;
  }
}