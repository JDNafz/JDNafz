// import java.time.LocalDate;
import java.util.ArrayList;

class Main {
    public static ArrayList<Book> books = new ArrayList<Book>();
  public static void main(String[] args) {
    User user1 = new User("JD Naf","1992-01-24");

    Book rainbows = new Book("Rainbows on Fire","Kill Joy Frenkins",69);
    EBook bandanas = new EBook("Bandanas","Tom Hanks",420,"mp3");
    AudioBook skysounds = new AudioBook("Skysounds","Skrillex", 60);
    // books.add(rainbows);
    // books.add(bandanas);

    // System.out.println(bandanas.toString());
    
 
    user1.borrow(rainbows);
    user1.borrow(skysounds);
    // rainbows.getInfo();
    System.out.println(books.toString());
    
    // System.out.printf("%s was born back in %s and they are %d years old.", user1.getName(), user1.getBirthDay(), user1.age());

    // System.out.printf("%s has borrowed these books:\n%s \n", user1.getName(), user1.borrowedBooks());

    // System.out.printf("%s by %s", rainbows.getTitle(),skysounds.getAuthor());
  }
}